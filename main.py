import threading
import numpy as np
import cv2
from img_utils import save_image, delete_image
from video_utils import start_video_record, end_video_record, delete_video
from filters import FILTERS, apply_filter

recording = False
filtered = False
filter_code = None
vid = None

web_cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

def handle_snapshot(frame):
    try: 
        # take a snapshot
        save_image(frame)

    except Exception as e: 
        print(f"Error: {e}")

def handle_record(frame):
    try: 
        global recording
        global vid
        global fourcc

        # record video
        if not recording: 
            vid = start_video_record(frame, fourcc)

            if vid: 
                print("Recording video...")
                recording = True
        
        else: 
            if vid: 
                end_video_record(vid)
                vid = None

    except Exception as e: 
        print(f"Error: {e}")

def handle_delete(): 
    try: 
        file_type = input("What would you like to delete?\n(I)mage\n(V)ideo\n>").upper

        if file_type == 'I': 
            delete_image()

        elif file_type == 'V': 
            delete_video()

        else: 
            print("Invalid file type")

    except Exception as e: 
        print(f"Error: {e}")

def handle_filter():
    try: 
        global filtered
        global filter_code

        if filtered: 
            filtered = False
            filter_code = None
        
        else: 
            print("Which filter would you like to apply?\n")
            
            i = 0
            for i in range(len(FILTERS)):
                print(f"({i+1}) {FILTERS[i]}\n")

            filter_choice = input(f"Enter number (1 - {len(FILTERS)}): ")
            
            if filter_choice.isdigit(): 
                filter_code = int(filter_choice.strip())

                if filter_code < 1 or filter_code > len(FILTERS): 
                    print("Invalid filter option.")
                    filter_code = None
                
                else:
                    print(f"{FILTERS[filter_code - 1]} will be applied.\n Press 'f' to remove filter.")
                    filtered = True

            else: 
                print("Invalid filter option.")

    except Exception as e: 
        print(f"Error: {e}")

def handle_help(): 
    print("""What would you like to do?\n
    (S) Take a snapshot\n
    (R) Record a video\n
    (D) Delete a file\n
    (F) Apply a filter\n
    (Q) Quit""")
           
print("Welcome to Frame Lab")
handle_help()

while True: 
    ret, frame = web_cam.read()

    if not filtered: 
        cv2.imshow("frame", frame)

    else: 
        image = apply_filter(filter_code, frame)
        cv2.imshow("frame", image)

    if recording and vid: 
        vid.write(frame)

    key = cv2.waitKey(1)

    if key == ord('s'):  
        if filtered: 
            arg = image
        else: 
            arg = frame

        threading.Thread(target=handle_snapshot, args=(arg,), daemon=True).start()
    
    elif key == ord('r'): 
        if filtered: 
            arg = image
        else: 
            arg = frame

        threading.Thread(target=handle_record, args=(arg,), daemon=True).start()

    elif key == ord('d'):
        threading.Thread(target=handle_delete, daemon=True).start()

    elif key == ord('f'): 
        if recording: 
            print("Please stop the recording to change apply filters!")
        else: 
            threading.Thread(target=handle_filter, daemon=True).start()

    elif key == ord('h'):
        threading.Thread(target=handle_help, daemon=True).start()

    elif key == ord('q'): 
        break

if vid: 
    vid.release()

web_cam.release()
cv2.destroyAllWindows()
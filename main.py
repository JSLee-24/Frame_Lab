import numpy as np
import cv2
from img_utils import save_image
from video_utils import start_video_record, end_video_record
from filters import FILTERS, apply_filter

recording = False
filtered = False
filter_code = None
vid = None

web_cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

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

    if key == ord('p'): 
        # take a photo
        save_image(frame)
    
    elif key == ord('r'): 
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

    elif key == ord('f'): 
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

    elif key == ord('q'): 
        break

if vid: 
    vid.release()

web_cam.release()
cv2.destroyAllWindows()
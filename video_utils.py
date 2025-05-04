import os
import cv2

VIDEO_DIR = "Videos"
FRAME_RATE = 30.0

def start_video_record(frame, fourcc): 
    try: 
        vid = None
        height, width = frame.shape[:2]

        if not os.path.exists(VIDEO_DIR): 
            os.makedirs(VIDEO_DIR)

        file_name, _ = input("What would you like to name the snapshot: ").split('.', maxsplit=1)
        file_path = os.path.join(VIDEO_DIR, f'{file_name}.mp4')

        if os.path.exists(file_path): 
            res = input(f"This would overwrite the existsing {file_name}.mp4. Continue (Y/N)? ")

            if res.capitalize() == 'N':
                print("Recording cancelled.")
                return vid
        
        vid = cv2.VideoWriter(file_path, fourcc, FRAME_RATE, (width, height))

    except Exception as e: 
        print(f"Error recording video: {e}")

    finally: 
        return vid    
    
def end_video_record(vid): 
    try: 
        vid.release()
        print("Video saved!")
    
    except Exception as e: 
        print(f"Error ending video recording: {e}")

def delete_video():
    try:         
        file_name, _ = input("Which video would you like to delete?: ").split('.', maxsplit=1)
        file_path = os.path.join(VIDEO_DIR, f"{file_name}.mp4")

        if not os.path.exists(file_path):
            print(f"{file_name}.mp4 does not exist!")
            return
        
        os.remove(file_path)
        print(f"{file_name}.mp4 deleted.")
            
    except Exception as e: 
        print(f"Error deleting a video: {e}") 
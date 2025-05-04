import numpy as np
import cv2
from img_utils import save_image
from video_utils import start_video_record, end_video_record

SNAPSHOT_DIR = "Snapshots"
VIDEO_DIR = "Videos"

recording = False
vid = None

web_cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame_width = int(web_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(web_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True: 
    ret, frame = web_cam.read()

    cv2.imshow('frame', frame)
    
    if recording and vid: 
        vid.write(frame)

    input = cv2.waitKey(1)

    if input == ord('p'): 
        # take a photo
        save_image(frame)
    
    elif input == ord('r'): 
        # record video
        if not recording: 
            vid = start_video_record(fourcc, frame_width, frame_height)

            if vid: 
                print("Recording video...")
                recording = True
        
        else: 
            if vid: 
                end_video_record(vid)
                vid = None

    elif input == ord('q'): 
        break

if vid: 
    vid.release()

web_cam.release()
cv2.destroyAllWindows()
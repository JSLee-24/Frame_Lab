import os
import cv2

SNAPSHOT_DIR = "Snapshots"

def save_image(image):
    try: 
        if not os.path.exists(SNAPSHOT_DIR): 
            os.makedirs(SNAPSHOT_DIR)

        print("Saving snapshot...")
        file_name = input("What would you like to name the snapshot: ")
        file_path = os.path.join(SNAPSHOT_DIR, f"{file_name}.jpg")

        if os.path.exists(file_path): 
            res = input(f"This would overwrite the existsing {file_name}.jpg. Continue (Y/N)? ")

            if res.capitalize() == 'N': 
                print("File not saved.")
                return
        
        cv2.imwrite(file_path, image)
        print("File saved!")

    except Exception as e: 
        print(f"Error saving photo: {e}")

import os
import cv2

IMAGE_DIR = "Images"
PERIOD = '.'

def save_image(image):
    try: 
        if not os.path.exists(IMAGE_DIR): 
            os.makedirs(IMAGE_DIR)

        file_name = input("What would you like to name the image: ")

        if PERIOD in file_name: 
            file_name, _ = file_name.split(PERIOD, maxsplit=1)

        file_path = os.path.join(IMAGE_DIR, f"{file_name}.jpg")

        if os.path.exists(file_path): 
            res = input(f"This would overwrite the existsing {file_name}.jpg. Continue (Y/N)? ")

            if res.upper() == 'N': 
                print("File not saved.")
                return
        
        cv2.imwrite(file_path, image)
        print("File saved!")

    except Exception as e: 
        print(f"Error saving an image: {e}")

def delete_image():
    try:         
        file_name = input("Which image would you like to delete?: ")
        
        if PERIOD in file_name: 
            file_name, _ = file_name.split(PERIOD, maxsplit=1)

        file_path = os.path.join(IMAGE_DIR, f"{file_name}.jpg")

        if not os.path.exists(file_path):
            print(f"{file_name}.jpg does not exist!")
            return
        
        os.remove(file_path)
        print(f"{file_name}.jpg deleted.")
            
    except Exception as e: 
        print(f"Error deleting an image: {e}") 
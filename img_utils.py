import os
import cv2

IMAGE_DIR = "Images"

def save_image(image):
    try: 
        if not os.path.exists(IMAGE_DIR): 
            os.makedirs(IMAGE_DIR)

        print("Saving image...")
        file_name, _ = input("What would you like to name the image: ").split('.', maxsplit=1)
        file_path = os.path.join(IMAGE_DIR, f"{file_name}.jpg")

        if os.path.exists(file_path): 
            res = input(f"This would overwrite the existsing {file_name}.jpg. Continue (Y/N)? ")

            if res.capitalize() == 'N': 
                print("File not saved.")
                return
        
        cv2.imwrite(file_path, image)
        print("File saved!")

    except Exception as e: 
        print(f"Error saving an image: {e}")

def delete_image():
    try:         
        file_name, _ = input("Which image would you like to delete?: ").split('.', maxsplit=1)
        file_path = os.path.join(IMAGE_DIR, f"{file_name}.jpg")

        if not os.path.exists(file_path):
            print(f"{file_name}.jpg does not exist!")
            return
        
        os.remove(file_path)
        print(f"{file_name}.jpg deleted.")
            
    except Exception as e: 
        print(f"Error deleting an image: {e}") 
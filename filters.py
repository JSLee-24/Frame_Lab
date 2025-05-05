import numpy as np
import cv2

FILTERS = [
    "Mirrors",
    "Grayscale", 
    "Inverted", 
    "Sepia Tone", 
    "Gaussian Blur",
    "Canny Edge", 
    "Pencil Sketch", 
    "Pencil Sketch (Coloured)", 
    "Vertical Flip", 
    "Horizontal Flip",
    "Cartoon", 
    "Glitch", 
    "Emboss",
]

def apply_filter(filter_code, frame): 
    filtered = FILTER_FCNS[FILTERS[filter_code - 1]](frame)

    return filtered

def mirrors(frame): 
    height, width = frame.shape[:2]
    shrunk_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    filtered = np.zeros(frame.shape, np.uint8)

    vertical_flipped = vertical_filp(shrunk_frame)
    horizontal_flipped = horizontal_flip(shrunk_frame)

    filtered[:height//2, :width//2] = vertical_flipped
    filtered[height//2:, :width//2] = shrunk_frame
    filtered[:height//2, width//2:] = horizontal_flip(vertical_flipped)
    filtered[height//2:, width//2:] = horizontal_flipped

    return filtered

def grayscale(frame): 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    return gray

def inverted(frame): 
    invert = cv2.bitwise_not(frame)

    return invert

def sepia_tone(frame): 
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia = cv2.transform(frame, kernel)
    sepia = np.clip(sepia, 0, 255)

    return sepia

def gaussian_blur(frame): 
    blurred = cv2.GaussianBlur(frame, (15, 15), 0)

    return blurred

def canny_edge(frame): 
    edges = cv2.Canny(frame, 100, 200)

    return edges

def pencil_sketch(frame): 
    gray, _ = cv2.pencilSketch(frame, sigma_s = 60, sigma_r = 0.07)

    return gray

def colour_pencil_sketch(frame):
    _, colour = cv2.pencilSketch(frame, sigma_s = 60, sigma_r = 0.07)

    return colour

def vertical_filp(frame):
    flipped = cv2.flip(frame, 0)

    return flipped

def horizontal_flip(frame): 
    flipped = cv2.flip(frame, 1)

    return flipped

def cartoon(frame): 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    colour = cv2.bilateralFilter(frame, 9, 300, 300)
    cartoon = cv2.bitwise_and(colour, colour, mask = edges)

    return cartoon

def glitch(frame): 
    blue, green, red = cv2.split(frame)
    glitch = cv2.merge([green, red, blue])

    return glitch

def emboss(frame): 
    kernel = np.array([[ -2, -1, 0],
                        [ -1,  1, 1],
                        [  0,  1, 2]])
    emboss = cv2.filter2D(frame, -1, kernel)

    return emboss

FILTER_FCNS = {
    "Mirrors": mirrors,
    "Grayscale": grayscale, 
    "Inverted": inverted, 
    "Sepia Tone": sepia_tone, 
    "Gaussian Blur": gaussian_blur,
    "Canny Edge": canny_edge, 
    "Pencil Sketch": pencil_sketch, 
    "Pencil Sketch (Coloured)": colour_pencil_sketch, 
    "Vertical Flip": vertical_filp, 
    "Horizontal Flip": horizontal_flip,
    "Cartoon": cartoon, 
    "Glitch": glitch, 
    "Emboss": emboss,
}
import cv2
import hashlib
import numpy as np
from PIL import Image
import time

class CameraHasher:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)


    def calculate_mean(self, pixels):
        total = 0
        count = 0
        for row in pixels:
            for value in row:
                total += value
                count +=1
        return total/count

    def ahash(self, image_array):
        img = Image.fromarray(image_array)
        img = img.resize((16, 16), Image.ANTIALIAS)
        img = img.convert('L')
        pixels = np.array(img)
        avg = self.calculate_mean(pixels)
        
        diff = pixels > avg
        binary_array = diff.flatten()
        secure_hash = hashlib.sha256(binary_array)
        return secure_hash.hexdigest()
    
    def save_processed_image(self, image_array, file_path='processed_image.png'):
        img = Image.fromarray(image_array)
        img = img.resize((16, 16), Image.ANTIALIAS)
        img = img.convert('L')
        img.save(file_path)  # Save the image to disk



    def capture_and_process(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame")
            return None
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.save_processed_image(frame_rgb, "output.png")
        print("ahash: ", self.ahash(frame_rgb))
        return self.ahash(frame_rgb)

    def release_camera(self):
        self.cap.release()

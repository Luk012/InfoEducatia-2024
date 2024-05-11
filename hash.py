import cv2
import numpy as np
from PIL import Image
import string
import time

class CameraHasher:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.chars = string.punctuation + string.digits + string.ascii_letters

    def process_image(self, image_array):
        line_sum = np.sum(image_array, axis=1)
        line_sum_prime = np.sum(line_sum, axis=1) if len(line_sum.shape) > 1 else line_sum
        length = len(self.chars)

        hash_result = []
        for value in line_sum_prime:
            digit = int(value % length)
            hash_result.append(self.chars[digit])

        return ''.join(hash_result)

    def capture_and_process(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame")
            return None
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(frame_rgb)
        return self.process_image(np.array(img_pil))

    def release_camera(self):
        self.cap.release()

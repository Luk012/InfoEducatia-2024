from PIL import Image
import numpy as np
import string


image = Image.open("C:\\Users\\lucad\\OneDrive\\Desktop\\lucutz.jpg")
array = np.array(image)

line_sum = np.sum(array, axis=1)

if len(line_sum.shape) > 1:
    line_sum_prime = np.sum(line_sum, axis=1)
else:
    line_sum_prime = line_sum  

chars = string.punctuation + string.digits + string.ascii_letters
length = len(chars)
chars = list(chars)


hash_result = []
for value in line_sum_prime:
    digit = value % length
    hash_result.append(chars[digit])

hash_string = ''.join(hash_result)
#print(hash_string)
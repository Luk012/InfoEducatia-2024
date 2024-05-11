import time
from password import Password
from hash import CameraHasher
from encrypt import PasswordEncryptor

camera_hasher = CameraHasher()
password_encryptor = PasswordEncryptor(Password)

try:
    while True:
        current_hash = camera_hasher.capture_and_process()
        if current_hash:
            encrypted_password = password_encryptor.write_encrypted_password(current_hash)
            print("Encrypted password:", encrypted_password)
            decrypted_password = password_encryptor.decode_password(encrypted_password, current_hash)
            print("Decrypted password:", decrypted_password)
        
        time.sleep(20)  
finally:
    camera_hasher.release_camera()

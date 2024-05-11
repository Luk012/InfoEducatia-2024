import time
from password import Password
from hash import CameraHasher
from encrypt import PasswordEncryptor
import tkinter as tk

camera_hasher = CameraHasher()
password_encryptor = PasswordEncryptor(Password)

def update_hash():
    global current_hash 
    current_hash = camera_hasher.capture_and_process()
    root.after(20000, update_hash)

root = tk.Tk()

root.geometry("500x500")
root.title("Bioactive Encryption")

label = tk.Label(root, text = "Bioactive Encryption", font  = ('Arial', 18))
label.pack(padx = 20, pady = 20)

passwordbox = tk.Text(root, height = 1, width = 20, font = ('Arial' , 18))
passwordbox.place(x = 10, y = 100)

showtext = tk.Text(root, height = 1, width = 50, font = ('Arial', 12))
showtext.config(state = tk.DISABLED)
showtext.place(x = 10, y = 200)

def show_encrypted_passsword():
    password= passwordbox.get(1.0, tk.END)  
    password_encryptor = PasswordEncryptor(password)
    print(password)
    global encrypted_password
    encrypted_password = password_encryptor.write_encrypted_password(current_hash)
    print("Encrypted password:", encrypted_password)
    decrypted_password = password_encryptor.decode_password(encrypted_password, current_hash)
    print("Decrypted password:", decrypted_password)
    root.after(20000, update_hash)
    showtext.config(state = tk.NORMAL)
    showtext.delete(1.0, tk.END)
    showtext.insert(1.0, encrypted_password)
    showtext.config(state = tk.DISABLED)

button = tk.Button(root, text = "Get Encrypted Password", font = ('Arial', 12), command = show_encrypted_passsword)
button.place(x = 10, y = 150)


update_hash()
root.mainloop()

import time
import tkinter as tk
from PIL import Image, ImageTk
from password import Password
from hash import CameraHasher
from encrypt import PasswordEncryptor

camera_hasher = CameraHasher()
current_hash = None

def update_hash():
    global current_hash
    current_hash = camera_hasher.capture_and_process()
    root.after(20000, update_hash)

root = tk.Tk()
root.geometry("500x500")
root.title("Bioactive Encryption")

image = Image.open("fishuuuu.png")
photo = ImageTk.PhotoImage(image)

bg_label = tk.Label(root, image=photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(root, text="Bioactive Encryption", font=('Arial Bold', 18), background='#1a1a1a', fg='#5e6eff', borderwidth=0)
label.pack(padx=20, pady=20)

passwordbox = tk.Entry(root, font=('Arial Bold', 18), background="#1a1a1a", fg='#5e6eff', borderwidth=0)
passwordbox.place(x=10, y=100)

showtext = tk.Text(root, height=1, width=50, font=('Arial Bold', 12), background="#1a1a1a", fg='#5e6eff', borderwidth=0)
showtext.config(state=tk.DISABLED)
showtext.place(x=10, y=200)

def show_encrypted_password():
    password = passwordbox.get()
    if not password or not current_hash:
        print("Password or hash is missing.")
        return
    password_encryptor = PasswordEncryptor(password.strip())
    encrypted_password = password_encryptor.write_encrypted_password(current_hash)
    decrypted_password = password_encryptor.decode_password(encrypted_password, current_hash)
    print("Encrypted password:", encrypted_password)
    print("Decrypted password:", decrypted_password)

    showtext.config(state=tk.NORMAL)
    showtext.delete(1.0, tk.END)
    showtext.insert(1.0, encrypted_password)
    showtext.config(state=tk.DISABLED)

button = tk.Button(root, text="Get Encrypted Password", font=('Arial Bold', 12), command=show_encrypted_password, background="#1a1a1a", fg='#5e6eff', borderwidth=0)
button.place(x=10, y=150)

update_hash()
root.mainloop()

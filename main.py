import time
import tkinter as tk
from PIL import Image, ImageTk
from password import Password
from hash import CameraHasher
from encrypt import PasswordEncryptor

camera_hasher = CameraHasher()
current_hash = None

root = tk.Tk()
root.geometry("1000x1000")
root.title("Bioactive Encryption")

MenuPage = tk.Frame(root)
EncryptPage = tk.Frame(root)
DecryptPage = tk.Frame(root)
ImagePage = tk.Frame(root)

MenuPage.grid(row = 0, column = 0, sticky = 'nsew')
EncryptPage.grid(row = 0, column = 0, sticky = 'nsew')
DecryptPage.grid(row = 0, column = 0, sticky = 'nsew')
ImagePage.grid(row = 0, column = 0, sticky = 'nsew')
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

image = Image.open("fishuuuu.png")
photo = ImageTk.PhotoImage(image)

def switch_page(page):
    page.tkraise()

menu_bg_label = tk.Label(MenuPage, image=photo)
menu_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

menu_label = tk.Label(MenuPage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#1a1a1a', fg='#5e6eff', borderwidth=0)
menu_label.pack(padx = 20, pady = 20)

switch_encryption_button = tk.Button(MenuPage, text="Encryption", font=('Arial Bold', 18), background="#1a1a1a", fg='#5e6eff', borderwidth=0, command = lambda: switch_page(EncryptPage))
switch_encryption_button.pack(padx = 100, pady = 100)

switch_decryption_button = tk.Button(MenuPage, text="Decryption", font=('Arial Bold', 18), background="#1a1a1a", fg='#5e6eff', borderwidth=0, command = lambda: switch_page(DecryptPage))
switch_decryption_button.pack(padx = 100, pady = 50)

switch_image_button = tk.Button(MenuPage, text="Images", font=('Arial Bold', 18), background="#1a1a1a", fg='#5e6eff', borderwidth=0, command = lambda: switch_page(ImagePage))
switch_image_button.pack(padx = 100, pady = 50)


#Encrypt Page

encrypt_bg_label = tk.Label(EncryptPage, image=photo)
encrypt_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(EncryptPage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#1a1a1a', fg='#5e6eff', borderwidth=0)
label.pack(padx=20, pady=20)

passwordbox = tk.Entry(EncryptPage, font=('Arial Bold', 18), background="#1a1a1a", fg='#5e6eff', borderwidth=0)
passwordbox.place(x=10, y=100)

showtext = tk.Text(EncryptPage, height=1, width=50, font=('Arial Bold', 12), background="#1a1a1a", fg='#5e6eff', borderwidth=0)
showtext.config(state=tk.DISABLED)
showtext.place(x=10, y=200)

encrypt_back_button = tk.Button(EncryptPage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#1a1a1a", fg='#5e6eff', borderwidth=0)
encrypt_back_button.place(x = 10, y = 20)

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

button = tk.Button(EncryptPage, text="Get Encrypted Password", font=('Arial Bold', 12), command=show_encrypted_password, background="#1a1a1a", fg='#5e6eff', borderwidth=0)
button.place(x=10, y=150)

#Decrypt Page

decrypt_bg_label = tk.Label(DecryptPage, image = photo)
decrypt_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

decrypt_label = tk.Label(DecryptPage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#1a1a1a', fg='#5e6eff', borderwidth=0)
decrypt_label.pack(padx=20, pady=20)

decrypt_back_button = tk.Button(DecryptPage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#1a1a1a", fg='#5e6eff', borderwidth=0)
decrypt_back_button.place(x = 10, y = 20)

passwordbox2 = tk.Entry(DecryptPage, font=('Arial Bold', 18), background="#1a1a1a", fg="#5e6eff",  borderwidth=0)
passwordbox2.place(x = 10, y = 100)

showtext2 = tk.Text(DecryptPage, height = 1, width = 50, font=('Arial Bold', 12), background="#1a1a1a", fg='#5e6eff', borderwidth=0)
showtext.config(state = tk.DISABLED)
showtext2.place(x=10, y=200)

def show_decrypted_password():
    encrypted_password = passwordbox2.get()
    if not encrypted_password or not current_hash:
        print("Encrypted password or hash is missing.")
        return
    passowrd_decryptor = PasswordEncryptor(None)
    decrypted_password = passowrd_decryptor.decode_password(encrypted_password, current_hash)
    print("Dectrypted password:", decrypted_password)

    showtext2.config(state=tk.NORMAL)
    showtext2.delete(1.0, tk.END)
    showtext2.insert(1.0, encrypted_password)
    showtext2.config(state=tk.DISABLED)



decrypt_button = tk.Button(DecryptPage, text="Get Decrypted Password", font = ('Arial Bold', 12), command=show_decrypted_password, background="#1a1a1a", fg='#5e6eff', borderwidth=0)
decrypt_button.place(x = 10, y = 150)

#Image Page

image_bg_label = tk.Label(ImagePage, image = photo)
image_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

image_label = tk.Label(ImagePage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#1a1a1a', fg='#5e6eff', borderwidth=0)
image_label.pack(padx=20, pady=20)

standard_image_label = tk.Label(ImagePage, image=photo)
standard_image_label.place(x = 100, y = 100)

processed_image_label = tk.Label(ImagePage, image=photo)
processed_image_label.place(x = 600, y = 100)

encrypt_key_label = tk.Label(ImagePage, text = "Encrypted Key: ", font = ('Arial Bold', 18), background='#1a1a1a', fg='#5e6eff', borderwidth=0)
encrypt_key_label.place(x = 100, y = 800)

MenuPage.tkraise()

def update_hash():
    global current_hash
    current_hash = camera_hasher.capture_and_process()
    img = Image.open("standard.png")
    img = img.resize((400,400))
    standard_image = ImageTk.PhotoImage(img)
    standard_image_label.config(image = standard_image)
    standard_image_label.image = standard_image
    img = Image.open("output.png")
    img = img.resize((400,400))
    processed_image = ImageTk.PhotoImage(img)
    processed_image_label.config(image = processed_image)
    processed_image_label.image = processed_image
    encrypt_key_label.config(text = "Ecryption Key: " + current_hash)
    root.after(20000, update_hash)

update_hash()
root.mainloop()

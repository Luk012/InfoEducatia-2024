import time
import tkinter as tk
from PIL import Image, ImageTk
from password import Password
from hash import CameraHasher
from encrypt import PasswordEncryptor

camera_hasher = CameraHasher()
current_hash = None

root = tk.Tk()
root.geometry("1920x1080")
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
image = image.resize((3000, 3000))
photo = ImageTk.PhotoImage(image)

def hover_effect(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background = colorOnHover))

    button.bind("<Leave>", func=lambda e: button.config(background = colorOnLeave))

def switch_page(page):
    page.tkraise()

#Menu Page

menu_bg_label = tk.Label(MenuPage, image=photo)
menu_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

menu_label = tk.Label(MenuPage, text="Bioactive Encryption", font=('Arial Bold', 25), background='#131414', fg='#5e6eff', borderwidth=0)
menu_label.pack(padx = 20, pady = 20)

switch_encryption_button = tk.Button(MenuPage, text="Encryption", font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0, command = lambda: switch_page(EncryptPage))
switch_encryption_button.pack(padx = 100, pady = 100)
hover_effect(switch_encryption_button, "#0e0f0f", '#131414')

switch_decryption_button = tk.Button(MenuPage, text="Decryption", font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0, command = lambda: switch_page(DecryptPage))
switch_decryption_button.pack(padx = 100, pady = 50)
hover_effect(switch_decryption_button, "#0e0f0f", '#131414')

switch_image_button = tk.Button(MenuPage, text="Images", font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0, command = lambda: switch_page(ImagePage))
switch_image_button.pack(padx = 100, pady = 50)
hover_effect(switch_image_button, "#0e0f0f", '#131414')


#Encrypt Page

encrypt_bg_label = tk.Label(EncryptPage, image=photo)
encrypt_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(EncryptPage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#131414', fg='#5e6eff', borderwidth=0)
label.pack(padx=20, pady=20)

passwordbox = tk.Entry(EncryptPage, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
passwordbox.pack(padx = 10, pady = 50)

showtext = tk.Text(EncryptPage, height=1, width=50, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
showtext.config(state=tk.DISABLED)
showtext.pack(padx=20, pady=50)

encrypt_back_button = tk.Button(EncryptPage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#131414", fg='#5e6eff', borderwidth=0)
encrypt_back_button.place(x = 10, y = 20)
hover_effect(encrypt_back_button, "#0e0f0f", '#131414')

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

button = tk.Button(EncryptPage, text="Get Encrypted Password", font=('Arial Bold', 40), command=show_encrypted_password, background="#131414", fg='#5e6eff', borderwidth=0)
button.pack(padx = 10, pady= 100)
hover_effect(button, "#0e0f0f", '#131414')

#Decrypt Page

decrypt_bg_label = tk.Label(DecryptPage, image = photo)
decrypt_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

decrypt_label = tk.Label(DecryptPage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#131414', fg='#5e6eff', borderwidth=0)
decrypt_label.pack(padx=20, pady=20)

decrypt_back_button = tk.Button(DecryptPage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_back_button.place(x = 10, y = 20)
hover_effect(decrypt_back_button, "#0e0f0f", '#131414')

passwordbox2 = tk.Entry(DecryptPage, font=('Arial Bold', 25), background="#131414", fg="#5e6eff",  borderwidth=0)
passwordbox2.pack(padx = 20, pady = 50)

showtext2 = tk.Text(DecryptPage, height = 1, width = 50, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
showtext.config(state = tk.DISABLED)
showtext2.pack(padx=10, pady=50)

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
    showtext2.insert(1.0, decrypted_password)
    showtext2.config(state=tk.DISABLED)



decrypt_button = tk.Button(DecryptPage, text="Get Decrypted Password", font = ('Arial Bold', 40), command=show_decrypted_password, background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_button.pack(padx=10, pady=75)
hover_effect(decrypt_button, "#0e0f0f", '#131414')

#Image Page

image_bg_label = tk.Label(ImagePage, image = photo)
image_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

image_label = tk.Label(ImagePage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#131414', fg='#5e6eff', borderwidth=0)
image_label.pack(padx=20, pady=20)

standard_image_label = tk.Label(ImagePage, image=photo)
standard_image_label.pack(side = 'left', padx = 20, pady = 10)

processed_image_label = tk.Label(ImagePage, image=photo)
processed_image_label.pack(side = 'left', padx = 20, pady = 10)

encrypt_key_label = tk.Label(ImagePage, text = "Encrypted Key: ", font = ('Arial Bold', 16), background='#131414', fg='#5e6eff', borderwidth=0)
encrypt_key_label.pack(padx=20, pady=20, side = 'top')

image_back_button = tk.Button(ImagePage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#131414", fg='#5e6eff', borderwidth=0)
image_back_button.place(x=10, y=20)
hover_effect(image_back_button, "#0e0f0f", '#131414')

MenuPage.tkraise()

timer_id = None

def update_hash():
    global timer_id
    if timer_id:
        root.after_cancel(timer_id)
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
    timer_id = root.after(20000, update_hash)

generate_hash_button = tk.Button(ImagePage, text = "Generate New Hash", font=('Arial Black', 12), command = update_hash, background="#131414", fg='#5e6eff', borderwidth=0)
generate_hash_button.pack(padx = 20, pady= 20 ,side = 'top')
hover_effect(generate_hash_button, '#0e0f0f', '#131414')

update_hash()
root.mainloop()

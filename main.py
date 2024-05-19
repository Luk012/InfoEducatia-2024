import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from hash import CameraHasher
from encrypt import PasswordEncryptor

camera_hasher = CameraHasher()
current_hash = None

root = tk.Tk()
root.geometry("1920x1080")
root.title("Bioactive Encryption")

MenuPage = tk.Frame(root)
FilePage = tk.Frame(root)
EncryptPage = tk.Frame(root)
DecryptPage = tk.Frame(root)
DecryptFilePage = tk.Frame(root)
ImagePage = tk.Frame(root)

MenuPage.grid(row = 0, column = 0, sticky = 'nsew')
FilePage.grid(row = 0, column = 0, sticky = 'nsew')
EncryptPage.grid(row = 0, column = 0, sticky = 'nsew')
DecryptPage.grid(row = 0, column = 0, sticky = 'nsew')
DecryptFilePage.grid(row = 0, column = 0, sticky = 'nsew')
ImagePage.grid(row = 0, column = 0, sticky = 'nsew')
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

image = Image.open("fishuuuu.png")
image = image.resize((3000, 3000))
photo = ImageTk.PhotoImage(image)

file_path = None

timer_id = None

def update_hash(widget):
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
    if widget:
        widget.delete(0, tk.END)
        widget.insert(0, current_hash)

def hover_effect(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background = colorOnHover))

    button.bind("<Leave>", func=lambda e: button.config(background = colorOnLeave))

def on_focus_in(event, widget, placeholder):
    if widget.get().strip() == placeholder:
        widget.delete(0, tk.END)
        widget.config(fg = "#5e6eff")

def on_focus_out(event, widget, placeholder):
    if not widget.get().strip():
        widget.insert(0, placeholder)
        widget.config(fg = "#c2d9fc")

def place_holder_text(widget, placeholder):
    widget.insert(0, placeholder)
    widget.bind("<FocusIn>", lambda event: on_focus_in(event, widget, placeholder))
    widget.bind("<FocusOut>", lambda event: on_focus_out(event, widget, placeholder))

def switch_page(page):
    page.tkraise()

def remove_text(text_to_remove):
    text_to_remove.destroy()

def upload_file():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select a .txt file",
        filetypes=[(".txt files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        uploaded_text = tk.Label(FilePage, text="Uploaded File " + file_path, font=('Arial Bold', 25), background='#131414', fg='#5e6eff', borderwidth=0)
        uploaded_text.pack(padx=10, pady=20)
        root.after(2000, lambda: remove_text(uploaded_text))
        
def encrypt_file(file_path, hash):
    if not hash:
        print("Hash is missing.")
        return
    
    if not file_path:
        no_file_label = tk.Label(FilePage, text="No File Uploaded", font=('Arial Bold', 25), background='#131414', fg='#5e6eff', borderwidth=0)
        no_file_label.pack(padx=10, pady=20)
        root.after(2000, lambda: remove_text(no_file_label))
        return
    
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    password_encryptor = PasswordEncryptor(file_content.strip())
    encrypted_content = password_encryptor.write_encrypted_password(hash)

    save_path = filedialog.asksaveasfilename(
        title="Save Encrypted File As",
        defaultextension='.txt',
        filetypes=[("Text files", "*.txt")]
    )

    if save_path:
        with open(save_path, 'w')as file:
            file.write(encrypted_content)

def decrypt_file(file_path, hash):
    if not hash:
        print("Hash is missing.")
        return
    
    if not file_path:
        no_file_label = tk.Label(FilePage, text="No File Uploaded", font=('Arial Bold', 25), background='#131414', fg='#5e6eff', borderwidth=0)
        no_file_label.pack(padx=10, pady=20)
        root.after(2000, lambda: remove_text(no_file_label))
        return
    
    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    password_decryptor = PasswordEncryptor(None)
    decrypted_content = password_decryptor.decode_password(file_content, hash)

    save_path = filedialog.asksaveasfilename(
        title="Save Encrypted File As",
        defaultextension='.txt',
        filetypes=[("Text files", "*.txt")]
    )

    if save_path:
        with open(save_path, 'w')as file:
            file.write(decrypted_content)



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

#Encrypt File Page

file_bg_label = tk.Label(FilePage, image=photo)
file_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

file_label = tk.Label(FilePage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#131414', fg='#5e6eff', borderwidth=0)
file_label.pack(padx=20, pady=20)

switch_to_password_button = tk.Button(FilePage, text="Switch to password", font=('Arial Bold', 12), command= lambda: switch_page(EncryptPage), background="#131414", fg='#5e6eff', borderwidth=0)
switch_to_password_button.pack(padx = 10, pady = 20)
hover_effect(switch_to_password_button, "#0e0f0f", '#131414')

ask_for_file_button = tk.Button(FilePage, text="Upload file", font=('Arial Bold', 25), command= upload_file, background="#131414", fg='#5e6eff', borderwidth=0)
ask_for_file_button.pack(padx=10, pady=20)
hover_effect(ask_for_file_button, "#0e0f0f", '#131414')

encrypt_file_hashbox = tk.Entry(FilePage, width=65, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
encrypt_file_hashbox.pack(padx = 10, pady = 50)

generate_new_hash = tk.Button(FilePage, text="Generate Hash", font=('Arial Bold', 12), command= lambda: update_hash(encrypt_file_hashbox), background="#131414", fg='#5e6eff', borderwidth=0)
generate_new_hash.pack(padx=10, pady=20)

encrypt_file_button = tk.Button(FilePage, text="Encrypt file", font=('Arial Bold', 25), command= lambda: encrypt_file(file_path, encrypt_file_hashbox.get()), background="#131414", fg='#5e6eff', borderwidth=0)
encrypt_file_button.pack(padx=10, pady=20)
hover_effect(encrypt_file_button, "#0e0f0f", '#131414')

file_back_button = tk.Button(FilePage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#131414", fg='#5e6eff', borderwidth=0)
file_back_button.place(x = 10, y = 20)
hover_effect(file_back_button, "#0e0f0f", '#131414')

#Encrypt Password Page

encrypt_bg_label = tk.Label(EncryptPage, image=photo)
encrypt_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(EncryptPage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#131414', fg='#5e6eff', borderwidth=0)
label.pack(padx=20, pady=20)

switch_to_file_button = tk.Button(EncryptPage, text="Switch to file", font=('Arial Bold', 12), command= lambda: switch_page(FilePage), background="#131414", fg='#5e6eff', borderwidth=0)
switch_to_file_button.pack(padx = 10, pady = 20)
hover_effect(switch_to_file_button, "#0e0f0f", '#131414')

passwordbox = tk.Entry(EncryptPage, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
passwordbox.pack(padx = 10, pady = 50)

encrypt_hashbox = tk.Entry(EncryptPage, width=65, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
encrypt_hashbox.pack(padx = 10, pady = 50)

generate_new_hash = tk.Button(EncryptPage, text="Generate Hash", font=('Arial Bold', 12), command= lambda: update_hash(encrypt_hashbox), background="#131414", fg='#5e6eff', borderwidth=0)
generate_new_hash.pack(padx=10, pady=20)

showtext = tk.Text(EncryptPage, height=1, width=50, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
showtext.config(state=tk.DISABLED)
showtext.pack(padx=20, pady=50)

encrypt_back_button = tk.Button(EncryptPage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#131414", fg='#5e6eff', borderwidth=0)
encrypt_back_button.place(x = 10, y = 20)
hover_effect(encrypt_back_button, "#0e0f0f", '#131414')

def show_encrypted_password():
    password = passwordbox.get()
    hash = encrypt_hashbox.get()
    if not password or not hash:
        print("Password or hash is missing.")
        return
    password_encryptor = PasswordEncryptor(password.strip())
    encrypted_password = password_encryptor.write_encrypted_password(hash)
    decrypted_password = password_encryptor.decode_password(encrypted_password, hash)
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

decrypt_switch_to_file_button = tk.Button(DecryptPage, text="Switch to file", font=('Arial Bold', 12), command= lambda: switch_page(DecryptFilePage), background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_switch_to_file_button.pack(padx = 10, pady = 20)
hover_effect(decrypt_switch_to_file_button, "#0e0f0f", '#131414')

decrypt_back_button = tk.Button(DecryptPage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_back_button.place(x = 10, y = 20)
hover_effect(decrypt_back_button, "#0e0f0f", '#131414')

passwordbox2 = tk.Entry(DecryptPage, font=('Arial Bold', 25), background="#131414", fg="#5e6eff",  borderwidth=0)
passwordbox2.pack(padx = 20, pady = 50)

decrypt_hashbox = tk.Entry(DecryptPage, width=65, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_hashbox.pack(padx = 10, pady = 50)

showtext2 = tk.Text(DecryptPage, height = 1, width = 50, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
showtext.config(state = tk.DISABLED)
showtext2.pack(padx=10, pady=50)

def show_decrypted_password():
    encrypted_password = passwordbox2.get()
    hash = decrypt_hashbox.get()
    if not encrypted_password or not current_hash:
        print("Encrypted password or hash is missing.")
        return
    passowrd_decryptor = PasswordEncryptor(None)
    decrypted_password = passowrd_decryptor.decode_password(encrypted_password, hash)
    print("Dectrypted password:", decrypted_password)

    showtext2.config(state=tk.NORMAL)
    showtext2.delete(1.0, tk.END)
    showtext2.insert(1.0, decrypted_password)
    showtext2.config(state=tk.DISABLED)

decrypt_button = tk.Button(DecryptPage, text="Get Decrypted Password", font = ('Arial Bold', 40), command=show_decrypted_password, background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_button.pack(padx=10, pady=75)
hover_effect(decrypt_button, "#0e0f0f", '#131414')

#Decrypt File Page

decrypt_file_bg_label = tk.Label(DecryptFilePage, image = photo)
decrypt_file_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

decrypt_file_label = tk.Label(DecryptFilePage, text="Bioactive Encryption", font=('Arial Bold', 18), background='#131414', fg='#5e6eff', borderwidth=0)
decrypt_file_label.pack(padx=20, pady=20)

decrypt_switch_to_password_button = tk.Button(DecryptFilePage, text="Switch to password", font=('Arial Bold', 12), command= lambda: switch_page(DecryptPage), background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_switch_to_password_button.pack(padx = 10, pady = 20)
hover_effect(decrypt_switch_to_password_button, "#0e0f0f", '#131414')

decrypt_ask_for_file_button = tk.Button(DecryptFilePage, text="Upload file", font=('Arial Bold', 25), command= upload_file, background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_ask_for_file_button.pack(padx=10, pady=20)
hover_effect(ask_for_file_button, "#0e0f0f", '#131414')

decrypt_file_hashbox = tk.Entry(DecryptFilePage, width=65, font=('Arial Bold', 25), background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_file_hashbox.pack(padx = 10, pady = 50)

decrypt_file_button = tk.Button(DecryptFilePage, text="Decrypt file", font=('Arial Bold', 25), command= lambda: decrypt_file(file_path, decrypt_file_hashbox.get()), background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_file_button.pack(padx=10, pady=20)
hover_effect(decrypt_file_button, "#0e0f0f", '#131414')

decrypt_file_back_button = tk.Button(DecryptFilePage, text="Back", font=('Arial Bold', 12), command= lambda: switch_page(MenuPage), background="#131414", fg='#5e6eff', borderwidth=0)
decrypt_file_back_button.place(x = 10, y = 20)
hover_effect(decrypt_file_back_button, "#0e0f0f", '#131414')

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

generate_hash_button = tk.Button(ImagePage, text = "Generate New Hash", font=('Arial Black', 12), command = lambda: update_hash(None), background="#131414", fg='#5e6eff', borderwidth=0)
generate_hash_button.pack(padx = 20, pady= 20 ,side = 'top')
hover_effect(generate_hash_button, '#0e0f0f', '#131414')

update_hash(None)

MenuPage.tkraise()

root.mainloop()

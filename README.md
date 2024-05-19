# Aplicația Bioactive Encryption

Această aplicație oferă o interfață grafică pentru utilizator (GUI) pentru diverse sarcini legate de criptare, cum ar fi generarea de fișiere ZIP protejate prin parolă, criptarea și decriptarea fișierelor și parolelor și generarea de hash-uri bazate pe imagini.

## Funcționalități

1. **Criptare și Decriptare Parole**: Criptează parole cu un hash generat și decriptează-le.
2. **Criptare și Decriptare Fișiere**: Criptează și decriptează fișiere text folosind un hash generat.
3. **Generare Fișiere ZIP Protejate prin Parolă**: Selectează multiple fișiere, introduce o parolă și generează un fișier ZIP protejat prin parolă.
4. **Generare Hash din Imagini**: Generează hash-uri din imagini capturate cu o cameră conectată.

## Cerințe

- Python 3.x
- Tkinter
- PIL (Pillow)
- OpenCV
- NumPy
- pyminizip

## Instalare

1. Clonează repository-ul sau descarcă codul sursă.
2. Instalează pachetele necesare folosind pip:
   ```sh
   pip install tkinter pillow opencv-python-headless numpy pyminizip
Utilizare

Rulează aplicația principală:

sh
Copy code
python main.py
GUI-ul se va deschide cu mai multe opțiuni:

Encryption: Criptează parole cu un hash generat.
Decryption: Decriptează parole folosind un hash.
ZIP Files: Selectează multiple fișiere, specifică o parolă și generează un fișier ZIP protejat prin parolă.
Images: Generează hash-uri din imagini capturate cu o cameră conectată.
Structura Fișierelor

main.py: Fișierul principal care conține GUI-ul și logica aplicației.
encrypt.py: Conține clasa PasswordEncryptor pentru criptarea și decriptarea parolelor.
hash.py: Conține clasa CameraHasher pentru generarea hash-urilor bazate pe imagini.
password.py: Conține o parolă de test pentru scopuri de testare.
Clase și Metode

PasswordEncryptor
xor_encrypt(data, key): Criptează datele folosind XOR și o cheie.
write_encrypted_password(hash_string): Criptează parola cu un șir de hash.
decode_password(encoded_password, hash_string): Decriptează parola cu un șir de hash.
CameraHasher
calculate_mean(pixels): Calculează media valorilor pixelilor.
ahash(image_array): Generează un hash mediu (ahash) dintr-o imagine.
capture_and_process(): Capturează o imagine de la cameră și o procesează.
release_camera(): Eliberează camera.
Pagini GUI

MenuPage
Meniul principal cu opțiuni pentru a naviga la diferite funcționalități.
EncryptPage
Criptează parole cu un hash generat.
DecryptPage
Decriptează parole folosind un hash.
FilePage
Criptează fișiere text folosind un hash generat.
DecryptFilePage
Decriptează fișiere text folosind un hash.
GenerateZIP
Selectează fișiere, specifică o parolă și generează un fișier ZIP protejat prin parolă.
Specifică numele folderului în care să salvezi fișierul ZIP generat și informațiile despre parolă.
ImagePage
Generează hash-uri din imagini capturate cu o cameră conectată.
Cum să Contribui

Forkează repository-ul.
Creează un branch nou (git checkout -b feature-branch).
Fă modificările tale și commit (git commit -m 'Adaugă funcționalitate nouă').
Fă push la branch (git push origin feature-branch).
Deschide un Pull Request.
Licență

Acest proiect este licențiat sub Licența MIT - vezi fișierul LICENSE pentru detalii.

Mulțumiri

Mulțumiri speciale dezvoltatorilor bibliotecilor utilizate în acest proiect: Tkinter, Pillow, OpenCV, NumPy, și pyminizip.

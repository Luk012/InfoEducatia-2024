# Bioactive Encryption Project

## Descriere
Acest proiect implementează un sistem de criptare bioactivă care utilizează hash-uri generate din imagini capturate pentru a cripta și decripta fișiere. Proiectul este construit folosind Python și include o interfață grafică pentru utilizator (GUI) bazată pe Tkinter.

## Structura Proiectului
Proiectul conține următoarele fișiere:
- `encrypt.py`: Conține clasele și funcțiile necesare pentru criptarea și decriptarea parolelor.
- `hash.py`: Conține funcționalitatea pentru generarea hash-urilor din imagini.
- `main.py`: Punctul de intrare al aplicației, care configurează GUI-ul și gestionează fluxul principal al aplicației.

## Instalare
1. Clonează acest repository:
    ```bash
    git clone <repository-url>
    ```
2. Navighează în directorul proiectului:
    ```bash
    cd <repository-directory>
    ```
3. Instalează pachetele necesare:
    ```bash
    pip install -r requirements.txt
    ```

## Utilizare
1. Rulează aplicația:
    ```bash
    python main.py
    ```
2. Utilizează interfața grafică pentru a selecta fișierele pe care dorești să le criptezi sau decriptezi.
3. Folosește opțiunile disponibile în GUI pentru a genera hash-uri, cripta fișiere și genera arhive ZIP criptate.

## Dependințe
- Python 3.x
- Tkinter
- PIL (Pillow)
- pyminizip

## Funcționalități
### Criptare
- Selectează fișierele pe care dorești să le criptezi.
- Generează un hash dintr-o imagine capturată.
- Utilizează hash-ul pentru a cripta fișierele selectate.

### Decriptare
- Selectează fișierele criptate pe care dorești să le decriptezi.
- Introdu hash-ul corect pentru a decripta fișierele.

### Generare ZIP
- Creează arhive ZIP criptate ale fișierelor selectate.

## Autor
- Luk012
- 1Arekkusu

Mulțumim pentru utilizarea Bioactive Encryption!

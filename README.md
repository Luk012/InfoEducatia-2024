# Bioactive Encryption Project

## Descriere
Acest proiect implementează un sistem de criptare bioactivă care utilizează hash-uri generate din imagini capturate pentru a cripta și decripta fișiere. Proiectul este construit folosind Python și include o interfață grafică pentru utilizator (GUI) bazată pe Tkinter.

## Structura Proiectului
Proiectul conține următoarele fișiere:
- `encrypt.py`: Conține clasele și funcțiile necesare pentru criptarea și decriptarea parolelor.
- `hash.py`: Conține funcționalitatea pentru generarea hash-urilor din imagini.
- `main.py`: Punctul de intrare al aplicației, care configurează GUI-ul și gestionează fluxul principal al aplicației.
- `password.py`: Conține parola utilizată pentru criptare.
- `requirements.txt`: Conține lista de pachete necesare pentru proiect.

## Instalare
1. Clonează acest repository:
    ```bash
    git clone https://github.com/Luk012/InfoEducatia-2024.git
    ```
2. Navighează în directorul proiectului:
    ```bash
    cd InfoEducatia-2024
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
- Tkinter (inclus în Python)
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

## Contribuții
Contribuțiile sunt binevenite! Te rugăm să deschizi un pull request sau să raportezi probleme în secțiunea de issues.

## Autor
- Luk012
- 1Arkkusu

Mulțumim pentru utilizarea Bioactive Encryption!

import random, os, datetime

def wczytaj_dane(pytania, odpowiedzi):
    if not os.path.exists("pytania.txt") or not os.path.exists("odpowiedzi.txt"):
        print("Brak plików z pytaniami lub odpowiedziami.")
        return None
    
        
        return baza

def uruchom_quiz(baza, k):
    pass

def zapisz_wyniki(imie, nazwisko, wynik, k):
    # Format imie;nazwisko;wynik;liczba_pytan;data
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("wyniki.txt", "a", encoding="utf-8") as f:
        f.write(f"{imie};{nazwisko};{wynik};{k};{data}\n")
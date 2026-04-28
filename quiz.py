import random, os, datetime

def wczytaj_dane():
    if not os.path.exists("pytania.txt") or not os.path.exists("odpowiedzi.txt"):
        print("Brak plików z pytaniami lub odpowiedziami.")
        return None
    
    pytania = []
    with open("pytania.txt", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip() and l.strip() != "==="]
    
    odpowiedzi = {}
    with open("odpowiedzi.txt", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                nr, litera = line.strip().split(":")
                odpowiedzi[int(nr)] = litera.strip()
    
    return {"pytania": lines, "odpowiedzi": odpowiedzi}

def uruchom_quiz(baza, k):
    if baza is None:
        return 0
    
    wszystkie = baza["pytania"]
    odpowiedzi = baza["odpowiedzi"]
   
     # Losuj 10-20 pytań (k z parametru lub domyślnie 15)
    n = k if k else 15
    wylosowane = random.sample(wszystkie, min(n, len(wszystkie)))
    
    wynik = 0
    
    for i, pytanie in enumerate(wylosowane, 1):
        print(f"\n{i}. {pytanie}")
        # UWAGA: pytania.txt w obecnym formacie nie zawiera podziału na odpowiedzi A-D
        # Zakładając format: "Treść pytania?" + "Odpowiedź A" + "Odpowiedź B" + ...
        
        odp = input("Wpisz odpowiedź (A/B/C/D): ").upper()
        
        # Sprawdź czy poprawna (szukamy w słowniku odpowiedzi)
        # Problem: jak mapować wylosowane pytanie do numeru w odpowiedzi.txt?
        
        if odp == odpowiedzi.get(i, ""):
            wynik += 1
            print("✓ Poprawna!")
        else:
            print("✗ Błąd!")
    
    return wynik

def zapisz_wyniki(imie, nazwisko, wynik, k):
    # Format imie;nazwisko;wynik;liczba_pytan;data
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("wyniki.txt", "a", encoding="utf-8") as f:
        f.write(f"{imie};{nazwisko};{wynik};{k};{data}\n")

def main():
    print("Witaj w quizie!")
    imie = input("Podaj swoje imię: ")
    nazwisko = input("Podaj swoje nazwisko: ")

    baza = wczytaj_dane()
    if baza is None:
        print ("Nie można uruchomić quizu.")
        return
    
    wynik = uruchom_quiz(baza, k=15)

    print (f"\nTwój wynik: {wynik} / 15")
    zapisz_wyniki(imie, nazwisko, wynik, 15)
    print("Wynik zapisany. Dziękujemy za udział!")

if __name__ == "__main__":
    main()
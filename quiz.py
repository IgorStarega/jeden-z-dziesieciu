import random, os, datetime

def wczytaj_dane():
    # upewniamy się że pliki istnieją, jeśli nie to zwracamy None
    if not os.path.exists("pytania.txt") or not os.path.exists("odpowiedzi.txt"):
        print("Brak plików z pytaniami lub odpowiedziami.")
        return None, None
    pytania = []
    with open("pytania.txt", encoding="utf-8") as f:
        blok = []
        for line in f:
            line = line.strip()
            if line and not line.startswith("="):
                blok.append(line)
            elif len(blok) >= 6:
                pytania.append(blok[:6])
                blok = []
        if len(blok) >= 6: pytania.append(blok[:6])
    # wczytujemy które odpowiedzi są poprawne
    odpowiedzi = {}
    with open("odpowiedzi.txt", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                nr, lit = line.strip().split(":")
                odpowiedzi[int(nr)] = lit.strip()
    return pytania, odpowiedzi

def main():
    print("Witaj w quizie!")
    imie = input("Podaj imię: ").strip()
    nazwisko = input("Podaj nazwisko: ").strip()
    pytania, odpowiedzi = wczytaj_dane()
    if not pytania: return print("Nie można uruchomić quizu.")
    # losujemy kolejność pytań i bierzemy 15 (albo tyle ile jest)
    random.shuffle(pytania)
    k = min(15, len(pytania))
    wynik = 0
    for i, p in enumerate(pytania[:k], 1):
        print(f"\n{i}. {p[1]}")
        print(f"  A) {p[2]}   B) {p[3]}   C) {p[4]}   D) {p[5]}")
        odp = input("Wpisz odpowiedź (A/B/C/D): ").upper()
        # pętla dopóki ktoś nie wpisze A B C D
        while odp not in "ABCD":
            odp = input("Nieprawidłowa! Wpisz A/B/C/D: ").upper()
        if odp == odpowiedzi.get(p[0], ""):
            wynik += 1; print("Poprawna!")
        else:
            print(f"Błąd! Poprawna: {odpowiedzi.get(p[0], '?')}")
    print(f"\nTwój wynik: {wynik}/{k}")
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # dopisuje wynik do pliku, jesli plik jest pusty to dodaje naglówek
    with open("wyniki.txt", "a+", encoding="utf-8") as f:
        f.seek(0)
        if not f.read():
            f.write(f"{'Imię':<12} {'Nazwisko':<15} {'Wynik':<7} {'Razem':<7} {'Data':<20}\n")
            f.write("-" * 65 + "\n")
        f.write(f"{imie:<12} {nazwisko:<15} {wynik:<7} {k:<7} {data:<20}\n")
    print("Wynik zapisany. Dziękujemy!")

if __name__ == "__main__":
    main()

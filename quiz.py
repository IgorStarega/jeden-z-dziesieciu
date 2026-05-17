import random, os, datetime

def wczytaj_pytania():
    if not os.path.exists("pytania.txt"):
        print("Brak pliku 'pytania.txt'.")
        return None
    pytania = []
    try:
        with open("pytania.txt", encoding="utf-8") as f:
            blok = []
            for line in f:
                line = line.strip()
                if line and not line.startswith("="):
                    blok.append(line)
                elif len(blok) >= 6:
                    pytania.append(blok[:6])
                    blok = []
                elif len(blok) > 0:
                    print(f"Ostrzeżenie: pominięto niekompletny blok ({len(blok)} linii).")
                    blok = []
            if len(blok) >= 6:
                pytania.append(blok[:6])
            elif len(blok) > 0:
                print(f"Ostrzeżenie: pominięto niekompletny blok na końcu pliku ({len(blok)} linii).")
    except PermissionError:
        print("Błąd: Brak uprawnień do odczytu pliku 'pytania.txt'.")
        return None
    except Exception as e:
        print(f"Błąd czytania pytań: {e}")
        return None

    if not pytania:
        print("Plik z pytaniami jest pusty lub ma zły format.")
        return None
    return pytania

def wczytaj_odpowiedzi():
    if not os.path.exists("odpowiedzi.txt"):
        print("Brak pliku 'odpowiedzi.txt'.")
        return None
    odpowiedzi = {}
    try:
        with open("odpowiedzi.txt", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    nr, lit = line.strip().split(":", 1)
                    nr = nr.strip()
                    lit = lit.strip().upper()
                    if nr.isdigit() and lit in "ABCD":
                        odpowiedzi[int(nr)] = lit
                    elif nr.isdigit():
                        print(f"Ostrzeżenie: pominięto odpowiedź '{lit}' dla pytania {nr} (nie A/B/C/D).")
    except PermissionError:
        print("Błąd: Brak uprawnień do odczytu pliku 'odpowiedzi.txt'.")
        return None
    except Exception as e:
        print(f"Błąd czytania odpowiedzi: {e}")
        return None
    return odpowiedzi

def main():
    print("=" * 40)
    print("Witaj w quizie!")
    print("=" * 40)

    while True:
        try:
            imie = input("Podaj imię: ").strip()
            if imie:
                break
            print("Imię nie może być puste.")
        except EOFError:
            print("\nKoniec danych wejściowych.")
            return

    while True:
        try:
            nazwisko = input("Podaj nazwisko: ").strip()
            if nazwisko:
                break
            print("Nazwisko nie może być puste.")
        except EOFError:
            print("\nKoniec danych wejściowych.")
            return

    pytania = wczytaj_pytania()
    if not pytania:
        print("Nie można uruchomić quizu.")
        return

    odpowiedzi = wczytaj_odpowiedzi()
    if odpowiedzi is None:
        print("Nie można uruchomić quizu.")
        return

    n = len(pytania)
    print(f"\nDostępnych pytań: {n}")

    while True:
        try:
            k_str = input(f"Ile pytań losować (1-{n}): ").strip()
            if not k_str:
                print("Podaj liczbę.")
                continue
            if not k_str.isdigit():
                print("Podaj liczbę całkowitą.")
                continue
            k = int(k_str)
            if k < 1 or k > n:
                print(f"Podaj liczbę z zakresu 1-{n}.")
                continue
            break
        except EOFError:
            print("\nKoniec danych wejściowych.")
            return

    random.shuffle(pytania)
    wybrane = pytania[:k]
    print(f"\nQuiz ma {k} pytań. Powodzenia!")

    litery = ["A", "B", "C", "D"]
    wynik = 0

    for i, p in enumerate(wybrane, 1):
        nr_pytania = int(p[0])
        tresc = p[1]
        odp_orig = [p[2], p[3], p[4], p[5]]

        # losowa kolejność odpowiedzi
        indeksy = [0, 1, 2, 3]
        random.shuffle(indeksy)
        odp_nowe = [odp_orig[idx] for idx in indeksy]

        # znajdź nową poprawną odpowiedź
        poprawna_orig = odpowiedzi.get(nr_pytania, "")
        if poprawna_orig in "ABCD":
            idx_orig = ord(poprawna_orig) - ord("A")
            for j, idx in enumerate(indeksy):
                if idx == idx_orig:
                    poprawna_nowa = litery[j]
                    break
            else:
                poprawna_nowa = "?"
        else:
            poprawna_nowa = "?"

        print(f"\n{i}. {tresc}")
        print(f"  A) {odp_nowe[0]}   B) {odp_nowe[1]}   C) {odp_nowe[2]}   D) {odp_nowe[3]}")

        try:
            odp = input("Wpisz odpowiedź (A/B/C/D): ").strip().upper()
        except EOFError:
            print("\nKoniec danych wejściowych.")
            break

        while odp not in "ABCD":
            try:
                odp = input("Nieprawidłowa! Wpisz A/B/C/D: ").strip().upper()
            except EOFError:
                print("\nKoniec danych wejściowych.")
                break

        if odp not in "ABCD":
            break

        if odp == poprawna_nowa:
            wynik += 1
            print("Poprawna!")
        else:
            print(f"Błąd! Poprawna: {poprawna_nowa}")

    print(f"\nTwój wynik: {wynik}/{k}")
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("wyniki.txt", "a+", encoding="utf-8") as f:
            f.seek(0)
            if not f.read():
                f.write(f"{'Imię':<12} {'Nazwisko':<15} {'Wynik':<7} {'Razem':<7} {'Data':<20}\n")
                f.write("-" * 65 + "\n")
            f.write(f"{imie:<12} {nazwisko:<15} {wynik:<7} {k:<7} {data:<20}\n")
        print("Wynik zapisany. Dziękujemy!")
    except PermissionError:
        print("Błąd: Brak uprawnień do zapisu pliku 'wyniki.txt'.")
    except Exception as e:
        print(f"Błąd zapisu wyniku: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nQuiz przerwany. Do zobaczenia!")

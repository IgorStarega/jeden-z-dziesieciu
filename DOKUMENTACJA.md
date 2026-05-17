# Dokumentacja aplikacji Quiz

## Twórcy

| Rola | Imię i nazwisko | Zadanie |
|------|----------------|---------|
| Autor | Maciek R. | Przygotowanie pliku z pytaniami i odpowiedziami, testowanie aplikacji |
| Autor | Igor S. | Napisanie kodu aplikacji, obsługa błędów, dokumentacja |

**Projekt na informatykę — Technikum Informatyczne, 4. rok**

---

## 1. Opis aplikacji

Aplikacja **Quiz** to program konsolowy napisany w języku Python, który przeprowadza test wiedzy w formie pytań wielokrotnego wyboru. Program:

- losuje **k** pytań ze zbioru **n** dostępnych pytań (użytkownik podaje liczbę k),
- przy każdym pytaniu losuje **kolejność odpowiedzi** (A, B, C, D),
- pytania i odpowiedzi wczytywane są z pliku `pytania.txt`,
- poprawne odpowiedzi wczytywane są z pliku `odpowiedzi.txt`,
- wynik quizu wraz z imieniem i nazwiskiem użytkownika zapisywany jest do pliku `wyniki.txt`.

Aplikacja jest odporna na błędy użytkownika — waliduje wszystkie dane wejściowe i obsługuje nieoczekiwane sytuacje (puste dane, błędne znaki, przerwanie działania, brak plików).

---

## 2. Jak korzystać z aplikacji

### 2.1. Wymagania

- **Python** w wersji 3.6 lub nowszej
- System operacyjny: Windows, Linux lub macOS
- Pliki `pytania.txt` i `odpowiedzi.txt` muszą znajdować się w tym samym folderze co `quiz.py`

### 2.2. Uruchomienie

Otwórz wiersz poleceń (konsolę), przejdź do folderu z projektem i wpisz:

```
python quiz.py
```

### 2.3. Przebieg quizu

Po uruchomieniu aplikacja:

1. **Wyświetla powitanie**
2. **Pyta o imię** — należy wpisać imię i zatwierdzić Enterem (puste imię zostanie odrzucone)
3. **Pyta o nazwisko** — należy wpisać nazwisko i zatwierdzić Enterem (puste nazwisko zostanie odrzucone)
4. **Wyświetla liczbę dostępnych pytań** i pyta ile pytań losować — należy wpisać liczbę z zakresu 1–n
5. **Rozpoczyna quiz** — wyświetla pytania w losowej kolejności, każde z odpowiedziami w losowej kolejności
6. **Pyta o odpowiedź** — należy wpisać literę A, B, C lub D i zatwierdzić Enterem
   - Jeśli wpisze się coś innego, aplikacja poprosi o ponowne wpisanie
7. **Po każdym pytaniu** informuje czy odpowiedź była poprawna, czy błędna (i podaje poprawną odpowiedź)
8. **Na końcu** wyświetla wynik i zapisuje go do pliku `wyniki.txt`

### 2.4. Zakończenie

Quiz kończy się po odpowiedzi na wszystkie wylosowane pytania. Można też przerwać quiz skrótem **Ctrl+C** — aplikacja zakończy się elegancko bez błędu.

---

## 3. Jak działa aplikacja

### 3.1. Struktura plików

```
quiz/
├── quiz.py           # Główny plik aplikacji (kod programu)
├── pytania.txt       # Plik z pytaniami i odpowiedziami
├── odpowiedzi.txt    # Plik z poprawnymi odpowiedziami
└── wyniki.txt        # Plik z wynikami (tworzony automatycznie)
```

### 3.2. Plik `pytania.txt` — pytania i odpowiedzi

Każde pytanie zajmuje **6 linii** oddzielonych separatorem (znaki `=`):

```
<numer pytania>
<treść pytania>
<odpowiedź A>
<odpowiedź B>
<odpowiedź C>
<odpowiedź D>
<separator =====>
```

**Przykład:**
```
1
Jak nazywa się stolica Francji?
Paryż
Londyn
Berlin
Madryt
======
```

Plik zawiera 15 pytań z różnych dziedzin wiedzy (geografia, matematyka, literatura, nauka, historia).

### 3.3. Plik `odpowiedzi.txt` — poprawne odpowiedzi

Każda linia zawiera numer pytania i literę poprawnej odpowiedzi:

```
1: A
2: C
3: B
```

Litera odnosi się do **oryginalnej kolejności** odpowiedzi w pliku `pytania.txt`. Program sam przelicza poprawną odpowiedź po losowym pomieszaniu odpowiedzi.

### 3.4. Plik `wyniki.txt` — wyniki użytkowników

Tworzony automatycznie przy pierwszym zapisie. Zawiera nagłówek i wpisy w formacie:

```
Imię         Nazwisko        Wynik   Razem   Data
-----------------------------------------------------------------
Jan          Kowalski        4       5       2026-05-17 14:30:00
```

### 3.5. Algorytm działania

1. **Wczytanie danych** — program odczytuje `pytania.txt` (parsuje bloki po 6 linii) i `odpowiedzi.txt` (tworzy słownik numer→litera)
2. **Wybór liczby pytań** — użytkownik podaje k (1–n), program sprawdza poprawność
3. **Losowanie pytań** — program miesza listę pytań (`random.shuffle`) i wybiera pierwszych k
4. **Dla każdego pytania:**
   - Pobiera 4 odpowiedzi z pliku
   - Miesza je losowo (`random.shuffle`)
   - Znajduje nową pozycję poprawnej odpowiedzi (na podstawie litery z `odpowiedzi.txt`)
   - Wyświetla pytanie z pomieszonymi odpowiedziami
   - Pobiera i waliduje odpowiedź użytkownika
   - Porównuje z poprawną odpowiedzią
5. **Zapis wyniku** — wynik z imieniem, nazwiskiem i datą dopisywany jest do `wyniki.txt`

---

## 4. Budowa aplikacji (kod źródłowy)

### 4.1. Funkcje

#### `wczytaj_pytania()`

Wczytuje pytania z pliku `pytania.txt`. Zwraca listę pytań (każde pytanie to lista 6 elementów) lub `None` w przypadku błędu.

**Obsługiwane błędy:**
- brak pliku
- brak uprawnień do odczytu
- pusty plik lub zły format
- niekompletne bloki (ostrzeżenie)

#### `wczytaj_odpowiedzi()`

Wczytuje poprawne odpowiedzi z pliku `odpowiedzi.txt`. Zwraca słownik `{numer_pytania: litera}` lub `None` w przypadku błędu.

**Obsługiwane błędy:**
- brak pliku
- brak uprawnień do odczytu
- nieprawidłowy format linii (ostrzeżenie)

#### `main()`

Główna funkcja programu. Steruje całym przepływem quizu:

1. Pobiera imię i nazwisko (z walidacją)
2. Wczytuje pytania i odpowiedzi
3. Pyta o liczbę pytań do losowania (z walidacją)
4. Losuje pytania i kolejność odpowiedzi
5. Przeprowadza quiz
6. Zapisuje wynik

### 4.2. Zabezpieczenia przed błędami

| Błąd użytkownika | Jak aplikacja reaguje |
|------------------|----------------------|
| Puste imię/nazwisko | Ponawia pytanie do czasu podania wartości |
| Nieprawidłowa liczba pytań | Ponawia pytanie do czasu podania liczby z zakresu |
| Odpowiedź inna niż A/B/C/D | Ponawia pytanie do czasu podania prawidłowej litery |
| Małe litery (a/b/c/d) | Automatycznie zamienia na wielkie |
| Ctrl+C podczas quizu | Kończy działanie z komunikatem pożegnania |
| Zamknięcie wejścia (EOF) | Kończy działanie z komunikatem |
| Brak pliku `pytania.txt` | Wyświetla błąd i kończy działanie |
| Brak pliku `odpowiedzi.txt` | Wyświetla błąd i kończy działanie |
| Brak uprawnień do plików | Wyświetla błąd i kończy działanie |
| Niekompletny blok pytań | Wyświetla ostrzeżenie i pomija blok |
| Nieprawidłowa litera w odpowiedziach | Wyświetla ostrzeżenie i pomija wpis |

### 4.3. Użyte biblioteki

Aplikacja korzysta wyłącznie z **bibliotek standardowych Pythona**:

| Biblioteka | Zastosowanie |
|------------|-------------|
| `random` | Losowanie kolejności pytań i odpowiedzi |
| `os` | Sprawdzanie istnienia plików |
| `datetime` | Pobieranie aktualnej daty i czasu |

---

## 5. Przykład działania

```
========================================
Witaj w quizie!
========================================
Podaj imię: Jan
Podaj nazwisko: Kowalski

Dostępnych pytań: 15
Ile pytań losować (1-15): 5

Quiz ma 5 pytań. Powodzenia!

1. Jak nazywa się stolica Francji?
  A) Londyn   B) Madryt   C) Paryż   D) Berlin
Wpisz odpowiedź (A/B/C/D): C
Poprawna!

2. Ile wynosi 2+2?
  A) 4   B) 6   C) 3   D) 5
Wpisz odpowiedź (A/B/C/D): A
Poprawna!

3. Kto napisał "Pan Tadeusz"?
  A) Juliusz Słowacki   B) Adam Mickiewicz   C) Henryk Sienkiewicz   D) Bolesław Prus
Wpisz odpowiedź (A/B/C/D): B
Poprawna!

4. Jaki jest największy ocean na Ziemi?
  A) Ocean Spokojny   B) Ocean Atlantycki   C) Ocean Indyjski   D) Ocean Arktyczny
Wpisz odpowiedź (A/B/C/D): X
Nieprawidłowa! Wpisz A/B/C/D: A
Poprawna!

5. Ile kontynentów jest na Ziemi?
  A) 6   B) 5   C) 8   D) 7
Wpisz odpowiedź (A/B/C/D): D
Poprawna!

Twój wynik: 5/5
Wynik zapisany. Dziękujemy!
```

---

## 6. Rozwiązywanie problemów

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `Brak pliku 'pytania.txt'` | Plik nie istnieje w folderze | Skopiuj plik `pytania.txt` do folderu z `quiz.py` |
| `Brak pliku 'odpowiedzi.txt'` | Plik nie istnieje w folderze | Skopiuj plik `odpowiedzi.txt` do folderu z `quiz.py` |
| `Plik z pytaniami jest pusty` | Plik jest pusty lub ma zły format | Sprawdź czy każde pytanie ma 6 linii i separator `=` |
| `Błąd: Brak uprawnień` | Brak praw do odczytu/zapisu plików | Uruchom jako administrator lub sprawdź uprawnienia |
| Polskie znaki nie działają | Plik nie jest w UTF-8 | Zapisz pliki w kodowaniu UTF-8 |
| `python` nie działa | Python nie jest w PATH | Użyj `py quiz.py` lub dodaj Python do PATH |

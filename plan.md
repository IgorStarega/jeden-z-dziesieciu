# Plan projektu: Quiz - aplikacja do testowania wiedzy

## Informacje o projekcie
- **Nazwa:** Quiz
- **Przeznaczenie:** Aplikacja do przeprowadzania testów wiedzy
- **Poziom:** Technikum informatyczne klasa 4

## Podział zadań dla 2 osób

### Osoba 1: Żul
1. **Przygotowanie pliku pytania.txt**
   - Zebrać minimum 10 pytań testowych
   - Każde pytanie w nowej linii
   - Pytania mają być z różnych tematów

2. **Przygotowanie pliku odpowiedzi.txt**
   - Dla każdego pytania: 4 możliwe odpowiedzi
   - Pierwsza odpowiedź w każdej czwórce musi być POPRAWNA
   - Format: odp1, odp2, odp3, odp4 (każda w nowej linii)

3. **Testowanie aplikacji**
   - Sprawdzić czy import plików działa
   - Przetestować losowanie pytań

### Osoba 2: Wilson
1. **Napisanie kodu quiz.py**
   - Funkcja wczytaj_pytania() - wczytywanie pytań z pliku
   - Funkcja wczytaj_odpowiedzi() - wczytywanie odpowiedzi
   - Funkcja losuj_pytania(k, n) - losowanie k pytań z n
   - Funkcja sprawdz_odpowiedz() - sprawdzenie poprawności
   - Funkcja zapisz_wynik() - zapis do pliku wyniki.txt

2. **Obsługa błędów**
   - Sprawdzenie czy plik istnieje
   - Walidacja danych wejściowych (liczby, litery)
   - Obsługa pustych pól

3. **Dokumentacja - dokumentacja.md**
   - Jak uruchomić aplikację
   - Opis działania
   - Format plików wejściowych

## Wspólne ustalenia
- Kod ma być prosty i czytelny
- Używać podstawowych struktur (listy, funkcje)
- Brak zaawansowanych bibliotek
- Komunikaty w języku polskim

## Harmonogram
- Dzień 1: Osoba 1 tworzy pliki txt
- Dzień 2: Osoba 2 pisze kod
- Dzień 3: Testowanie i poprawki
- Dzień 4: Dokumentacja

## Wymagania techniczne
- Python 3.x
- Pliki w formacie UTF-8
- System operacyjny: Windows/Linux
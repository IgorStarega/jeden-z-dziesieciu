# Schemat struktury plików projektu Quiz

## Struktura katalogów

```
projekt-quiz/
├── schemat.md          # Dokumentacja projektu
├── quiz.py             # Aplikacja quiz (Python)
├── pytania.txt        # Baza pytań i odpowiedzi
├── odpowiedzi.txt     # Poprawne odpowiedzi
└── wyniki.txt         # Wyniki rozwiązań
```

## Opis plików

| Plik | Opis |
|------|------|
| `quiz.py` | Główna aplikacja - skrypt Python uruchamiany z konsoli |
| `pytania.txt` | Pytania i możliwe odpowiedzi (format: tekstowy) |
| `odpowiedzi.txt` | Poprawne odpowiedzi do pytań |
| `wyniki.txt` | Wyniki - imię, nazwisko, wynik, data |
| `schemat.md` | Dokumentacja techniczna |

## Format pliku pytania.txt

Każde pytanie składa się z wielu linii:
```
NUMER_PYTANIA
Treść pytania?
Odpowiedź A
Odpowiedź B
Odpowiedź C
Odpowiedź D
===
```

## Format pliku odpowiedzi.txt

```
NUMER_PYTANIA: POPRAWNA_ODPOWIEDŹ
```

Przykład:
```
1: A
2: C
3: B
```

## Format pliku wyniki.txt

```
Imię;Nazwisko;Wynik;Liczba pytań;Data
```

Przykład:
```
Jan;Kowalski;7;10;2026-04-27 14:30:00
Anna;Nowak;9;10;2026-04-27 15:00:00
```
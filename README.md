# TextMixer – Aplikacja Django

## Projekt zawiera dwie aplikacje webowe napisane w Django:

1. **Miksowanie tekstu** – wgrany plik tekstowy zostaje przetworzony tak, aby każde słowo miało pomieszane litery w środku, ale pierwsza i ostatnia litera pozostały na miejscu.  
2. **Walidator PESEL** – sprawdza poprawność numeru PESEL, a jeśli jest poprawny, wyświetla datę urodzenia i płeć.

---


---

## Instalacja


# 1. Sklonuj repozytorium (lub pobierz ZIP)
  ```sh
  git clone https://github.com/Tobajos/textmixer.git
  ```

  ```sh
  cd textmixer
  ```


# 2. (Opcjonalnie) Utwórz i aktywuj wirtualne środowisko
  ```sh
  python -m venv venv
  ```

  ```sh
  venv\Scripts\activate        # Windows
  ```
# lub

  ```sh
  source venv/bin/activate     # macOS/Linux
  ```


# 3. Zainstaluj wymagane pakiety
  ```sh
  pip install -r requirements.txt
  ```


# 4. Uruchom serwer developerski
  ```sh
  python manage.py runserver
  ```


Użycie

Po uruchomieniu serwera przejdź do:

http://127.0.0.1:8000/

Zobaczysz stronę główną z dwoma kafelkami:

    Miksowanie tekstu → /text/

    Walidacja PESEL → /pesel/

Funkcjonalności
Miksowanie tekstu

    Prześlij plik .txt z tekstem

    Każde słowo zostanie przetasowane (z wyjątkiem pierwszej i ostatniej litery)

    Wynik zostanie wyświetlony na stronie

Walidator PESEL

    Wprowadź numer PESEL

    Aplikacja sprawdza poprawność na podstawie sumy kontrolnej

    Wyświetla datę urodzenia i płeć

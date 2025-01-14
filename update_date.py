import os
import time
from datetime import datetime
from subprocess import run

def update_date_file():
    # Ścieżka do pliku
    date_file = "date.txt"

    # Pobierz aktualną datę i czas
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Zapisz datę do pliku
    with open(date_file, "w") as file:
        file.write(f"Aktualna data i czas: {current_time}\n")

    print(f"Plik {date_file} został zaktualizowany.")

def git_commit_and_push():
    # Wykonaj commit i push
    run(["git", "add", "date.txt"], check=True)
    run(["git", "commit", "-m", "Automatyczna aktualizacja daty"], check=True)
    run(["git", "push"], check=True)
    print("Zaktualizowany plik został wysłany na GitHub.")

def main():
    try:
        update_date_file()
        git_commit_and_push()
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()

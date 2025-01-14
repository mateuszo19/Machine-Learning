import os
from datetime import datetime
from subprocess import run

def update_date_file():
    # Ścieżka do pliku
    folder_path = "data/raw"
    date_file = os.path.join(folder_path, "date.csv")

    # Upewnij się, że folder istnieje
    os.makedirs(folder_path, exist_ok=True)

    # Pobierz aktualną datę i czas
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Sprawdź, czy plik istnieje, aby dodać nagłówki tylko raz
    file_exists = os.path.isfile(date_file)

    # Zapisz datę do pliku
    with open(date_file, "a") as file:
        if not file_exists:
            file.write("Timestamp\n")  # Nagłówek CSV
        file.write(f"{current_time}\n")

    print(f"Plik {date_file} został zaktualizowany.")

def git_commit_and_push():
    # Ścieżka do pliku
    date_file = "data/raw/date.csv"

    # Wykonaj commit i push
    run(["git", "add", date_file], check=True)
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

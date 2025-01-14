# -*- coding: utf-8 -*-

import os
from datetime import datetime
from subprocess import call

def update_date_file():
    # Ścieżka do pliku
    folder_path = "data/raw"
    date_file = os.path.join(folder_path, "date.csv")

    # Upewnij się, że folder istnieje
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Pobierz aktualną datę i czas
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Sprawdź, czy plik istnieje, aby dodać nagłówki tylko raz
    file_exists = os.path.isfile(date_file)

    # Zapisz datę do pliku
    with open(date_file, "a") as file:
        if not file_exists:
            file.write("Timestamp\n")  # Nagłówek CSV
        file.write("{}\n".format(current_time))

    print("Plik {} został zaktualizowany.".format(date_file))

def git_commit_and_push():
    # Ścieżka do pliku
    date_file = "data/raw/date.csv"

    # Wykonaj commit i push
    call(["git", "add", date_file])
    call(["git", "commit", "-m", "Train model"])
    call(["git", "push"])
    print("Zaktualizowany plik został wysłany na GitHub.")

def main():
    try:
        update_date_file()
        git_commit_and_push()
    except Exception as e:
        print("Wystąpił błąd: {}".format(e))

if __name__ == "__main__":
    main()

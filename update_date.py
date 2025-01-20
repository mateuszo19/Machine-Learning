# -*- coding: utf-8 -*-

import os
from datetime import datetime
from subprocess import call

def remove_git_lock():
    """
    Usuwa plik .git/index.lock, jeśli istnieje, aby zapobiec problemom z blokadą repozytorium.
    """
    git_lock_file = "/root/gitapp/.git/index.lock"

    if os.path.exists(git_lock_file):
        try:
            os.remove(git_lock_file)
            print("🗑 Usunięto plik blokady Git: {}".format(git_lock_file))
        except Exception as e:
            print("❌ Błąd podczas usuwania pliku blokady Git: {}".format(e))

def update_date_file():
    """
    Funkcja dodaje pojedynczy rekord do pliku CSV.
    """
    folder_path = "data/raw"
    date_file = os.path.join(folder_path, "date.csv")

    # Tworzenie folderu, jeśli nie istnieje
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Sprawdzenie, czy plik już istnieje
    file_exists = os.path.isfile(date_file)

    # Dodanie nowego rekordu do CSV
    with open(date_file, "a") as file:
        if not file_exists:
            file.write("Timestamp\n")  # Dodanie nagłówka tylko jeśli plik nie istniał
        file.write("{}\n".format(current_time))

    print("✅ Plik {} został zaktualizowany.".format(date_file))

def git_commit_and_push():
    """
    Funkcja dodaje plik CSV do Git, wykonuje commit i push.
    """
    os.chdir("/root/gitapp")  # Przejście do katalogu repozytorium
    git_path = "/usr/bin/git"
    date_file = "data/raw/date.csv"

    try:
        # Usunięcie blokady Git przed operacją
        remove_git_lock()

        call([git_path, "add", date_file])
        call([git_path, "commit", "-m", "Automatyczna aktualizacja daty"])
        call([git_path, "push"])
        print("✅ Zaktualizowany plik został wysłany na GitHub.")
    except Exception as e:
        print("❌ Wystąpił błąd podczas operacji Git: {}".format(e))

def main():
    """
    Główna funkcja uruchamiająca aktualizację pliku i synchronizację z Git.
    """
    try:
        update_date_file()
        git_commit_and_push()
    except Exception as e:
        print("❌ Wystąpił błąd: {}".format(e))

if __name__ == "__main__":
    main()

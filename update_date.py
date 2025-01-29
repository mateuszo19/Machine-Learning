# -*- coding: utf-8 -*-

import os
import random
from subprocess import call

def remove_git_lock():
   
    git_lock_file = "/root/gitapp/.git/index.lock"

    if os.path.exists(git_lock_file):
        try:
            os.remove(git_lock_file)
            print("🗑 Usunięto plik blokady Git: {}".format(git_lock_file))
        except Exception as e:
            print("❌ Błąd podczas usuwania pliku blokady Git: {}".format(str(e)))

def generate_fake_ml_data():
    
    folder_path = "data/raw"
    data_file = os.path.join(folder_path, "ml_data.csv")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_exists = os.path.isfile(data_file)

    with open(data_file, "a") as file:
        if not file_exists:
            file.write("Feature1,Feature2,Feature3,Label\n") 

        # Generowanie 10 losowych rekordów
        for _ in range(10):
            x = round(random.uniform(-1, 1), 2)
            y = round(random.uniform(-1, 1), 2)
            z = round(random.uniform(-1, 1), 2)
            label = random.choice([0, 1]) 
            file.write("{},{},{},{}\n".format(x, y, z, label))

    return data_file

def git_commit_and_push(file_path):
    """
    Funkcja dodaje plik CSV do Git, wykonuje commit i push.
    """
    os.chdir("/root/gitapp")
    git_path = "/usr/bin/git"

    try:
        remove_git_lock()

        call([git_path, "add", file_path])
        call([git_path, "commit", "-m", "Automatyczna aktualizacja danych ML"])
        call([git_path, "push"])
        print("✅ Zaktualizowany plik został wysłany na GitHub.")
    except Exception as e:
        print("❌ Wystąpił błąd podczas operacji Git: {}".format(str(e)))

def main():

    try:
        file_path = generate_fake_ml_data()
        git_commit_and_push(file_path)
    except Exception as e:
        print("❌ Wystąpił błąd: {}".format(str(e)))

if __name__ == "__main__":
    main()

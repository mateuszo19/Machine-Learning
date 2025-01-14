# -*- coding: utf-8 -*-

import os
import time
from datetime import datetime
from subprocess import call

def update_date_file():
    folder_path = "data/raw"
    date_file = os.path.join(folder_path, "date.csv")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.isfile(date_file)

    with open(date_file, "a") as file:
        if not file_exists:
            file.write("Timestamp\n")  # Nagłówek CSV
        file.write("{}\n".format(current_time))

    print("Plik {} został zaktualizowany.".format(date_file))

def git_commit_and_push():
    os.chdir("/root/gitapp")
    git_path = "/usr/bin/git"
    date_file = "data/raw/date.csv"

    call([git_path, "add", date_file])
    call([git_path, "commit", "-m", "Model training"])
    call([git_path, "push"])
    print("Zaktualizowany plik został wysłany na GitHub.")

def main():
    while True:
        try:
            update_date_file()
            git_commit_and_push()
        except Exception as e:
            print("Wystąpił błąd: {}".format(e))
        
        # Oczekuj losową ilość czasu przed kolejnym wykonaniem (np. 3-6 godzin)
        wait_time = 3 * 3600 + (time.time() % 10800)  # 3-6 godzin (w sekundach)
        print("Czekam przez {} sekund.".format(wait_time))
        time.sleep(wait_time)

if __name__ == "__main__":
    main()

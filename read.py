#!/usr/bin/env python3
import subprocess
import os


files = subprocess.run(['ls'], capture_output=True, text=True)
files = files.stdout.splitlines()


files_length = len(files)
    

while True:
    try:
        page = int(input("What page would you like to start on: "))
        if  0<=page<=files_length:
            break
        else:
            print("Not a page")
            continue

    except ValueError:
        print("You did not type a number")
        continue



while page <= files_length:

    subprocess.run(['termvisage', files[page]])
    print(f"Pg. {page}")
    user_input = input("Press q to quit. Press Enter to Continue: ")
    if user_input == "q":
        break
    else:
        page += 1
        continue

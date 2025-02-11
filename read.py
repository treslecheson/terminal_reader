#!/usr/bin/env python3
import subprocess
from InquirerPy import prompt


files = subprocess.run(['ls'], capture_output=True, text=True)
files2 = files.stdout.splitlines()



files_length = len(files2)
    


starting_question = [
    {
        "type": "list",
        "message": "What page would you like to start on?",
        "choices": files2,
    },
]

result = prompt(starting_question)
choice = result[0]

start = 0
for images in files2:
    start += 1
    if images == choice:
        break

page = start
while page <= files_length:

    subprocess.run(['termvisage', files2[page]])
    continue_quit_question = [
        {
            "type": "list",
            "message": f"Pg. {page}",
            "choices": ["Continue", "Quit"],
        },
    ]
    continue_result = prompt(continue_quit_question)
    continue_choice = continue_result[0]
    if continue_choice == "Continue":
        page += 1
        continue
    else:
        break

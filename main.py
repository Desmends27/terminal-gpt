#!/usr/bin/python3
"""This is where the magic happens """
from packages.chat import gpt,save_to_json_file
from packages.chat_console import console
from sys import argv
import os

if (len(argv) <= 1):
    gpt()
else:
    for arg in range(1,len(argv)):
        if argv[arg].startswith("--"):
            match argv[arg][2:]:
                case "loop":
                    console().cmdloop()
                case "clear":
                    try:
                        save_to_json_file([])
                    except Exception as e:
                        print(e)
                case _:
                    print("Invalid option")
                    break
        
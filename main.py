#!/usr/bin/python3
"""This is where the magic happens """
from packages.chat import gpt,save_to_json_file
from packages.chat_console import console
from sys import argv
import os
import sys

def main():
    argv = sys.argv
    input_sentence = None

    for arg in range(1, len(argv)):
        if argv[arg].startswith("--"):
            option = argv[arg][2:]
            if option == "loop":
                console().cmdloop()
            elif option == "clear":
                try:
                    save_to_json_file([])
                except Exception as e:
                    print(e)
            else:
                print("Invalid option")
                break
        else:
            # Treat the first argument without "--" as the input sentence
            input_sentence = " ".join(argv[arg:])
            break

    if input_sentence is not None:
        gpt(input_sentence)

if __name__ == "__main__":
    main()

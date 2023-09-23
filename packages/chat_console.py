#!/usr/bin/python3
"""Console mode for gpt"""
import cmd
from packages.chat import gpt
from packages.chat import save_to_json_file

class console(cmd.Cmd):
    intro = " Type prompt and wait for response "
    prompt = "gpt "

    def default(self, arg):
        """If empyt line is pressesd"""
        gpt(arg)
    
    def do_clear(self, arg):
        """Clear the message history"""
        save_to_json_file([])
        
    def do_exit(self, arg):
        """Exits the console"""
        print('Thank you for using chat')
        return True
    
    def do_EOF(self, arg):
        """Ctrl + C"""
        print('Thank you for using chat')
        return True

    

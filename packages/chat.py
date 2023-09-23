#!/usr/bin/python3
"""All main functions go here"""

import json
import os
import openai

try:
    with open(file="password.txt", mode='r') as f:
        api_key = f.read()
except Exception as e:
    print(e)



openai.api_key=api_key

def save_to_json_file(my_obj):
    """Add messages to json file"""
    with open("messages.json",mode='w', encoding='utf-8') as fp:
        json.dump(obj=my_obj, fp=fp)
def load_from_json_file():
    """Load data from messages.json"""
    with open("messages.json", mode='r', encoding='utf-8') as fp:
        return json.load(fp=fp)
    
def save_load(obj) -> list:
    """Save and load from json file
        Returns: a list of dictionaries with prompts"""
    try:
        message_history = load_from_json_file()
    except:
        message_history = []
    message_history.append(obj)
    save_to_json_file(message_history)
    return message_history
    
def gpt(user_input = None):
    """Waits for user input and then prompts gpt for answer
    """
    if user_input == None:
        user_input = input("gpt ")
    message_history = save_load({"role":"user", "content":user_input})
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history = save_load({"role":"assistant", "content": reply_content})

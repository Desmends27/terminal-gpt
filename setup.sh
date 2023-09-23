#!/usr/bin/bash

# Install python3 and pip
sudo apt install -y python3
sudo apt install -y python3-pip

# Install openai
pip install openai

# User input for API key
read -p "Enter API key: " api_key

echo "$api_key" > password.txt

# Update the main.py permissions
chmod +x main.py

# Move the terminal-gpt directory to ~/bin/
sudo mv ../terminal-gpt ~/bin/

# Create symbolic link for main
ln -s ~/bin/terminal-gpt/main.py ~/bin/gpt

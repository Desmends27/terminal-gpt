#!/bin/bash

# Install Python 3 and pip
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install the OpenAI Python package using pip
pip3 install openai

# Prompt the user for the API key
read -p "Enter API key: " api_key

# Define the installation directory
install_dir="/usr/local/bin/terminal_gpt"

# Create the installation directory
sudo mkdir -p "$install_dir"

# Create a file called password.txt in the installation directory and store the API key
echo "$api_key" | sudo tee "$install_dir/password.txt" > /dev/null

# Copy the necessary files to the installation directory
sudo cp -r ./{README.md,__pycache__,main.py,packages} "$install_dir"

# Create a symbolic link to main.py in /usr/local/bin/ with the name 'gpt'
sudo ln -s "$install_dir/main.py" "/usr/local/bin/gpt"

# Change permissions to make main.py executable
sudo chmod +x "$install_dir/main.py"

# Display a message indicating successful installation
echo "Terminal gpt has been installed."
echo "You can now run 'gpt' from anywhere in the terminal."

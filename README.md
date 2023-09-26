## Terminal Project


Terminal GPT is a command-line tool that leverages OpenAI's GPT (Generative Pre-trained Transformer) to generate text based on user input. This tool allows you to interact with GPT through your terminal, making it easy to generate text for various applications.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Generating Text](#generating-text)
  - [Additional Options](#additional-options)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

#installation


1. Clone this repository to your local machine:
 ```
   https://github.com/Desmends27/terminal-gpt.git
```
2. Navigate to the project directory
     ```
     cd terminal-gpt
    ```
3. Run the installation script:
        ```
           ./install.sh
       ```
Follow the prompts to install Python 3, pip, and the necessary dependencies. You'll also be asked to enter your API key for OpenAI, which will be securely stored for future use.

(#usage
You can generate text using Terminal GPT by simply typing:
  ```
    gpt Your input sentence here
  ```
#additional-options
Terminal GPT supports the following additional options:

--loop: Start an interactive console session where you can input multiple sentences and receive responses interactively. Type exit to exit the console session.
```
  gpt --loop
```

--clear: Clear the conversation history and start fresh.
```
gpt --clear
```
Note: Clearing the conversation history will remove all previous inputs and outputs.


#contributing
Contributions to Terminal GPT are welcome! Feel free to open issues, submit pull requests, or provide feedback to help improve this tool.


#acknowledgments
This project uses OpenAI's GPT-3 model. Visit OpenAI for more information.

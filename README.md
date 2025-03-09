# ScreenGPT

ScreenGPT is a project that leverages LLM to understand the screen content. 
It provides response based on the user defined prompts and the screen content.
You need an OpenAI compatible API key to use this software. 

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview
ScreenGPT uses state-of-the-art AI to analyze and render screen content dynamically. It offers a flexible and extensible framework for integrating AI-powered screen interactions into your projects.

## Features
- Real-time screen analysis and interaction
- Customizable LLM system prompts and user prompts
- Support Openai compatible API
- Extensible design for future enhancements

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Alchemist-Aloha/screengpt.git
    ```
2. Generate a python virtual environment (optional but recommended):
    ```sh
    # pip
    python -m venv .venv
    # or uv
    uv venv
    # Activate the virtual environment
    .venv\Scripts\activate
    ```
3. Install the packages:
    ```sh
    # pip
    pip install -e screengpt
    # or uv
    uv pip install -e screengpt
    ```

## Usage
### Start the application with:

```sh
python -m screengpt
```
- Input your OpenAI compatible API key when prompted. 
- Default setting is Openrouter Base URL with free google/gemini-2.0-flash-exp:free model. 
You can obtain your API key from [OpenRouter](https://openrouter.ai/settings/keys).
- Modify the system prompt and user prompt as you like. The default one is for game copilot.
- Depend on your use case, you can change the hotkey to your desired key.
- Hit "Apply Settings" to start the application. The settings will be saved in config.ini so you don't have to reinput those agin next time.
- Press the hotkey (default is Ctrl+alt+e) to capture the screenshot and the response will be shown both on the screen and the terminal.

## License
This project is licensed under the MIT License. 
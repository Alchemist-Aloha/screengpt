# ScreenGPT

ScreenGPT leverages large language models (LLMs) to analyze and understand screen content. It generates responses based on user-defined prompts and the visual input from your screen. To use this software, you will need an OpenAI-compatible API key.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview
ScreenGPT utilizes advanced LLMs to interpret screen content and provides a flexible, extensible framework for integrating AI-powered screen interactions into your workflow.

## Features
- Real-time screen analysis.
- Customizable system and user prompts.
- Graphical user interface (GUI) for easy configuration.
- Support for OpenAI-compatible APIs.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Alchemist-Aloha/screengpt.git
    ```
2. Create a Python virtual environment (optional but recommended):
    ```sh
    # Using pip:
    python -m venv .venv

    # Or using uv:
    uv venv

    # Activate the virtual environment:
    .venv\Scripts\activate
    ```
3. Install the required packages:
    ```sh
    # Using pip:
    pip install -e screengpt

    # Or using uv:
    uv pip install -e screengpt
    ```

## Usage
### Start the Application:
```sh
python -m screengpt
```
or use provided Windows X64 executable. 

- Enter your OpenAI-compatible API key when prompted.
- The default settings use the OpenRouter base URL with the free model: google/gemini-2.0-flash-exp:free.
- Obtain your API key from [OpenRouter](https://openrouter.ai/settings/keys).
- Modify the system and user prompts as needed; the default prompt is designed for game copilot assistance.
- Adjust the hotkey to your preference.
- Click "Apply Settings" to start the application. The settings will be saved in config.ini, so you won’t need to re-enter them next time.
- Press the hotkey (default: Ctrl+Alt+E) to capture a screenshot; the response will be displayed both on screen and in the terminal.

## License
This project is licensed under the MIT License.
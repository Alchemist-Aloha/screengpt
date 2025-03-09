from setuptools import setup

setup(
    name="screengpt",
    version="0.1",
    description="Screenshot Analyzer powered by LLMs",
    author="Alchemist Aloha",
    py_modules=["main", "ui"],
    install_requires=[
        "Pillow",
        "openai",
        "pyautogui",
        "keyboard"
    ],
    entry_points={
        "console_scripts": [
            # Ensure main.py defines a main() function.
            "screengpt = main:main"
        ]
    }
)
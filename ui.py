# ui.py
import tkinter as tk
from tkinter import ttk, messagebox

class ScreenshotAnalyzerUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Screenshot Analyzer")

        # Variables for settings
        self.api_key = tk.StringVar()
        self.base_url = tk.StringVar(value="https://openrouter.ai/api/v1")
        self.model = tk.StringVar(value="google/gemini-2.0-flash-exp:free")
        self.system_prompt = tk.StringVar(value="You are an expert game advisor. Analyze the provided screenshot of the game. Based on the current game state, provide concise and actionable guidance to the player. Focus on strategic advice, potential moves, and helpful hints. Keep the response short and directly relevant to the screenshot's content.")
        self.hotkey = tk.StringVar(value="ctrl+alt+e")

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # API Key
        ttk.Label(self.root, text="API Key:").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.api_key, show="*").grid(row=0, column=1, sticky="we")

        # Base URL
        ttk.Label(self.root, text="Base URL:").grid(row=1, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.base_url).grid(row=1, column=1, sticky="we")

        # Model
        ttk.Label(self.root, text="Model:").grid(row=2, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.model).grid(row=2, column=1, sticky="we")

        # System Prompt
        ttk.Label(self.root, text="System Prompt:").grid(row=3, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.system_prompt).grid(row=3, column=1, sticky="we")

        # Hotkey
        ttk.Label(self.root, text="Hotkey:").grid(row=4, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.hotkey).grid(row=4, column=1, sticky="we")

        # Apply settings button
        ttk.Button(self.root, text="Apply Settings", command=self.controller.apply_settings).grid(row=5, column=0, columnspan=2, pady=10)

        self.root.columnconfigure(1, weight=1)

    def get_settings(self):
        return {
            "api_key": self.api_key.get(),
            "base_url": self.base_url.get(),
            "model": self.model.get(),
            "system_prompt": self.system_prompt.get(),
            "hotkey": self.hotkey.get(),
        }

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, message):
        messagebox.showerror("Error", message)
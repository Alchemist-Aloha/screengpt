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
        self.system_prompt = "You are an expert game advisor. Analyze the provided screenshot of the game. Based on the current game state, provide concise and actionable guidance to the player. Focus on strategic advice, potential moves, and helpful hints. Keep the response short and directly relevant to the screenshot's content."
        self.user_prompt = "Analyze this screenshot and provide game guidance."
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
        prompt_frame = ttk.Frame(self.root)
        prompt_frame.grid(row=3, column=1, sticky="we")
        self.system_prompt_text = tk.Text(prompt_frame, wrap="word", height=5)
        self.system_prompt_text.insert("1.0", self.system_prompt)  # Set default value
        self.system_prompt_text.pack(side="left", fill="both", expand=True)
        prompt_scrollbar = ttk.Scrollbar(prompt_frame, orient="vertical", command=self.system_prompt_text.yview)
        prompt_scrollbar.pack(side="right", fill="y")
        self.system_prompt_text.config(yscrollcommand=prompt_scrollbar.set)

        # User Prompt
        ttk.Label(self.root, text="User Prompt:").grid(row=4, column=0, sticky="w")
        user_prompt_frame = ttk.Frame(self.root)
        user_prompt_frame.grid(row=4, column=1, sticky="we")
        self.user_prompt_text = tk.Text(user_prompt_frame, wrap="word", height=5)
        self.user_prompt_text.insert("1.0", self.user_prompt)  # Set default value
        self.user_prompt_text.pack(side="left", fill="both", expand=True)
        user_prompt_scrollbar = ttk.Scrollbar(user_prompt_frame, orient="vertical", command=self.user_prompt_text.yview)
        user_prompt_scrollbar.pack(side="right", fill="y")
        self.user_prompt_text.config(yscrollcommand=user_prompt_scrollbar.set)

        # Hotkey
        ttk.Label(self.root, text="Hotkey:").grid(row=5, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.hotkey).grid(row=5, column=1, sticky="we")

        # Apply settings button
        ttk.Button(self.root, text="Apply Settings", command=self.controller.apply_settings).grid(row=6, column=0, columnspan=2, pady=10)

        self.root.columnconfigure(1, weight=1)

    def get_settings(self):
        return {
            "api_key": self.api_key.get(),
            "base_url": self.base_url.get(),
            "model": self.model.get(),
            "system_prompt": self.system_prompt_text.get("1.0", "end-1c"),  # Get text from Text widget
            "user_prompt": self.user_prompt_text.get("1.0", "end-1c"),  # Get text from Text widget
            "hotkey": self.hotkey.get(),
        }

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, message):
        messagebox.showerror("Error", message)
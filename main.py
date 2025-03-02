# main.py
import tkinter as tk
import pyautogui
import keyboard
import time
import os
import io
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI
import base64
from datetime import datetime
from ui import ScreenshotAnalyzerUI
import configparser

class ScreenshotAnalyzerController:
    def __init__(self, root):
        self.root = root
        self.ui = ScreenshotAnalyzerUI(root, self)
        self.config = configparser.ConfigParser()
        self.load_settings()

    def apply_settings(self):
        settings = self.ui.get_settings()
        self.api_key = settings["api_key"]
        self.base_url = settings["base_url"]
        self.model = settings["model"]
        self.system_prompt = settings["system_prompt"]
        self.user_prompt = settings["user_prompt"]
        self.hotkey = settings["hotkey"]

        if not self.api_key:
            self.ui.show_error("API Key is required.")
            return

        try:
            keyboard.remove_hotkey(self.hotkey)
        except Exception as e:
            print(f"Error removing hotkey: {e}")  # Handle the case where the hotkey was not set before
            pass

        keyboard.add_hotkey(self.hotkey, self.capture_and_send)
        self.ui.show_message("Info", f"Settings applied. Press {self.hotkey} to capture.")

        # Save settings to config.ini
        self.config['SETTINGS'] = settings
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
            
    def load_settings(self):
        if os.path.exists('config.ini'):
            self.config.read('config.ini')
            settings = self.config['SETTINGS']
            self.ui.api_key.set(settings.get('api_key', ''))
            self.ui.base_url.set(settings.get('base_url', 'https://openrouter.ai/api/v1'))
            self.ui.model.set(settings.get('model', 'google/gemini-2.0-flash-exp:free'))
            self.ui.system_prompt_text.delete("1.0", tk.END)
            self.ui.system_prompt_text.insert("1.0", settings.get('system_prompt', 'You are an expert game advisor. Analyze the provided screenshot of the game. Based on the current game state, provide concise and actionable guidance to the player. Focus on strategic advice, potential moves, and helpful hints. Keep the response short and directly relevant to the screenshot\'s content.'))
            self.ui.user_prompt_text.delete("1.0", tk.END)
            self.ui.user_prompt_text.insert("1.0", settings.get('user_prompt', 'Analyze this screenshot and provide game guidance.'))
            self.ui.hotkey.set(settings.get('hotkey', 'ctrl+alt+e'))

    def capture_and_send(self):
        try:
            # Capture screenshot
            screenshot = pyautogui.screenshot()
            img_byte_arr = io.BytesIO()
            screenshot.save(img_byte_arr, format='PNG')
            img_byte_arr_value = img_byte_arr.getvalue()

            # Save screenshot to subfolder 'screen'
            self.save_screenshot(screenshot)

            # Send to OpenAI via OpenRouter
            client = OpenAI(base_url=self.base_url, api_key=self.api_key)

            completion = client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": self.user_prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{self.screenshot_to_base64(img_byte_arr_value)}",
                                },
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )

            # Extract and display the response
            answer = completion.choices[0].message.content
            self.display_response(answer)

        except Exception as e:
            print(f"Error: {e}")
            self.display_response(f"An error occurred: {e}")

    def save_screenshot(self, screenshot):
        """Saves the screenshot to the 'screen' subfolder with a timestamped filename."""
        if not os.path.exists("screen"):
            os.makedirs("screen")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screen/screenshot_{timestamp}.png"
        screenshot.save(filename)
        print(f"Screenshot saved to: {filename}")

    def screenshot_to_base64(self, image_bytes):
        """Converts image bytes to base64."""
        return base64.b64encode(image_bytes).decode('utf-8')

    def display_response(self, text):
        """Displays the response in a transparent window on top of the screen."""
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        root.attributes('-alpha', 0.8)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        label = tk.Label(root, text=text, wraplength=screen_width - 20, justify='left', background='white', padx=10, pady=10)
        label.pack()

        root.update_idletasks()
        label_width = label.winfo_width()
        x = (screen_width - label_width) // 2
        root.geometry(f"+{x}+0")

        root.after(10000, root.destroy)

        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    controller = ScreenshotAnalyzerController(root)
    root.mainloop()
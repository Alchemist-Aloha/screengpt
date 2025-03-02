import pyautogui
import keyboard
import time
import os
import io
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI
import tkinter as tk
from tkinter import Toplevel, Label, PhotoImage
import base64
from datetime import datetime

# Retrieve API key from environment variables
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable not set.")

SITE_URL = os.environ.get("SITE_URL", "")  # Optional, retrieve from env or default to empty string
SITE_NAME = os.environ.get("SITE_NAME", "") # Optional, retrieve from env or default to empty string
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "google/gemini-2.0-flash-exp:free"  # or another vision model, if appropriate for your request.

client = OpenAI(
    base_url=BASE_URL,
    api_key=OPENROUTER_API_KEY,
)

def capture_and_send():
    """Captures a screenshot, sends it to OpenAI via OpenRouter, and displays the response."""
    try:
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        img_byte_arr = io.BytesIO()
        screenshot.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Save screenshot to subfolder 'screen'
        save_screenshot(screenshot)        

        # Send to OpenAI via OpenRouter
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": SITE_URL,  # Optional
                "X-Title": SITE_NAME,  # Optional
            },
            model=MODEL,  # or another vision model, if appropriate for your request.
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert game advisor. Analyze the provided screenshot of the game. Based on the current game state, provide concise and actionable guidance to the player. Focus on strategic advice, potential moves, and helpful hints. Keep the response short and directly relevant to the screenshot's content.",
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Analyze this screenshot and provide game guidance."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{screenshot_to_base64(img_byte_arr)}",
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )

        # Extract and display the response
        answer = completion.choices[0].message.content
        display_response(answer)

    except Exception as e:
        print(f"Error: {e}")
        display_response(f"An error occurred: {e}")

def screenshot_to_base64(image_bytes):
    """Converts image bytes to base64."""
    return base64.b64encode(image_bytes).decode('utf-8')

def save_screenshot(screenshot):
    """Saves the screenshot to the 'screen' subfolder with a timestamped filename."""
    if not os.path.exists("screen"):
        os.makedirs("screen")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screen/screenshot_{timestamp}.png"
    screenshot.save(filename)
    print(f"Screenshot saved to: {filename}")
    
def display_response(text):
    """Displays the response in a transparent window on top of the screen."""
    root = tk.Tk()
    root.overrideredirect(True)  # Remove window decorations
    root.attributes('-topmost', True)  # Make it always on top
    root.attributes('-alpha', 0.8)  # Transparency

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Create a label with the response text
    label = Label(root, text=text, wraplength=screen_width - 20, justify='left', background='white', padx=10, pady=10)
    label.pack()

    # Position the window at the top center
    root.update_idletasks() #makes sure the label has been created.
    label_width = label.winfo_width()
    x = (screen_width - label_width) // 2
    root.geometry(f"+{x}+0") #position the window.

    # Close the window after a delay
    root.after(10000, root.destroy)  # Close after 10 seconds (adjust as needed)

    root.mainloop()

def on_key():
    """Callback function for Ctrl+Alt+E hotkey."""
    capture_and_send()

# Register the hotkey
keyboard.add_hotkey('ctrl+alt+e', on_key)

print("Press Ctrl+alt+E to capture a screenshot and get an AI analysis via OpenRouter.")
keyboard.wait()
import time
import pyautogui
import cv2
import numpy as np
import pytesseract
from Notification import send_notification
from globals import rewind_count
from Click import upgrade_and_rewind

class GameState:
    def __init__(self):
        self.screenshot = None
        self.state = "unknown"  # Default state

    def set_state(self, text):
        if "skill" in text.lower():
            self.state = "skills menu"
        elif "stat" in text.lower():
            self.state = "stats menu"
        elif "resume" in text.lower():
            self.state = "pause menu"
        elif "revive" in text.lower():
            self.state = "defeated"
        elif "time" and "mobs" and "killed" and "days" and "portals" in text.lower():
            self.state = "end of run"
            upgrade_and_rewind()

        elif "select the" in text.lower():
            self.state = "ANTI-MACRO DETECTED select the correct image"
            # send notification
            send_notification("Days Bygone", "Rewind Count: " + str(rewind_count))
            time.sleep(1)
            send_notification("Days Bygone", "Anti Macro Triggered!")
            print("Anti Macro Triggered! Exiting the program.")
            quit()
        elif "tap" in text.lower():
            self.state = "ANTI-MACRO DETECTED tap"
            send_notification("Days Bygone", "Rewind Count: " + str(rewind_count))
            time.sleep(1)
            send_notification("Days Bygone", "Anti Macro Triggered!")
            print("Anti Macro Triggered! Exiting the program.")
            quit()



    def get_state(self):
        return self.state

    def capture_screen(self):
        # Get the list of windows with the title 'BlueStacks'
        windows = pyautogui.getWindowsWithTitle('BlueStacks')

        if windows:
            # Get the first window
            window = windows[0]

            # Activate the window to bring it to the front
            window.activate()
            time.sleep(0.01)

            # Get the window's left, top, width, and height attributes
            left, top, width, height = window.left, window.top, window.width, window.height

            # Take a screenshot of the specific area
            self.screenshot = pyautogui.screenshot(region=(left, top, width, height))

            # Save the screenshot
            self.screenshot.save('game_screen.png')


    def preprocess_image(self):
        # Load the image
        img = cv2.imread('game_screen.png')

        # Resize the image to make the text larger
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

        # Convert to gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply thresholding
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        return thresh

    def extract_text(self, image):
        # OCR
        text = pytesseract.image_to_string(image)
        return text


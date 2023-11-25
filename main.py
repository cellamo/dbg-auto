import time
from GameState import GameState
from globals import rewind_count
import keyboard
import pyautogui

# Create an instance of the GameState class
game_state = GameState()

# Initialize the previous state to None
prev_state = None

rewind_count[0] = 0

while True:
    # Get the position and size of the BlueStacks window
    windows = pyautogui.getWindowsWithTitle('BlueStacks')
    if not windows:
        print("BlueStacks window not found!")
        exit(1)

    window = windows[0]
    window.activate()

    # Capture the current game screen
    game_state.capture_screen()

    # Preprocess the captured image to prepare it for OCR
    image = game_state.preprocess_image()

    # Extract text from the preprocessed image using OCR
    text = game_state.extract_text(image)

    # Set the game state based on the extracted text
    game_state.set_state(text)

    # Get the current state
    current_state = game_state.get_state()

    # If the state has changed, print the new state
    if current_state != prev_state:
        print(current_state)
        prev_state = current_state

    if keyboard.is_pressed('esc'):
        quit()

    # Wait for 1000ms
    time.sleep(1)



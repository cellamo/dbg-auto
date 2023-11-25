import pyautogui
import random
import time
from globals import buttons, rewind_count
import keyboard
from Notification import send_notification

# Get the position and size of the BlueStacks window
windows = pyautogui.getWindowsWithTitle('BlueStacks')
if not windows:
    print("BlueStacks window not found!")
    exit(1)

window = windows[0]
window_left, window_top, window_width, window_height = window.left, window.top, window.width, window.height

def click_in_area(area):
    window.activate()
    x, y, width, height = area

    # Adjust coordinates relative to the BlueStacks window
    click_x = window_left + x + random.randint(0, width)
    click_y = window_top + y + random.randint(0, height)

    # Move to the point and click
    pyautogui.click(click_x, click_y)

    # Add a delay between 0.01 and 0.1 seconds
    time.sleep(random.uniform(0.01, 0.1))

# Example usage: Click the pause button
# click_in_area(buttons['pause'])

def upgrade_and_rewind():
    if keyboard.is_pressed('esc'):
        print("ESC key pressed. Exiting the program.")
        quit()

    # Return to menu
    print("Returning to menu...")
    click_in_area(buttons['return_menu'])
    time.sleep(3)

    # Open stats menu
    click_in_area(buttons['open_stats'])
    time.sleep(0.4)

    # Select 25
    click_in_area(buttons['select_25'])
    time.sleep(0.4)

    # Upgrade damage
    click_in_area(buttons['upgrade_damage'])
    time.sleep(0.4)

    # Select 100
    click_in_area(buttons['select_100'])
    time.sleep(0.4)

    # Upgrade crit
    click_in_area(buttons['upgrade_crit'])
    time.sleep(0.4)

    # Open skills menu
    print("Opening skills menu...")
    click_in_area(buttons['open_skills_menu'])
    time.sleep(0.5)

    # rewind
    print("Rewinding...")
    click_in_area(buttons['rewind'])
    time.sleep(0.4)

    # rewind confirm
    click_in_area(buttons['rewind_confirm'])
    time.sleep(0.8)
    
    # increment rewind count
    rewind_count[0] += 1
    print("Rewind Count: " + str(rewind_count[0]))
    send_notification("Days Bygone", "Rewind Completed. Total Rewinds: " + str(rewind_count))

    # open stats menu
    print("Opening stats menu...")
    click_in_area(buttons['open_stats'])
    time.sleep(0.4)

    # select 100
    click_in_area(buttons['select_100'])
    time.sleep(0.2)

    # upgrade gold
    print("Upgrading gold...")
    click_in_area(buttons['upgrade_gold'])
    time.sleep(0.2)

    # battle
    print("Starting battle...")
    click_in_area(buttons['battle'])
    time.sleep(0.5)

    # campaign
    click_in_area(buttons['campaign'])
    time.sleep(0.2)

    # x2
    click_in_area(buttons['x2'])
    time.sleep(0.2)
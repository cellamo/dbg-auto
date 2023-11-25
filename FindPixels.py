import time
import pyautogui
import cv2


def on_mouse(event, x, y, flags, params):
    global top_left_pt, bottom_right_pt, drawing

    # Detecting mouse button down event
    if event == cv2.EVENT_LBUTTONDOWN:
        if top_left_pt is None:
            top_left_pt = (x, y)
        else:
            bottom_right_pt = (x, y)
            drawing = False

def get_area_coordinates():
    global top_left_pt, bottom_right_pt, drawing
    top_left_pt, bottom_right_pt = None, None
    drawing = True

    windows = pyautogui.getWindowsWithTitle('BlueStacks')

    # Take a screenshot using PyAutoGUI
    window = windows[0]

    # Activate the window to bring it to the front
    window.activate()
    time.sleep(0.01)

    # Get the window's left, top, width, and height attributes
    left, top, width, height = window.left, window.top, window.width, window.height

    # Take a screenshot of the specific area
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # Save the screenshot
    screenshot.save('game_screen.png')

    # Read the screenshot with OpenCV
    image = cv2.imread('game_screen.png')

    # Create a window and set a mouse callback function
    cv2.namedWindow('Game Screen')
    cv2.setMouseCallback('Game Screen', on_mouse)

    while drawing:
        # Display the image
        cv2.imshow('Game Screen', image)

        # Draw the rectangle
        if top_left_pt is not None and bottom_right_pt is not None:
            cv2.rectangle(image, top_left_pt, bottom_right_pt, (0, 255, 0), 2)

        # Breaking out of the loop
        if cv2.waitKey(1) & 0xFF == 27:  # Escape key
            break

    cv2.destroyAllWindows()

    if top_left_pt and bottom_right_pt:
        print("Top Left Point: ", top_left_pt)
        print("Bottom Right Point: ", bottom_right_pt)
        return top_left_pt, bottom_right_pt

# Run the function
get_area_coordinates()
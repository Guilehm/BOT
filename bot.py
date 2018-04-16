import time

import pyautogui
from PIL import ImageGrab

bg_color = (247, 247, 247)
player_color = (83, 83, 83)

print('starting at 4 seconds...')
time.sleep(4)


def detect_object(x1, x2, y1, y2):
    screen = ImageGrab.grab()
    for x in range(x1, x2):
        for y in range(y1, y2):
            color = screen.getpixel((x, y))
            if color == (83, 83, 83):
                return True

while True:
    if detect_object(300, 320, 390, 450):
        pyautogui.press('up')
import time
import _thread

import pyautogui
from PIL import ImageGrab

# bg_color = (247, 247, 247)
# player_color = (83, 83, 83)

print('starting at 4 seconds...')
time.sleep(4)


def increase(x):
    while True:
        x += 0.1
        print('def increase')
        time.sleep(1)


def detect_object(x1, x2, y1, y2):
    screen = ImageGrab.grab()
    bg_color = screen.getpixel((180, 160))
    for x in range(int(x1), int(x2)):
        for y in range(y1, y2):
            color = screen.getpixel((x, y))
            if color != bg_color:
                return True



X = 530.0
while True:
    X += 0.00000000000017
    if detect_object(X, X+90, 590, 680):
        pyautogui.press('up')
import time

import pyautogui
from PIL import ImageGrab

# bg_color = (247, 247, 247)
player_color = (83, 83, 83)

print('starting at 4 seconds...')
time.sleep(4)

X = 330.0

def detect_object(x1, x2, y1, y2):
    screen = ImageGrab.grab()
    bg_color = screen.getpixel((10, 80))
    for x in range(int(x1), int(x2)):
        for y in range(y1, y2):
            color = screen.getpixel((x, y))
            if color != bg_color:
                print(color)
                return True

while True:
    if detect_object(X, X+20, 380, 420):
        pyautogui.press('up')
        seconds = time.clock()
        # print('Time:', seconds)
        X += 0.9

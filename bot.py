import time

import pyautogui
from PIL import ImageGrab

bg_color = (247, 247, 247)
player_color = (83, 83, 83)

print('starting at 4 seconds...')
time.sleep(4)

# while True:
#     screen = ImageGrab.grab()
#     for x in range(300, 350):
#         for y in range(383, 460):
#             color = screen.getpixel((x, y))
#             if color != (247, 247, 247):
#                 print(color)
    # monster = screen.getpixel((280, 450))
    # print(monster)

def detect_object():
    screen = ImageGrab.grab()
    for x in range(300, 320):
        for y in range(390, 450):
            color = screen.getpixel((x, y))
            if color == (83, 83, 83):
                return True

while True:
    if detect_object():
        pyautogui.press('up')
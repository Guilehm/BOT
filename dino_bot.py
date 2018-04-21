import time
from timeit import default_timer

import pyautogui
from PIL import ImageGrab

# bg_color = (247, 247, 247)
player_color = (83, 83, 83)

print('starting at 4 seconds...')
time.sleep(4)

<<<<<<< HEAD
X = 325.0
=======
X = 530.0
>>>>>>> e96b8daa3faf8bdaeefe0fdeff0f13cd8205d453

def detect_object(x1, x2, y1, y2):
    screen = ImageGrab.grab()
    bg_color = screen.getpixel((180, 160))
    for x in range(int(x1), int(x2)):
        for y in range(y1, y2):
            color = screen.getpixel((x, y))
            if color != bg_color:
                # print(color)
                return True

<<<<<<< HEAD
last = default_timer()
while True:
    if detect_object(X, X+26, 380, 420):
        pyautogui.press('up')
        seconds = time.clock()
        # print('Time:', seconds)
        # X += 1.2
        if default_timer() - last > 1:
            X += 2.3
=======
jumps = 0
while True:
    if detect_object(X, X+90, 590, 680):
        pyautogui.press('up')
        seconds = time.clock()
        jumps += 1
        X += 1.1
        print('Jumps:', jumps)
>>>>>>> e96b8daa3faf8bdaeefe0fdeff0f13cd8205d453

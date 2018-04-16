import time

from PIL import ImageGrab

bg_color = (247, 247, 247)
player_color = (83, 83, 83)

print('starting at 4 seconds...')
time.sleep(4)
screen = ImageGrab.grab()


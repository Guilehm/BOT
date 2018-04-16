import time

from PIL import ImageGrab

print('starting at 4 seconds...')
time.sleep(4)
screen = ImageGrab.grab()
color = screen.getpixel((100, 430))
print(color)

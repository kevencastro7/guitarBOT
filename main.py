import pyscreenshot as ImageGrab
import pyautogui
import numpy as np
import datetime
import  time
'''
im = ImageGrab.grab()
color = im.getpixel((600, 450))
print color
'''

def pressTeclas(teclas):
    if len(teclas) == 5:
        pyautogui.hotkey(teclas[0],teclas[1],teclas[2],teclas[3],teclas[4])
    elif len(teclas) == 4:
        pyautogui.hotkey(teclas[0],teclas[1],teclas[2],teclas[3])
    elif len(teclas) == 3:
        pyautogui.hotkey(teclas[0],teclas[1],teclas[2])
    elif len(teclas) == 2:
        pyautogui.hotkey(teclas[0],teclas[1])
    else:
        pyautogui.hotkey(teclas[0])

# time.sleep(2)
a = datetime.datetime.now().microsecond

# pressTeclas(['a'])
im = ImageGrab._grab_simple(True,filename='image.png',bbox=[10,10,100,100])



print datetime.datetime.now().microsecond/1000 - a/1000

#abcdeabcabaaaaaaaaaaaa
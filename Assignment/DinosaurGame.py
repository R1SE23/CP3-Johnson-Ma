from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *
class Coordinates():
    replayBtn = (480,500)
    dinosaur = (181,510)
    #250 = x coordinate to check for tree
    #y coordinate = 535
def restartGame():
    pyautogui.click(Coordinates.replayBtn)



def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')




def imageGrab():
    global a
    box = (250, 512, 290, 542)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    print(a.sum())

def main():
    while True:
        imageGrab()
        if a.sum()!=1447:
            pressSpace()
restartGame()
main()

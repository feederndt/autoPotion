import pyautogui
import cv2
import keyboard

from time import sleep

pyautogui.ImageNotFoundException()

def isHaveSoftwood():
    woodPosition = pyautogui.locateAllOnScreen(
        image="images/softwood.png", grayscale=False, region=[680, 700, 500, 350], confidence=0.8)
    positionArr = []
    for pos in woodPosition:
     positionArr.append(pos)

    print(positionArr)

def isSoftwoodSelecting():
  try:
    isSoftwoodSelecting = pyautogui.locateOnScreen(
        image="images/woodSelecting.png", grayscale=False, region=[680, 700, 500, 350], confidence=0.9)
    print("ok")

    return bool(isSoftwoodSelecting)
  except pyautogui.ImageNotFoundException:
    print("Deo thay")

    return False

if __name__ == "__main__":
    # isHaveSoftwood()
    isSoftwoodSelecting()

    # running = True

    # while running:
    #     if keyboard.is_pressed("l"):
    #         running = not running
    #     isSoftwood()

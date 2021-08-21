import pyautogui
import numpy as np
import cv2
import time


def Fishing(x, y, size, hold):
    pyautogui.screenshot('screen.png', region=(x, y, size, size))
    img = cv2.imread('screen.png')
    cv2.imshow("cap", img)
    cv2.waitKey(1)
    t = 0
    for x in range(0, size, 1):
        for y in range(0, size, 1):
            r, g, b = (img[y, x])
            if r == 255 and g == 255 and b == 255:
                t += 1
    if t > hold:
        return 1
    else:
        return 0


def chooseRod(delay, pay):
    pyautogui.press('e')  # bag
    time.sleep(delay)
    pyautogui.press('1')  # choose tab rod
    time.sleep(delay)
    pyautogui.press('2')  # choose rad
    time.sleep(delay)
    if pay == 1:
        pyautogui.press('5')  # pay
        time.sleep(delay)


time.sleep(3)

# chooseRod(0.4, 0)


while True:
    time.sleep(0.5)
    pyautogui.press('3')  # fish
    time.sleep(0.2)
    while Fishing(994, 378, 50, 10) == 0:
        pass
    pyautogui.press('space')
    time.sleep(4)
    pyautogui.press('4')
    time.sleep(0.1)

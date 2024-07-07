import pyautogui
from time import sleep

n = int(input())
sleep(2)
for i in range(1, n + 1):
    pyramid_row = '#' * i
    pyautogui.write(pyramid_row,interval=0.25)
    pyautogui.press('enter')
    



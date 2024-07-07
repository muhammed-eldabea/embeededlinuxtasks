import pyautogui as py 
import time

py.moveTo(100, 100, duration=1)
py.click()
time.sleep(1)
py.typewrite("Hello World")
time.sleep(1)
py.press('enter')
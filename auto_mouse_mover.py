import pyautogui, time

pyautogui.FAILSAFE = False
print("This program is for people who like to pretend they work:)")
try:
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x+1, y)
        time.sleep(300)
        x, y = pyautogui.position()
        pyautogui.moveTo(x-1, y)
        time.sleep(300)

except KeyboardInterrupt:
    print('\n')
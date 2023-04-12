import pyautogui as pag
import time

def setup():
    pegasusBackground = "main/images/pegasus-background.png"
    win1 = "main/images/win1.png"
    win2 = "main/images/win2.png"
    win3 = "main/images/win3.png"
    win4 = "main/images/win4.png"
    win5 = "main/images/win5.png"
    win6 = "main/images/win6.png"
    noWindows = "main/images/no-windows.png"
    viewChange = "main/images/view-change.png"

    windowSelect("Pegasus")

    while True:
        pag.hotkey("alt", "w")
        if pag.locateOnScreen(noWindows) == None:
            pegasusWindowSelect(1)
            pag.hotkey("alt", "c")
            time.sleep(1)
            if pag.locateOnScreen(viewChange):
                pag.hotkey("alt", "n")
            print("closed windows")
        else:
            print("no windows")
            break

    while pag.locateOnScreen(pegasusBackground) == None:
        pass
    pag.click(pag.locateOnScreen(pegasusBackground), button = "right")
    for i in range(2):
        pag.press("down", presses = 2)
        pag.press("right")
    pag.press("enter")
    while pag.locateOnScreen(win1) == None:
        pass
    pag.hotkey("alt", "l")
    while pag.locateOnScreen(win2) == None:
        pass    
    pegasusWindowSelect(1)
    pag.hotkey("alt", "i")
    pag.press("1")
    while pag.locateOnScreen(win3) == None:
        pass
    while pag.locateOnScreen(pegasusBackground) == None:
        pass
    pag.click(pag.locateOnScreen(pegasusBackground), button = "right")
    for i in range(2):
        pag.press("down", presses = 2)
        pag.press("right")
    pag.press("up")
    pag.press("right", presses = 2)
    pag.press("up", presses = 2)
    pag.press("right")
    pag.press("enter")
    while pag.locateOnScreen(win4) == None:
        pass
    pag.hotkey("alt", "l")
    while pag.locateOnScreen(win5) == None:
        pass
    pegasusWindowSelect(4)
    pag.hotkey("alt", "i")
    while pag.locateOnScreen(win6) == None:
        pass

def windowSelect(window):
    if window == "Pegasus":
        pegasus = pag.getWindowsWithTitle("Pegasus CIS - K A Watts Plumbing & Heating Ltd")[0]
        pegasus.maximize()
        pegasus.activate()
    elif window == "Excel":
        excel = pag.getWindowsWithTitle("Call Off Sheet - Excel")[0]
        excel.maximize()
        excel.activate()

def pegasusWindowSelect(window):
    windowSelect("Pegasus")
    pag.hotkey("alt", "w")
    if window == 1:
        pag.press("1")
    elif window == 2:
        pag.press("2")
    elif window == 3:
        pag.press("3")
    elif window == 4:
        pag.press("4")
    elif window == 5:
        pag.press("5")
    elif window == 6:
        pag.press("6")
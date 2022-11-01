import pyautogui as pag
import pyperclip as pyp
import time
from call_off.window_selector import WindowSelector
from data.job_details import jobDetails

class FillSheet():

    def __init__(self):
        ""
        self._selector = WindowSelector()

    def fillSheet(self, sheetData, fileName):
        self._prepSheet()
        self._write(sheetData)
        self._saveAs(sheetData, fileName)
        self._checkFileName()
        time.sleep(2)

    def _waitWindow(self, name):
        """Wait for the specified window to appear"""
        # Loop until window called "name" has appeared
        waiting = True
        while waiting:
            # Get a list of all window titles
            windows = pag.getAllTitles()
            # If the specified name exists in "windows", focus that window and end the loop
            if name in windows:
                window = pag.getWindowsWithTitle(name)[0]
                window.activate()
                waiting = False

    def _prepSheet(self):
        ""
        # Select the call off sheet
        self._selector.selectWindow("excel")
        # Move select the cell in the top left corner of the sheet
        pag.hotkey("ctrl", "home")
        # Navigate to the developer name cell
        pag.press("right")
        pag.press("down")

    def _write(self, sheetData):
        ""
        # Move down through the cells on the sheet, filling in the appropriate data for each
        for item in sheetData:
            pag.write(item)
            pag.press("down")

    def _saveAs(self, sheetData, fileName):
        # Save as
        pag.press("f12")
        # Wait until the "Save As" window has appeared
        self._waitWindow("Save As")
        # Select the file type drop down
        pag.hotkey("alt", "t")
        # Select PDF as file type
        pag.press("p")
        # Return to the file name input box
        pag.hotkey("alt", "n")
        # Enter the name of the file
        if fileName != "1ST FIX KIT":
            pag.write(f"{jobDetails[sheetData[0]][sheetData[1]][2]} Plot {sheetData[2]} {fileName.title()} Call off sheet.pdf")
        else:
            pag.write(f"{jobDetails[sheetData[0]][sheetData[1]][2]} Plot {sheetData[2]} 1st Fix Kit Call of sheet.pdf")
        # Save
        pag.press("enter")

    def _checkFileName(self):
        # If the file name already exists
        while True:
            time.sleep(0.1)
            if "Confirm Save As" in pag.getAllTitles():
                pag.press("enter")
                pag.hotkey("alt", "n")
                self._copy()
                fileName = pyp.paste()
                if fileName[-1] == "f":
                    fileName = fileName[0:-4]
                
                if fileName[-1].isnumeric() == False:
                    fileName = " ".join([fileName, "2"])
                else:
                    fileNumber = int(fileName[-1]) + 1
                    fileName = f"{fileName[0:-1]}{fileNumber}"
                pag.press("delete")
                pag.write(fileName)
                pag.press("enter")
            else:
                break

    def _copy(self):
        """Uses the keyboard shortcut 'ctrl' + 'c'"""
        pag.hotkey("ctrl", "c")
        time.sleep(0.1)
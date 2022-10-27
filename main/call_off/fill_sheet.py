import pyautogui as pag
import time
from call_off.window_selector import WindowSelector

class FillSheet():

    def __init__(self):
        ""
        self._selector = WindowSelector

    def fillSheet(self, sheetData, fileName):
        # Select the call off sheet
        self._selector.selectWindow("Excel")
        # Move select the cell in the top left corner of the sheet
        pag.hotkey("ctrl", "home")
        # Navigate to the developer name cell
        pag.press("right")
        pag.press("down")
        # Move down through the cells on the sheet, filling in the appropriate data for each
        for item in sheetData:
            pag.write(item)
            pag.press("down")
        # Save as
        pag.press("f12")
        # Wait until the "Save As" window has appeared
        self._waitWindow("Save As")
        # Select the file type drop down
        pag.press("tab")
        # Select PDF as file type
        pag.press("p")
        # Return to the file name input box
        pag.hotkey("shift", "tab")
        # Enter the name of the file
        if fileName != "1ST FIX KIT":
            pag.write(f"Plot {sheetData[2]} {fileName.title()} Call off sheet.pdf")
        else:
            pag.write(f"Plot {sheetData[2]} 1st Fix Kit Call of sheet.pdf")
        # Save
        pag.press("enter")
        # If the file name already exists
        time.sleep(0.1)
        if "Confirm Save As" in pag.getAllTitles():
            # File already exists
            print(f"Tried to save 'Plot {sheetData[2]} {fileName.title()} Call off sheet.pdf', but the file already exists")
            # Print call off sheet data to console so that it isn't lost
            for item in sheetData:
                print(item)
            # Do not overwrite existing file
            pag.press("enter")
            # Close "Save As" window
            pag.press("esc")
        time.sleep(2)

    def _waitWindow(name):
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
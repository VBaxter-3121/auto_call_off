import pyautogui as pag
import pyperclip as pyp
import time
from call_off.window_selector import WindowSelector

class ReadRecords():
    ""

    def __init__(self):
        ""
        self._selector = WindowSelector()
        self._win4 = "main/images/win4.png"

    def read(self, requiredStages):
        ""
        prevPo = ""
        # alternateStages = self._getAlternateStages(requiredStages)
        alternateStagesFound = []
        requiredPoDict = {}

        headerNotes = self._findHeaderNotes()
        self._selectFirstCell()
        
        while True:
            currentPo = self._getCurrentPo()
            if currentPo == prevPo:
                break
            currentNotes = self._getCurrentNotes(headerNotes)
            currentSupplier = self._getCurrentSupplier()
            currentStage = self._getCurrentStage()

            self._selectNextCell()
            self._poRequired(requiredStages,
                [currentPo, currentStage, currentSupplier, currentNotes],
                requiredPoDict)
            prevPo = currentPo
        
        return requiredPoDict

    # def _getAlternateStages(requiredStages):
    #     ""
    #     alternateStages = []
    #     for stage in requiredStages:
    #         if stage == "MID FIX":
    #             alternateStages.append("SHOWER TRAY")
    #         elif stage == "HEATING & BATH":
    #             alternateStages.append("HEATING")
    #             alternateStages.append("BATH")
    #             alternateStages.append("2ND FIX KIT")
    #         elif stage == "FIX 2":
    #             alternateStages.append("2ND FIX FITTINGS")
    #         elif stage == "FINALS":
    #             alternateStages.append("HEATING FINALS")
    #             alternateStages.append("SANI FINALS")
    #     return alternateStages

    def _findHeaderNotes(self):
        ""
        self._selector.selectPegasusWindow(4)
        # Locate position of header notes
        pag.moveTo(pag.locateOnScreen(self._win4))
        pag.move(25, 50)
        return pag.position()

    def _selectFirstCell(self):
        ""
        self._selector.selectPegasusWindow(5)
        # Move selection to the Po column
        pag.press("home")
        # Ensure first cell is selected
        pag.press("f12")
        pag.press("f9")

    def _getCurrentPo(self):
        ""
        self._selector.selectPegasusWindow(5)
        self._copy()
        return pyp.paste()

    def _getCurrentStage(self):
        ""
        self._selector.selectPegasusWindow(6)
        # Open the "All Purchase Order Item List" window
        pag.hotkey("alt", "l")
        # Move to the "Manufacturer Code" column
        pag.press("right")
        pag.press("right")
        pag.press("right")
        pag.press("right")
        pag.press("right")
        pag.press("right")
        self._copy()
        # Close the "All Purchase Order Item List" window
        pag.hotkey("alt", "c")
        return pyp.paste()
        
    def _getCurrentSupplier(self):
        ""
        self._selector.selectPegasusWindow(5)
        # Move to the supplier column, copy the value and save to variable currentSupplier
        ## This assumes that the supplier column is 2 to the right of the Po number. Make
        ## sure that this is the case otherwise it will pick up the wrong information.
        pag.press("right")
        pag.press("right")
        self._copy()
        return pyp.paste()       

    def _getCurrentNotes(self, headerNotes):
        ""
        # Select current order
        pag.press("enter")
        # Check header notes
        self._selector.selectPegasusWindow(4)
        pag.hotkey("alt", "n")
        pag.click(headerNotes, button="right")
        pag.press("a")
        self._copy()
        return pyp.paste()

    def _selectNextCell(self):
        ""
        self._selector.selectPegasusWindow(5)
        # Return to the Po number coloumn and move to the next order
        pag.press("home")
        pag.press("f11")

    def _copy(self):
        """Uses the keyboard shortcut 'ctrl' + 'c'"""
        pag.hotkey("ctrl", "c")
        time.sleep(0.1)

    def _poRequired(self, requiredStages, currentPoDetails, requiredPoDict):
        ""
        if currentPoDetails[1] in requiredStages:
            requiredPoDict[currentPoDetails[0]] = [currentPoDetails[1],
                currentPoDetails[2], currentPoDetails[3]]

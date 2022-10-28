import pyautogui as pag
import time
from call_off.window_selector import WindowSelector

class FilterRecords:
    "Filters records on Pegasus"

    def __init__(self):
        "Contructs an instance of the FilterRecords class"
        self._selector = WindowSelector()
        self._default = "main\images\default-job-number.png"
        self._empty = "main\images\empty-list.png"

    def filter(self, jobNumber, phaseNumbers):
        """Filters Pegasus orders by job number and phase number
        
        Parameters:
        jobNumber: A string representing an individual job number
        phaseNumbers: A list of strings representing phase numbers
        """
        self._selector.selectPegasusWindow(5)

        # Clear any existing filters
        pag.hotkey("ctrl", "f6")
        # Open filter window
        pag.press("f6")
        time.sleep(1)
        # Open the advanced section
        pag.hotkey("alt", "v")

        ## Add expression to filter by job number
        # Focus "Field Name" drop down
        pag.hotkey("alt", "n")

        # If "Field Name" not set to "Default Job Number", set it correctly
        if pag.locateOnScreen(self._default) == None:
            while True:
                pag.press("d")
                if pag.locateOnScreen(self._default) != None:
                    break
        
        # Focus input field
        pag.press("tab", presses=2)
        # Enter job number
        pag.write(jobNumber)
        # Add to filter expressions
        pag.hotkey("alt", "a")

        ## Add one or more expressions to filter by phase numbers
        for number in phaseNumbers:
            # Focus "Field Name" drop down
            pag.hotkey("alt", "n")
            # If "Field Name", not set to "Cost Phase Type", set it correctly
            pag.press("c")
            # Focus input field
            pag.press("tab", presses=2)
            # Enter phase number
            pag.write(number)
            # Add to filter expressions
            pag.hotkey("alt", "a")

        ## Set and/or logic to filters if filtering by more than one phase number
        if len(phaseNumbers) > 1:
            # Select filters
            pag.hotkey("shift", "tab")
            # Move to first filter
            pag.press("pgup")
            # Move past first filter (job number) and second filter (first phase number)
            pag.press("down", presses=2)
            for i in range(len(phaseNumbers) - 1):
                # Set relationship to "Or"
                pag.hotkey("alt", "o")
                # Return selection to current filter
                pag.press("tab", presses=5)
                # Move to next filter (if this is the last filter, this won't affect anything)
                pag.press("down")

            # Select all filters
            ## For some reason you need to use both the left and right shift keys in order
            ## to select the items in the list in this instance.
            ## https://stackoverflow.com/questions/56949628/keydown-function-not-working-with-shift-key
            pag.hotkey("shiftleft", "shiftright", "pgup")
            # Remove job number filter from selection
            pag.hotkey("shiftleft", "shiftright", "down")
            # Group phase number filters
            pag.hotkey("alt", "g")

        # Close advanced section
        pag.hotkey("alt", "v")
        # Move selection to "OK"
        pag.press("tab")
        # Filter purchase orders
        pag.press("enter")

        # Check if any records were found
        time.sleep(0.5)
        if pag.locateOnScreen(self._empty) != None:
            print(f"No records found for the following filter: {jobNumber}, {str(phaseNumbers)}")
            return False
        else:
            return True
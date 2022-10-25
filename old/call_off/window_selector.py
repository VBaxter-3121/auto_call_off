import pyautogui as pag

class WindowSelector:
    "Provides functions that allow certain windows to be selected"

    def __init__(self):
        "Contructs an instance of the WindowSelector class"

    def selectWindow(self, title):
        """Focuses the specified window
        
        Parameters:
        title: A string referencing the window to be focused
        """
        if title == "pegasus":
            window = pag.getWindowsWithTitle("Pegasus CIS - K A Watts Plumbing & Heating Ltd")[0]
            window.maximize()
            window.activate()
        elif title == "excel":
            window = pag.getWindowsWithTitle("Call Off Sheet - Excel")[0]
            window.maximize()
            window.activate()

    def selectPegasusWindow(self, window):
        """Focus the Pegasus program, then focus the specified window within
        Pegasus. This function assumes that the windows were opened in this order:
        'Purchase Orders'
        'Purchase Order List'
        'Purchase Order Items'
        'All Purchase Orders'
        'All Purchase Order List'
        'All Purchase Order Items'

        Parameters:
        window(int): A number from 1-6 referencing one of the six windows in
        Pegasus
        """
        self.selectWindow("pegasus")
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
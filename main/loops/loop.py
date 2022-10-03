import PySimpleGUI as sg

class Loop():
    """The loop keeps a window running until the user closes the
    window.
    """

    def __init__(self, window):
        "Prepares the loop to run"
        self._window = window

    def startLoop(self):
        "Begins the loop"
        while True:
            event, values = self._window.read()

            # For testing
            print(event)

            if event == sg.WIN_CLOSED:
                break

            self._listenLoop(event, values)
        
        self._window.close()
    
    def _listenLoop(self, event, values):
        "Checks for events and calls appropriate functions"

        if event == "":
            ""
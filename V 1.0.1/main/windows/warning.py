import PySimpleGUI as sg
from windows.window import Window

class Warning(Window):
    """"""

    def __init__(self, plots):
        "Contructs an instance of the warning class"
        self._title = "Plots without data"
        self._layout = [
            [sg.Text(f"""Warning: the following plots have had no data set for them:
{plots}
If you continue now, these plots will be removed from the call off list.""")],
            [sg.Button("Cancel", size=(10, 1), key="cancel"), sg.Button("Continue", size=(10, 1), key="continue")]
        ]
        super().__init__(self._title, self._layout)
        self._window.DisableClose=True
    
    def read(self):
        "Handles events and values related to the warning window"
        while True:
            event, values = self._window.read()
            if event == sg.WIN_CLOSED:
                break

            elif event == "cancel":
                self._window.close()
                return "cancel"

            elif event == "continue":
                self._window.close()
                return "continue"
import PySimpleGUI as sg
from windows.window import Window

class Output(Window):
    ""

    def __init__(self):
        ""
        self._title = "Call Off Output"
        self._layout = [
            [sg.Text("Check below notes and add header notes where appropriate")],
            [sg.Listbox(values=[], size=(100, 30), key="outputList")],
            [sg.Push(), sg.Checkbox("Progress Sheets Updated", default=False, enable_events=True, key="check"), 
                sg.Button("Continue", size=(10, 1), disabled=True, key="continue")]
        ]

        super().__init__(self._title, self._layout)
        self._window.DisableClose=True

        self._outputList = self._window["outputList"]
        self._check = self._window["check"]
        self._continue = self._window["continue"]

    def read(self):
        ""
        while True:
            event, values = self._window.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == "continue":
                break

            self._toggleDisabled(event, values)

    def _toggleDisabled(self, event, values):
        "Checks if each button should be disabled or not"
        if self._check.get() == True:
            self._continue.update(disabled=False)
        else:
            self._continue.update(disabled=True)

    def printLine(self, line):
        ""
        self._outputList.Values.append(line)
        self._outputList.update(self._outputList.Values)
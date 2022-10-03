import PySimpleGUI as sg
from windows.window import Window

class EditGroup(Window):
    """This window allows the user to edit the developer, site, and
    plot numbers of an existing group. The user can go into the
    details for each individual plot and edit them.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self):
        "Contruscts the 'Edit Group' window"
        self._title = "Edit Group"
        self._layout = [
            [sg.Text("Developer:")],
            [sg.Combo(values=[], size=(30, 1), key="developer")],
            [sg.Text("Site:")],
            [sg.Combo(values=[], size=(30, 1), key="site")],
            [sg.Text("Plots:")],
            [sg.In(size=(30, 1), key="plotInput")],
            [sg.Listbox(values=[], size=(30, 5), key="plotList")],
            [
                sg.Push(), sg.Button("Set Plot", key="setPlotEdit"),
                sg.Button("Delete", key="deletePlotEdit")
            ],
            [sg.Text("_"*32)],
            [
                sg.Push(), sg.Button("Set All", key="setAllEdit"), sg.Button("Cancel", key="cancelGroupEdit"),
                sg.Button("Save", key="saveGroupEdit")]
        ]
        super().__init__(self._title, self._layout)

    def open(self):
        "Opens the home window and runs the event loop"
        while True:
            event, values = self._window.read()
            if event == sg.WIN_CLOSED:
                break
        self._window.close()
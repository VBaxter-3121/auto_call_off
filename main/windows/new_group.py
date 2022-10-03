import PySimpleGUI as sg
from windows.window import Window

class NewGroup(Window):
    """This window allows the user to enter the developer, site, and
    plot numbers that the new group will use. Once this information
    is in place, the user will be able to set the details for each
    individual plot. Once a plot has information set, the user can
    go back into that information to edit it. Finally, the user can
    delete individual plots from the list.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self):
        "Contruscts the 'New Group' window"
        self._title = "New Group"
        self._layout = [
            [sg.Text("Developer:")],
            [sg.Combo(values=[], size=(30, 1), key="developer")],
            [sg.Text("Site:")],
            [sg.Combo(values=[], size=(30, 1), key="site")],
            [sg.Text("Plots:")],
            [sg.In(size=(30, 1), key="plotInput")],
            [sg.Listbox(values=[], size=(30, 5), key="plotList")],
            [
                sg.Push(), sg.Button("Set Plot", key="setPlot"),
                sg.Button("Delete", key="deletePlot")],
            [sg.Text("_"*32)],
            [
                sg.Push(), sg.Button("Set All", key="setAll"), sg.Button("Cancel", key="cancelGroup"),
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
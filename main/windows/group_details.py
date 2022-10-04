import PySimpleGUI as sg
from windows.window import Window

class GroupDetails(Window):
    """This window allows the user to enter the developer, site, and
    plot numbers that the group will use. Once this information
    is in place, the user will be able to set the details for each
    individual plot. Once a plot has information set, the user can
    go back into that information to edit it. Finally, the user can
    delete individual plots from the list.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self):
        "Contructs the 'Group Details' window"
        self._title = "Group Details"
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
                sg.Button("Delete", key="deletePlot")
            ],
            [
                sg.Push(), sg.Button("Set All", key="setAllPlots"),
                sg.Button("Delete All", key="deleteAll")
            ],
            [sg.Text("_"*32)],
            [
                sg.Push(), sg.Button("Cancel", key="cancelGroup"),
                sg.Button("Confirm", key="confirmGroup")]
        ]

        super().__init__(self._title, self._layout)

        ## Key variables
        self._developer = self._window["developer"]
        self._site = self._window["site"]
        self._plotInput = self._window["plotInput"]
        self._plotList = self._window["plotList"]
        self._setPlot = self._window["setPlot"]
        self._deletePlot = self._window["deletePlot"]
        self._setAllPlots = self._window["setAllPlots"]
        self._deleteAll = self._window["deleteAll"]
        self._cancelGroup = self._window["cancelGroup"]
        self._confirmGroup = self._window["confirmGroup"]
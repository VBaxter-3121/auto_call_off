import PySimpleGUI as sg
from windows.window import Window

class GroupData(Window):
    """This window allows the user to enter theplot numbers that the group will use.
    Once this information is in place, the user will be able to set the data for
    each individual plot. Once a plot has information set, the user can go back into
    that information to edit it. Finally, the user can delete individual plots from
    the list.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self, groupName):
        """Contructs an instance of the 'Group Data' class
        
        Parameters:
        groupName (str): The name of the current group
        """
        self._title = groupName
        self._layout = [
            [sg.Text("Plots:")],
            [sg.In(size=(5, 1), enable_events=True, key="plotInput")],
            [sg.Listbox(values=[], size=(30, 10), key="plotList")],
            [sg.Button("Set All", size=(7, 1), disabled=True, key="setAll"), sg.Push(),
                sg.Button("Delete", size=(7, 1), disabled=True, key="deletePlot"), sg.Push(),
                sg.Button("Delete All", size=(7, 1), disabled=True, key="deleteAll")],
            [sg.Button("Cancel", size=(10, 1), key="cancelGroup"), sg.Push(),
                sg.Button("Confirm", size=(10, 1), disabled=True, key="confirmGroup")]
        ]

        super().__init__(self._title, self._layout)
        # self._window.DisableClose=True

        ## Key variables
        self._plotInput = self._window["plotInput"]
        self._plotList = self._window["plotList"]
        self._deletePlot = self._window["deletePlot"]
        self._setAll = self._window["setAll"]
        self._deleteAll = self._window["deleteAll"]
        self._cancelGroup = self._window["cancelGroup"]
        self._confirmGroup = self._window["confirmGroup"]
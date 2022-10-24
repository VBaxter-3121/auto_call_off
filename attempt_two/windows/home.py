import PySimpleGUI as sg
from windows.window import Window

class Home(Window):
    """The home window is the first window that the user will see
    upon opening the program. It contains a list showing all groups
    the user may have entered up to that point, as well as buttons
    to add a new group, edit an existing group, or start the call off
    process.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self):
        "Contructs an instance of the 'Home' class"
        self._title = "Auto Call Off"
        self._layout = [
            [sg.Text("Developer:")],
            [sg.Combo(values=[], size=(35, 1), enable_events=True, key="developer")],
            [sg.Text("Site:")],
            [sg.Combo(values=[], size=(35, 1), enable_events=True, key="site")],
            [sg.Text("Groups:")],
            [sg.Listbox(values=[], size=(35, 10), key="groupList")],
            [sg.Button("Add Group", size=(13, 1), disabled=True, key="addGroup"), sg.Push(),
                sg.Button("Delete Group", size=(13, 1), disabled=True, key="deleteGroup")],
            [sg.Button("Edit Group", size=(13, 1), disabled=True, key="editGroup"), sg.Push(),
                sg.Button("Start Call Offs", size=(13, 1), disabled=True, key="startCallOffs")]
        ]

        super().__init__(self._title, self._layout)

        ## Key variables
        self._groupList = self._window["groupList"]
        self._addGroup = self._window["addGroup"]
        self._deleteGroup = self._window["deleteGroup"]
        self._editGroup = self._window["editGroup"]
        self._startCallOffs = self._window["startCallOffs"]
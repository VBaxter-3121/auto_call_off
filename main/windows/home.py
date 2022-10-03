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
        "Constructs the 'Home' window"
        self._title = "Auto Call Off"
        self._layout = [
            [sg.Text("Groups:")],
            [sg.Listbox(values=["Testing", "Probando"], size=(41, 10), enable_events=True, key="groupList")],
            [sg.Button("Add New Group", key="addNewGroup"), sg.Button("Edit", disabled=True, key="editGroup"),
            sg.Button("Delete", disabled=True, key="deleteGroup"), sg.Button("Start Call Offs", disabled=True, key="startCallOffs")]
        ]
        super().__init__(self._title, self._layout)

    # def open(self):
    #     "Opens the home window and runs the event loop"
    #     while True:
    #         event, values = self._window.read()
    #         if event == sg.WIN_CLOSED:
    #             break
    #     self._window.close()
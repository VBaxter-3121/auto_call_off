import PySimpleGUI as sg
from windows.window import Window
from windows.group_data import GroupData
from data.job_details import jobDetails

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
            [sg.Listbox(values=[], size=(35, 10), enable_events=True, key="groupList")],
            [sg.Button("Add Group", size=(13, 1), disabled=True, key="addGroup"), sg.Push(),
                sg.Button("Delete Group", size=(13, 1), disabled=True, key="deleteGroup")],
            [sg.Button("Edit Group", size=(13, 1), disabled=True, key="editGroup"), sg.Push(),
                sg.Button("Start Call Offs", size=(13, 1), disabled=True, key="startCallOffs")]
        ]

        super().__init__(self._title, self._layout)

        ## Key variables
        self._developer = self._window["developer"]
        self._site = self._window["site"]
        self._groupList = self._window["groupList"]
        self._addGroup = self._window["addGroup"]
        self._deleteGroup = self._window["deleteGroup"]
        self._editGroup = self._window["editGroup"]
        self._startCallOffs = self._window["startCallOffs"]

        self._developer.update(values=list(map(lambda developer : developer, jobDetails.keys())))

    def read(self):
        "Handles events and values related to the home window"
        while True:
            event, values = self._window.read()

            # For debugging
            print(event)

            # Window closed
            if event == sg.WIN_CLOSED:
                break
            
            # Developer selected
            elif event == "developer":
                values["site"] = ""
                self._site.update(values=list(map(lambda site : site, jobDetails[values["developer"]].keys())))
            
            # Add Group pressed
            elif event == "addGroup":
                # Prevent identical groups being added
                if f"{values['developer']}, {values['site']}" not in self._groupList.Values:
                    # Add new group to list
                    self._groupList.Values.append(f"{values['developer']}, {values['site']}")
                    self._groupList.update(values=self._groupList.Values)
                    # Empty developer and site boxes
                    self._developer.update("")
                    self._site.update(values="")

            # Delete Group pressed
            elif event == "deleteGroup":
                # Remove group from list
                self._groupList.Values.remove(values["groupList"][0])
                self._groupList.update(values=self._groupList.Values)

            # Edit Button pressed
            elif event == "editGroup":
                groupData = GroupData(values["groupList"][0])
                groupData.read()

            self._toggleDisabled(event, values)
    
    def _toggleDisabled(self, event, values):
        "Checks if each button should be disabled or not"
        # Add Group
        if values["site"] != "" and event != "addGroup":
            self._addGroup.update(disabled=False)
        else:
            self._addGroup.update(disabled=True)

        # Delete Group/Edit Group
        if values["groupList"] != [] and event != "deleteGroup":
            self._deleteGroup.update(disabled=False)
            self._editGroup.update(disabled=False)
        else:
            self._deleteGroup.update(disabled=True)
            self._editGroup.update(disabled=True)

        # Start Call Offs
        pass
import PySimpleGUI as sg
from call_off.call_off import CallOff
from windows.window import Window
from windows.group_data import GroupData
from main.data.job_details import jobDetails
from windows.setup import setup


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

    def __init__(self, data):
        "Contructs an instance of the 'Home' class"
        self._callOffData = data
        self._title = "Auto Call Off"
        self._layout = [
            [sg.Text("Developer:"), sg.Push(), sg.Button("Set Up Pegasus", size=(13, 1), disabled=False, key="setUpPegasus")],
            [sg.Combo(values=[], size=(40, 1), enable_events=True, readonly=True, key="developer")],
            [sg.Text("Site:")],
            [sg.Combo(values=[], size=(40, 1), enable_events=True, readonly=True, key="site")],
            [sg.Text("Groups:")],
            [sg.Listbox(values=[], size=(40, 10), enable_events=True, key="groupList")],
            [sg.Button("Add Group", size=(13, 1), disabled=True, key="addGroup"), sg.Push(),
                sg.Button("Delete Group", size=(13, 1), disabled=True, key="deleteGroup")],
            [sg.Button("Edit Group", size=(13, 1), disabled=True, key="editGroup"), sg.Push(),
                sg.Button("Start Call Offs", size=(13, 1), disabled=True, key="startCallOffs")]
        ]

        super().__init__(self._title, self._layout)
        self._window.bring_to_front()

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
            # print(event)

            # Window closed
            if event == sg.WIN_CLOSED:
                return False
            
            # Developer selected
            elif event == "developer":
                values["site"] = ""
                self._site.update(values=list(map(lambda site : site, jobDetails[values["developer"]].keys())))
            
            # Add Group pressed
            elif event == "addGroup":
                # Add new group
                self._callOffData.writeGroup(f"{values['developer']}, {values['site']}")
                self._refreshList()
                # Empty developer and site boxes
                self._developer.update("")
                self._site.update(values="")

            # Delete Group pressed
            elif event == "deleteGroup":
                # Remove group
                self._callOffData.deleteGroup(values["groupList"][0].replace(" *NO DATA*", ""))
                self._refreshList()

            # Edit Button pressed
            elif event == "editGroup":
                groupData = GroupData(values["groupList"][0].replace(" *NO DATA*", ""), self._callOffData)
                self._window.disable()
                groupData.read()
                self._window.enable()
                self._window.bring_to_front()
                self._refreshList()

            elif event == "setUpPegasus":
                setup()
                self._window.bring_to_front()

            elif event == "startCallOffs":
                callOffDict = self._callOffData.readDict()
                callOff = CallOff(callOffDict)
                self._window.close()
                callOff.execute()
                break

            self._toggleDisabled(event, values)
    
    def _toggleDisabled(self, event, values):
        "Checks if each button should be disabled or not"
        # Add Group
        if (values["site"] != "" and event != "addGroup" and
        f"{values['developer']}, {values['site']}" not in
        self._callOffData.readGroups()):
            self._addGroup.update(disabled=False)
        else:
            self._addGroup.update(disabled=True)

        # Delete Group/Edit Group
        if (values["groupList"] != [] and event != "deleteGroup" and
            event != "editGroup"):
            self._deleteGroup.update(disabled=False)
            self._editGroup.update(disabled=False)
        else:
            self._deleteGroup.update(disabled=True)
            self._editGroup.update(disabled=True)

        # Start Call Offs
        ready = True
        for groupName in self._groupList.Values:
            if groupName[-1] == "*":
                ready = False
                break
        if ready:
            self._startCallOffs.update(disabled=False)
        else:
            self._startCallOffs.update(disabled=True)

    def _refreshList(self):
        "Refreshed the groups list"
        currentGroups = self._markEmptyGroups()
        self._groupList.update(values=currentGroups)

    def _markEmptyGroups(self):
        "Checks if each group in list is empty"
        currentGroups = self._callOffData.readGroups()
        for group in currentGroups:
            isEmpty = self._callOffData.groupEmpty(group)
            if isEmpty:
                groupIndex = currentGroups.index(group)
                currentGroups[groupIndex] = f"{group} *NO DATA*"
        return currentGroups
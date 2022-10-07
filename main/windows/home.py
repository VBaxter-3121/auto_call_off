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
            [sg.Listbox(values=[], size=(45, 10), key="groupList")],
            [
                sg.Button("Add New Group", size=(12, 1), key="addNewGroup"), sg.Button("Edit Group", size=(12, 1), disabled=True, key="editGroup"),
                sg.Button("Delete Group", size=(12, 1), disabled=True, key="deleteGroup")
            ],
            [sg.Push(), sg.Button("Start Call Offs", size=(38, 1), disabled=True, key="startCallOffs"), sg.Push()]
        ]

        super().__init__(self._title, self._layout)

        ## Key variables
        self._groupList = self._window["groupList"]
        self._addNewGroup = self._window["addNewGroup"]
        self._editGroup = self._window["editGroup"]
        self._deleteGroup = self._window["deleteGroup"]
        self._startCallOffs = self._window["startCallOffs"]

        self.toggleButtons()
    ##########

    def toggleButtons(self):
        """Checks if the edit, delete and start buttons should be enabled
        and sets them appropriately"""
        if self._groupList.Values != []:
            self._editGroup.Update(disabled=False)
            self._deleteGroup.Update(disabled=False)
            self._startCallOffs.Update(disabled=False)
        else:
            self._editGroup.Update(disabled=True)
            self._deleteGroup.Update(disabled=True)
            self._startCallOffs.Update(disabled=True)
    ##########

    def deleteGroup(self):
        "Deletes the currently selected group"
        try:
            groupListItems = self._groupList.Values
            groupListItems.remove(self._groupList.get()[0])
            self._groupList.Update(values=groupListItems)
        except:
            pass
    ##########

    def getSelectedGroup(self):
        "Returns the currently selected group"
        try:
            return self._groupList.get()[0]
        except:
            pass
    ##########

    def updateList(self, groupsList):
        "Refreshes list with data from allGroupsDict"
        for group in groupsList:
            self._groupList.Values.append(group)
            self._groupList.Update(self._groupList.Values)
from loops.loop import Loop

class HomeLoop(Loop):
    """The home loop keeps the home window open until it is either
    closed or the user opens a group window"""

    def __init__(self, window):
        "Prepares the home loop to run"
        super().__init__(window)
        self._groupList = self._window["groupList"]
        self._addNewGroup = self._window["addNewGroup"]
        self._editGroup = self._window["editGroup"]
        self._deleteGroup = self._window["deleteGroup"]
        self._startCallOffs = self._window["startCallOffs"]
        self.buttonsEnabled()

    def _listenLoop(self, event, values):
        """Checks for events and calls appropriate functions. Also runs
        logic to enable/disable buttons etc."""

        # Events

        # If delete button is pressed, remove the currently selected
        # group from the list
        if event == "deleteGroup":
            groupListItems = self._groupList.Values
            groupListItems.remove(self._groupList.get()[0])
            self._groupList.Update(values=groupListItems)

        # Enable/disable elements

        # Enable/disable edit, delete and start call off buttons based
        # on if there are groups in the listbox
        
        self.buttonsEnabled()

    def buttonsEnabled(self):
        if self._groupList.Values != []:
            self._editGroup.Update(disabled=False)
            self._deleteGroup.Update(disabled=False)
            self._startCallOffs.Update(disabled=False)
        else:
            self._editGroup.Update(disabled=True)
            self._deleteGroup.Update(disabled=True)
            self._startCallOffs.Update(disabled=True)
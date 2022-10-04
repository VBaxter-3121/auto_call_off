import PySimpleGUI as sg

from windows.home import Home
from windows.group_details import GroupDetails
from windows.plot_details import PlotDetails

class Organiser():
    """Controls which windows are open, how they behave and how they store
    their data"""

    def __init__(self, data):
        """Contructs the organiser class
        
        Attributes:
        data: An instance of the Data class
        """
        self._openHome()
        self._data = data
        self._running = True
        self._openPlot("1")

    def startProgram(self):
        "Begins a loop to read window events"
        while self._running:
            event, values = self._currentWindow.read()

            ## For testing ##
            print(event)

            # Run through events specific to each window
            if self._currentWindow.Title == "Auto Call Off":
                self._listenHome(event, values)

            elif self._currentWindow.Title == "Add New Group":
                self._listenNew(event, values)

            elif self._currentWindow.Title[0:4] == "Plot":
                self._listenDetails(event, values)

            if event == sg.WIN_CLOSED:
                self._running = False

    ## Window opening methods

    def _openHome(self):
        "Creates a new instance of Home and makes that the current window"
        self._home = Home()
        self._currentWindow = self._home.getWindow()

    def _openGroup(self):
        "Creates a new instance of GroupDetails and makes that the current window"
        self._new = GroupDetails()
        self._currentWindow = self._new.getWindow()
    
    def _openPlot(self, plotNumber):
        """Creates a new instance of PlotDetails and makes that the current window
        
        Parameters:
        plotNumber: A string containing the current plot number
        """
        self._details = PlotDetails(plotNumber)
        self._currentWindow = self._details.getWindow()

    ## Event listening methods

    def _listenHome(self, event, values):
        """Contains events specific to the home window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event: An event from self._currentWindow.read()
        values: A list of values from self._currentWindow.read()
        """
        # Add a new group
        if event == "addNewGroup":
            self._currentWindow.close()
            self._openNew()

        elif event == "editGroup":
            ""
            ## Waiting on data to see how this will work ##
            
            ## For testing ##
            self._currentWindow.close()
            self._openNew()

        # Delete the currently selected group
        elif event == "deleteGroup":
            self._home.deleteGroup()

        elif event == "startCallOffs":
            ""
            ## Waiting on data to see how this will work ##

            ## For testing ##
            self._currentWindow.close()
            self._openDetails("5")

        elif event == sg.WIN_CLOSED:
            self._running = False

        # If the home window is still open, run checks
        if self._currentWindow.Title == "Auto Call Off" and self._running == True:
            # Check if the edit, delete and start buttons should be enabled
            # and set them appropriately
            self._home.toggleButtons()

    def _listenNew(self, event, values):
        """Contains events specific to the new group window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event: An event from self._currentWindow.read()
        values: A list of values from self._currentWindow.read()
        """

    def _listenDetails(self, event, values):
        """Contains events specific to the plot details window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event: An event from self._currentWindow.read()
        values: A list of values from self._currentWindow.read()
        """
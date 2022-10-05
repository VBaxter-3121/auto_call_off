from locale import delocalize
from winreg import DeleteValue
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

    def startProgram(self):
        "Begins a loop to read window events"
        while self._running:
            event, values = self._currentWindow.read()

            ## For testing ##
            print(event)

            # Run through events specific to each window
            if self._currentWindow.Title == "Auto Call Off":
                self._listenHome(event, values)

            elif self._currentWindow.Title == "Group Details":
                self._listenGroup(event, values)

            elif self._currentWindow.Title[0:4] == "Plot":
                self._listenPlot(event, values)

            if event == sg.WIN_CLOSED:
                if self._currentWindow.Title == "Auto Call Off":
                    self._running = False
                elif self._currentWindow.Title == "Group Details":
                    self._openHome()
                elif self._currentWindow.Title[0:4] == "Plot":
                    self._openGroup()

    ## Window opening methods

    def _openHome(self):
        "Creates a new instance of Home and makes that the current window"
        self._home = Home()
        self._currentWindow = self._home.getWindow()

    def _openGroup(self):
        "Creates a new instance of GroupDetails and makes that the current window"
        self._group = GroupDetails(self._data)
        self._currentWindow = self._group.getWindow()
    
    def _openPlot(self, plotNumber):
        """Creates a new instance of PlotDetails and makes that the current window
        
        Parameters:
        plotNumber: A string containing the current plot number
        """
        self._plot = PlotDetails(plotNumber)
        self._currentWindow = self._plot.getWindow()

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
            self._openGroup()

        elif event == "editGroup":
            ""
            ## Waiting on data to see how this will work ##

        # Delete the currently selected group
        elif event == "deleteGroup":
            self._home.deleteGroup()

        elif event == "startCallOffs":
            ""
            ## Waiting on data to see how this will work ##

        # If the home window is still open, run checks
        if self._currentWindow.Title == "Auto Call Off" and event != sg.WIN_CLOSED:
            self._home.toggleButtons()

    def _listenGroup(self, event, values):
        """Contains events specific to the group details window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event: An event from self._currentWindow.read()
        values: A list of values from self._currentWindow.read()
        """

        if event == "developer":
            self._group.populateSites(values["developer"])

        elif event == "plotInput-":
            self._group.addPlot(values["plotInput"])

        elif event == "deletePlot":
            self._group.deletePlot()

        elif event == "deleteAll":
            self._group.deleteAll()

        elif event == "cancelGroup":
            self._currentWindow.close()
            # Will need to add code to clear any dictionaries in progress
            # for this group

        # If the group window is still open, run checks
        if self._currentWindow.Title == "Group Details" and event != sg.WIN_CLOSED and event != "cancelGroup":
            self._group.toggleButtons()


    def _listenPlot(self, event, values):
        """Contains events specific to the plot details window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event: An event from self._currentWindow.read()
        values: A list of values from self._currentWindow.read()
        """
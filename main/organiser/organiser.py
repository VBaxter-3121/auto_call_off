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
        self._breakPlotLoop = False
    ##########

    def startProgram(self):
        "Begins a loop to read window events"
        while True:
            event, values = self._homeWindow.read()

            ## For testing ##
            print(event)

            self._listenHome(event, values)

            if event == sg.WIN_CLOSED:
                break
    ##########

    ########## Window Opening Methods ##########

    def _openHome(self):
        "Creates a new instance of Home"
        self._home = Home()
        self._homeWindow = self._home.getWindow()
    ##########

    def _openGroup(self):
        "Creates a new instance of GroupDetails"
        self._group = GroupDetails(self._data)
        self._groupWindow = self._group.getWindow()
        self._homeWindow.disable()
        while True:
            event, values = self._groupWindow.read()

            ## For testing ##
            print(event)

            self._listenGroup(event, values)

            if event == sg.WIN_CLOSED:
                self._homeWindow.bring_to_front()
                break
        self._homeWindow.enable()
    ##########
    
    def _openPlot(self, developer, site, plot):
        """Creates a new instance of PlotDetails
        
        Parameters:
        plot: A string containing the current plot number
        """
        self._plot = PlotDetails(developer, site, plot)
        self._plotWindow = self._plot.getWindow()
        self._groupWindow.disable()
        while True:
            event, values = self._plotWindow.read()

            ## For testing ##
            print(event)

            self._listenPlot(event, values)

            if event == sg.WIN_CLOSED:
                self._homeWindow.bring_to_front()
                self._groupWindow.bring_to_front()
                break
        self._groupWindow.enable()
    ##########

    ########## Listening Methods ##########

    def _listenHome(self, event, values):
        """Contains events specific to the home window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event: An event from self._homeWindow.read()
        values: A list of values from self._homeWindow.read()
        """
        # Add a new group
        if event == "addNewGroup":
            self._openGroup()

        # Edit an existing group
        elif event == "editGroup":
            group = self._home.getSelectedGroup()
            if group != None:
                self._openGroup()

        # Delete the currently selected group
        elif event == "deleteGroup":
            self._home.deleteGroup()

        # Pass user input to call off functions
        elif event == "startCallOffs":
            ""

        if event != sg.WIN_CLOSED:
            self._home.toggleButtons()
    ##########

    def _listenGroup(self, event, values):
        """Contains events specific to the group details window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event: An event from self._groupWindow.read()
        values: A list of values from self._groupWindow.read()
        """

        if event == "developer":
            self._group.populateSites(values["developer"])
            values["site"] = ""

        elif event == "plotInput-":
            self._group.addPlot()

        elif event == "setPlot":
            try:
                selectedPlot = self._group.getSelectedPlot()
                self._openPlot(values["developer"], values["site"], selectedPlot)
            except:
                pass

        elif event == "setAll":
            self._breakPlotLoop = False
            for plot in self._group.getPlotList():
                if self._breakPlotLoop == False:
                    self._openPlot(values["developer"], values["site"], plot)
                else:
                    break

        elif event == "deletePlot":
            self._group.deletePlot()

        elif event == "deleteAll":
            self._group.deleteAll()

        elif event == "cancelGroup":
            self._group.deleteAll()
            self._groupWindow.close()

        elif event =="confirmGroup":
            self._group.confirmGroup()

        if event != sg.WIN_CLOSED and event != "cancelGroup" and event != "confirmGroup":
            self._group.toggleButtons(values["developer"], values["site"])
    ##########

    def _listenPlot(self, event, values):
        """Contains events specific to the plot details window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event: An event from self._plotWindow.read()
        values: A list of values from self._plotWindow.read()
        """

        if event =="saveDetails":
            self._plot.saveDetails()
            self._plot.clearChecks()
        
        elif event == "cancelPlot":
            self._breakPlotLoop = True
            self._plotWindow.close()

        elif event == "deleteDetails":
            self._plot.deleteDetails()

        elif event == "editDetails":
            self._plot.clearDetails()
            self._plot.editDetails()

        elif event == "clearDetails":
            self._plot.clearDetails()

        elif event == "cancelPlot":
            self._plotWindow.close()

        elif event == "confirmPlot":
            detailsList = self._plot.confirmPlot()
            plot = detailsList[0][2]
            self._group.markPlot(plot)
            counter = 0
            for details in detailsList:
                self._data.addPlot(details, counter)
                counter += 1
            self._plotWindow.close()

        if event != sg.WIN_CLOSED and event != "cancelPlot" and event != "confirmPlot":
            self._plot.toggleButtons()
    ##########
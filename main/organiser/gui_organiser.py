import PySimpleGUI as sg

from windows.home import Home
from windows.group_details import GroupDetails
from windows.plot_details import PlotDetails

class GUIOrganiser():
    """Controls which windows are open, how they behave and how they store
    their data"""

    def __init__(self, data):
        """Contructs an instancethe GUIorganiser class
        
        Attributes:
        data (Data): An instance of the Data class
        breakPlotLoop (bool): Used to interrupt the "Set all plots" loop
        """
        self._openHome()
        self._data = data
        self._breakPlotLoop = False

    def startProgram(self):
        "Begins a loop to read window events"
        while True:
            event, values = self._homeWindow.read()

            ## For testing ##
            print(event)

            self._listenHome(event, values)

            if event == sg.WIN_CLOSED:
                break

    def _openHome(self):
        "Creates a new instance of Home"
        self._home = Home()
        self._homeWindow = self._home.getWindow()

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
    
    def _openPlot(self, developer, site, plot):
        """Creates a new instance of PlotDetails
        
        Parameters:
        developer (str): The name of the current developer
        site (str): The name of the current site
        plot (str): The current plot number
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


    def _listenHome(self, event, values):
        """Contains events specific to the home window, and runs other logic checks
        to enable or disable window elements
        
        Parameters:
        event (str): The current event
        values (list): The current values
        """
        # Add a new group
        if event == "addNewGroup":
            self._openGroup()

        # Delete the currently selected group
        elif event == "deleteGroup":
            self._home.deleteGroup()

        # Pass user input to call off functions
        elif event == "startCallOffs":
            self._homeWindow.close()

        if event != sg.WIN_CLOSED and event != "startCallOffs":
            self._home.toggleButtons()

    def _listenGroup(self, event, values):
        """Contains events specific to the group details window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event (str): The current event
        values (list): The current values
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
            homeList = self._data.getAllGroups()
            self._home.updateList(homeList)

        if event != sg.WIN_CLOSED and event != "cancelGroup" and event != "confirmGroup":
            self._group.toggleButtons(values["developer"], values["site"])

    def _listenPlot(self, event, values):
        """Contains events specific to the plot details window, and runs other logic checks
        to enable or disable window elements
        
        Attributes:
        event (str): The current event
        values (list): The current values
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
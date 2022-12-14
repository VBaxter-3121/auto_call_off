from optparse import Values
import PySimpleGUI as sg
from windows.window import Window

class GroupDetails(Window):
    """This window allows the user to enter the developer, site, and
    plot numbers that the group will use. Once this information
    is in place, the user will be able to set the details for each
    individual plot. Once a plot has information set, the user can
    go back into that information to edit it. Finally, the user can
    delete individual plots from the list.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self, data):
        """Contructs an instance of the 'Group Details' class
        
        Parameters:
        data: An instance of the Data class
        """
        self._title = "Group Details"
        self._layout = [
            [sg.Text("Developer:")],
            [sg.Combo(values=[], size=(30, 1), enable_events=True, key="developer")],
            [sg.Text("Site:")],
            [sg.Combo(values=[], size=(30, 1), enable_events=True, key="site")],
            [sg.Text("Plots:")],
            [sg.In(size=(30, 1), enable_events=True, key="plotInput")],
            [sg.Listbox(values=[], size=(30, 5), key="plotList")],
            [
                sg.Button("Set Plot", size=(12, 1), disabled=True, key="setPlot"), sg.Push(),
                sg.Button("Delete", size=(12, 1), disabled=True, key="deletePlot")
            ],
            [
                sg.Button("Set All", size=(12, 1), disabled=True, key="setAll"), sg.Push(),
                sg.Button("Delete All", size=(12, 1), disabled=True, key="deleteAll")
            ],
            [sg.Text("_"*32)],
            [
                sg.Button("Cancel", size=(10, 1), key="cancelGroup"), sg.Push(),
                sg.Button("Confirm", size=(10, 1), disabled=True, key="confirmGroup")]
        ]

        super().__init__(self._title, self._layout)
        self._window.DisableClose=True

        ## Key variables
        self._developer = self._window["developer"]
        self._site = self._window["site"]
        self._plotInput = self._window["plotInput"]
        self._plotList = self._window["plotList"]
        self._setPlot = self._window["setPlot"]
        self._deletePlot = self._window["deletePlot"]
        self._setAll = self._window["setAll"]
        self._deleteAll = self._window["deleteAll"]
        self._cancelGroup = self._window["cancelGroup"]
        self._confirmGroup = self._window["confirmGroup"]

        ## Other
        self._data = data
        self._plotListItems = []

        self._populateDevelopers()
        self._plotInput.bind("<Return>", "-")
    ##########

    def _populateDevelopers(self):
        "Populates the developer options"
        self._developer.update(values=self._data.getDevelopers())
    ##########

    def populateSites(self, developer):
        "Populates the site options based on the developer"
        self._site.update(values=self._data.getSites(developer))
    ##########

    def toggleButtons(self, developer, site):
        """Checks if the set, set all, delete, delete all and confirm
        buttons should be enabled and sets appropriately"""
        # Set, delete, set all and delete all buttons
        if self._plotList.Values != [] and developer != "" and site != "":
            print(developer)
            print(site)
            self._setPlot.Update(disabled=False)
            self._deletePlot.Update(disabled=False)
            self._setAll.Update(disabled=False)
            self._deleteAll.Update(disabled=False)
            self._plotsConfirmed = 0
            self._plotsNotConfirmed = 0
            for item in self._plotList.Values:
                if item[-1] == "*":
                    self._plotsConfirmed += 1
                else:
                    self._plotsNotConfirmed += 1

            if self._plotsConfirmed > 0:
                self._confirmGroup.Update(disabled=False)
            else:
                self._confirmGroup.Update(disabled=True)
        else:
            self._setPlot.Update(disabled=True)
            self._deletePlot.Update(disabled=True)
            self._setAll.Update(disabled=True)
            self._deleteAll.Update(disabled=True)        
    ##########

    def addPlot(self):
        """Adds the number in the plot input to the plot list, and
        clears the input box"""
        if self._plotInput.get() != "":
            self._plotList.Values.append(self._plotInput.get())
            self._plotList.Update(self._plotList.Values)
            self._plotInput.Update("")
    ##########

    def markPlot(self, plot):
        "Adds a marker next to a plot on the list that has been confirmed"
        counter = 0
        for item in self._plotList.Values:
            if item == plot:
                self._plotList.Values[counter] = item + " *"
            self._plotList.Update(self._plotList.Values)
            counter += 1
    ##########

    def deletePlot(self):
        "Deletes the currently selected plot"
        try:
            plotListItems = self._plotList.Values
            plotListItems.remove(self._plotList.get()[0])
            self._plotList.Update(values=plotListItems)
            self._data.deleteFromCurrent([self._plotList.get()[0]])
        except:
            pass
    ##########

    def deleteAll(self):
        "Deletes all plots"
        self._plotList.Update(values=[])
        self._data.deleteFromCurrent(self._plotList.Values)
    ##########

    def getSelectedPlot(self):
        "Returns selected plot"
        plot = self._plotList.get()[0]
        if plot[-1:] == "*":
            plot = plot[0:-2]
        return plot
    ##########

    def getPlotList(self):
        "Returns a list of all plots"
        plotListReturn = []
        for plot in self._plotList.Values:
            if plot[-1:] == "*":
                plotListReturn.append(plot[0:-2])
            else:
                plotListReturn.append(plot)
        
        return plotListReturn
    ##########

    def confirmGroup(self):
        """Checks if all plots have been set, and then passes their
        information to Data.allGroupsDict"""
        validConfirm = False
        for plot in self._plotList.Values:
            if plot[-1:] != "*":
                break
            else:
                validConfirm = True
        if validConfirm == True:
            self._data.addGroup()
            self._window.close()
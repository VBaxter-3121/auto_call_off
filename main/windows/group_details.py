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
        "Contructs the 'Group Details' window"
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
        self._plotInfo = []

        self._populateDevelopers()
        self._plotInput.bind("<Return>", "-")

    def _populateDevelopers(self):
        "Populates the developer options"
        self._developer.update(values=self._data.getDevelopers())

    def populateSites(self, developer):
        "Populates the site options based on the developer"
        self._site.update(values=self._data.getSites(developer))

    def toggleButtons(self):
        """Checks if the set, set all, delete, delete all and confirm
        buttons should be enabled and set appropriately"""
        # Set, delete, set all and delete all buttons
        if self._plotList.Values != []:
            self._setPlot.Update(disabled=False)
            self._deletePlot.Update(disabled=False)
            self._setAll.Update(disabled=False)
            self._deleteAll.Update(disabled=False)
        else:
            self._setPlot.Update(disabled=True)
            self._deletePlot.Update(disabled=True)
            self._setAll.Update(disabled=True)
            self._deleteAll.Update(disabled=True)

        # Confirm button
        
    def addPlot(self, plot):
        """Adds the number in the plot input to the plot list, and
        clears the input box"""
        self._plotListItems.append(plot)
        self._plotList.Update(values=self._plotListItems)
        self._plotInput.Update("")

    def setPlot(self):
        "Sets the details for the selected plot"
        

    def deletePlot(self):
        "Deletes the selected plot"
        try:
            plot = self._plotList.get()[0]
            self._plotListItems.remove(plot)
            self._plotList.Update(values=self._plotListItems)
        except:
            pass

    def setAll(self):
        "Sets the details for all plots in order from beginning to end"


    def deleteAll(self):
        "Deletes all plots in list"
        self._plotListItems = []
        self._plotList.Update(values=self._plotListItems)
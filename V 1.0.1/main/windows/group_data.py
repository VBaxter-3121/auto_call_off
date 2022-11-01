import PySimpleGUI as sg
from windows.window import Window
from windows.plot_data import PlotData

class GroupData(Window):
    """This window allows the user to enter the plot numbers that the group will use.
    Once this information is in place, the user will be able to set the data for
    each individual plot. Once a plot has information set, the user can go back into
    that information to edit it. Finally, the user can delete individual plots from
    the list.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self, groupName, data):
        """Contructs an instance of the 'Group Data' class
        
        Parameters:
        title (str): The name of the current group
        """
        self._callOffData = data
        self._title = groupName
        plots = self._callOffData.readPlots(groupName)
        self._layout = [
            [sg.Text(groupName)],
            [sg.In(size=(5, 1), enable_events=True, key="plotInput"), sg.Text("Type plot number and press 'enter'")],
            [sg.Text("Plots:")],
            [sg.Listbox(values=plots, size=(33, 10), enable_events=True, key="plotList")],
            [sg.Button("Set Plots", size=(8, 1), disabled=True, key="setPlots"), sg.Push(),
                sg.Button("Delete", size=(8, 1), disabled=True, key="deletePlot"), sg.Push(),
                sg.Button("Delete All", size=(8, 1), disabled=True, key="deleteAll")],
            [sg.Button("Back", size=(11, 1), key="backGroup"), sg.Push(),
                sg.Button("Confirm", size=(11, 1), disabled=True, key="confirmGroup")]
        ]

        super().__init__(self._title, self._layout)
        self._window.DisableClose=True

        ## Key variables
        self._plotInput = self._window["plotInput"]
        self._plotList = self._window["plotList"]
        self._setPlots = self._window["setPlots"]
        self._deletePlot = self._window["deletePlot"]
        self._deleteAll = self._window["deleteAll"]
        self._backGroup = self._window["backGroup"]
        self._confirmGroup = self._window["confirmGroup"]

        # Allow the enter key to add a plot number to the list
        self._plotInput.bind("<Return>", "Add")
        self._toggleDisabled(None, None)

    def read(self):
        "Handles events and values related to the group data window"
        while True:
            event, values = self._window.read()

            # For dubugging
            # print(event)

            # Window closed
            if event == sg.WIN_CLOSED or event == "backGroup":
                break

            # Plot number added
            elif event == "plotInputAdd":
                if values["plotInput"] not in self._callOffData.readPlots(self._title):
                    # Add new plot number to list
                    if len(values["plotInput"]) <= 3:
                        try:
                            self._callOffData.writePlot(self._title, str(int(values["plotInput"])))
                            self._plotList.update(values=self._callOffData.readPlots(self._title))
                        except:
                            pass
                    # Empty plot number input box
                    self._plotInput.update("")

            # Set Plots pressed
            elif event == "setPlots":
                plotData = PlotData(self._title, self._plotList.Values, self._callOffData)
                self._window.disable()
                closeSelf = plotData.read()
                self._window.enable()
                self._window.bring_to_front()
                if closeSelf:
                    self._window.close()
                    break

            # Delete Plot pressed
            elif event == "deletePlot":
                self._callOffData.deletePlot(self._title, values["plotList"][0])
                self._plotList.update(values=self._callOffData.readPlots(self._title))

            # Delete All pressed
            elif event == "deleteAll":
                for plot in self._plotList.Values:
                    self._callOffData.deletePlot(self._title, plot)
                    self._plotList.update(values=self._callOffData.readPlots(self._title))

            self._toggleDisabled(event, values)
        
        self._window.close()

    def _toggleDisabled(self, event, values):
        "Checks if each button should be disabled or not"

        # Set Plots
        if self._callOffData.readPlots(self._title) != []:
            self._setPlots.update(disabled=False)
        else:
            self._setPlots.update(disabled=True)

        # Delete Plot
        if (self._callOffData.readPlots(self._title) != [] and
            event != "deletePlot" and event != "deleteAll"):
            try:
                if values["plotList"][0] != []:
                    self._deletePlot.update(disabled=False)
            except:
                pass
        else:
            self._deletePlot.update(disabled=True)

        # Delete All
        if (self._callOffData.readPlots(self._title) != [] and
            event != "deleteAll"):
            self._deleteAll.update(disabled=False)
        else:
            self._deleteAll.update(disabled=True)

        # Confirm
        pass
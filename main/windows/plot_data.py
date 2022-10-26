from tokenize import group
import PySimpleGUI as sg
from windows.window import Window
from windows.warning import Warning
from data.job_details import jobDetails

class PlotData(Window):
    """This window allows the user to enter the call off stages, date,
    time and notes for individual plots. The information can be applied
    to all call off stages, or, in the event that different stages
    require different notes, or even dates/times, this information be be
    applied only to certain stages. In this case, a list of different
    groups of stages will be displayed, allowing the user to go back into
    each one and edit the information. Finally, the user can simply clear
    all detials from the plot and start again. When the information is
    correct, the user can save the data.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self, title, plots, data):
        """Contructs an instance of the 'PlotData' class
                
        Parameters:
        groupName (str): The name of the current group
        """
        self._callOffData = data
        self._title = title
        self._plots = plots
        self._currentPlotIndex = 0
        self._stages = [
            "GUTTER KIT", "DOWNPIPE KIT", "GAS KIT",
            "1ST FIX KIT", "SOILS KIT", "MID FIX", "HEATING & BATH",
            "FIX 2", "SANI", "FIX 3", "FINALS", "FIX 4"
        ]
        if len(self._plots) > 1:
            self._multiplePlots = False
        else:
            self._multiplePlots = True
        self._layout = [
            [sg.Push(), sg.Button("Prev", size=(5, 1), disabled=True, key="prevButton"), 
                sg.Text(f"Plot {self._plots[self._currentPlotIndex]}", key="plotNumber"),
                sg.Button("Next", size=(5, 1), disabled=self._multiplePlots, key="nextButton"), sg.Push()],
            [sg.Column([
                    [sg.Text("Call Off Stages:")],
                    [sg.Checkbox("Gutter Kit                ", default=False, enable_events=True, key="gutter")],
                    [sg.Checkbox("Downpipe Kit         ", default=False, enable_events=True, key="downpipe")],
                    [sg.Checkbox("Gas Kit                 ", default=False, enable_events=True, key="gasKit")],
                    [sg.Checkbox("1st Fix Kit             ", default=False, enable_events=True, key="1stFixKit")],
                    [sg.Checkbox("Soils Kit                ", default=False, enable_events=True, key="soilsKit")],
                    [sg.Checkbox("Shower Tray/Mid Fix", size=(16, 1), default=False, enable_events=True, key="midFix")],
                    [sg.Checkbox("Heating & Bath       ", default=False, enable_events=True, key="heatAndBath")],
                    [sg.Checkbox("Fix 2                     ", default=False, enable_events=True, key="fix2")],
                    [sg.Checkbox("Sani                      ", default=False, enable_events=True, key="sani")],
                    [sg.Checkbox("Fix 3                     ", default=False, enable_events=True, key="fix3")],
                    [sg.Checkbox("Finals                   ", default=False, enable_events=True, key="finals")],
                    [sg.Checkbox("Fix 4                     ", default=False, enable_events=True, key="fix4")],
                    [sg.Button("Clear Checkboxes", size=(15, 1), key="clearBoxes")]
            ]),
            sg.VSeparator(),
            sg.Column([
                    [sg.Text("Date:")],
                    [sg.In(size=(10, 1), enable_events=True, key="date"), sg.CalendarButton("📅",
                        close_when_date_chosen=True, target="date", no_titlebar=False,
                        format=("%d/%m/%Y"), size=(3, 1), key="calendar")],
                    [sg.Text("Time:")],
                    [sg.In(size=(10, 1), key="time")],
                    [sg.Text("Notes:")],
                    [sg.In(size=(19, 2), key="notes")],
                    [sg.Button("Save Data", size=(8, 1), disabled=True, key="saveData"),
                        sg.Button("Clear Data", size=(8, 1), key="clearData")],
                    [sg.Listbox(values=[], size=(19, 11), enable_events=True, key="dataList")],
                    [sg.Button("Delete", size=(18, 1), disabled=True, key="deleteData")]
            ])
            ],
            [sg.Push(), sg.Button("Cancel", size=(14, 1), key="cancelPlots"),
                sg.Button("Confirm", size=(14, 1), key="confirmPlots"), sg.Push()]
        ]

        super().__init__(self._title, self._layout)
        # self._window.DisableClose=True

        ## Key variables
        # Checkboxes
        self._gutter = self._window["gutter"]
        self._downpipe = self._window["downpipe"]
        self._gasKit = self._window["gasKit"]
        self._1stFixKit = self._window["1stFixKit"]
        self._soilsKit = self._window["soilsKit"]
        self._midFix = self._window["midFix"]
        self._heatAndBath = self._window["heatAndBath"]
        self._fix2 = self._window["fix2"]
        self._sani = self._window["sani"]
        self._fix3 = self._window["fix3"]
        self._finals = self._window["finals"]
        self._fix4 = self._window["fix4"]
        self._checkboxes = [
            self._gutter, self._downpipe,
            self._gasKit, self._1stFixKit, self._soilsKit,
            self._midFix, self._heatAndBath, self._fix2,
            self._sani, self._fix3, self._finals, self._fix4
        ]
        # Others
        self._prevButton = self._window["prevButton"]
        self._plotNumber = self._window["plotNumber"]
        self._nextButton = self._window["nextButton"]
        self._clearBoxes = self._window["clearBoxes"]
        self._date = self._window["date"]
        self._calendar = self._window["calendar"]
        self._time = self._window["time"]
        self._notes = self._window["notes"]
        self._saveData = self._window["saveData"]
        self._clearData = self._window["clearData"]
        self._dataList = self._window["dataList"]
        self._deleteData = self._window["deleteData"]
        self._cancelPlots = self._window["cancelPlots"]
        self._confirmPlots = self._window["confirmPlots"]

    def read(self):
        "Handles events and values related to the plot data window"
        self._updateDataList()
        while True:
            event, values = self._window.read()

            # For debugging
            print(event)

            # Window closed
            if event == sg.WIN_CLOSED:
                self._window.close()
                break

            elif event == "cancelPlots":

                self._window.close()
                break

            # Prev pressed
            elif event == "prevButton":
                self._currentPlotIndex -= 1
                self._plotNumber.update(f"Plot {self._plots[self._currentPlotIndex]}")
                self._updateDataList()

            # Next pressed
            elif event == "nextButton":
                self._currentPlotIndex += 1
                self._plotNumber.update(f"Plot {self._plots[self._currentPlotIndex]}")
                self._updateDataList()

            # Save Data pressed
            elif event == "saveData":
                dataSet = self._makeDataSet()
                self._callOffData.writeDataSet(self._title,
                    self._plots[self._currentPlotIndex], dataSet)
                self._updateDataList()
                # self._dataList.update(values=list(map(lambda list : f"{list[3][0]} etc.",
                #     self._callOffData.readDataSets(self._title, self._plots[self._currentPlotIndex]))))

            # Delete Data pressed
            elif event == "deleteData":
                index = self._dataList.Values.index(values["dataList"][0])
                self._callOffData.deleteDataSet(self._title, self._plots[self._currentPlotIndex], index)
                self._updateDataList()
                # self._dataList.update(values=list(map(lambda list : f"{list[3][0]} etc.",
                #     self._callOffData.readDataSets(self._title, self._plots[self._currentPlotIndex]))))

            # Confirm pressed
            elif event == "confirmPlots":
                indices = (index for index, item in
                    enumerate(list(map(
                        lambda plot : self._callOffData.readDataSets(self._title, plot), self._plots))) if item == [])
                emptyList = list(map(lambda index : self._plots[index], indices))
                print(emptyList)
                if emptyList == []:
                    self._window.close()
                    break
                else:
                    warning = Warning(emptyList)
                    userResponse = warning.read()
                    if userResponse == "cancel":
                        pass
                    elif userResponse == "continue":
                        self._callOffData.trimPlots(self._title,
                            emptyList)
                        self._window.close()
                        break

            elif event == "clearBoxes":
                for box in self._checkboxes:
                    box.update(False)

            elif event == "clearData":
                self._date.update("")
                self._time.update("")
                self._notes.update("")

            self._toggleDisabled(event, values)

            # Update data depending on current plot here

    def _toggleDisabled(self, event, values):
        "Checks if each button should be disabled or not"

        # Prev Plot
        if self._currentPlotIndex != 0:
            self._prevButton.update(disabled=False)
        else:
            self._prevButton.update(disabled=True)

        # Next Plot
        if self._currentPlotIndex != len(self._plots) - 1:
            self._nextButton.update(disabled=False)
        else:
            self._nextButton.update(disabled=True)

        # Save Data
        if (True in list(map(lambda checkbox : checkbox.get(), self._checkboxes)) and
            self._date.get() != ""):
            self._saveData.update(disabled=False)
        else:
            self._saveData.update(disabled=True)
        
        # Delete Data
        if (self._callOffData.readDataSets(self._title, self._plots[self._currentPlotIndex]) != [] and
            event != "deleteData"):
            try:
                if values["dataList"][0] != []:
                    self._deleteData.update(disabled=False)
            except:
                pass
        else:
            self._deleteData.update(disabled=True)

    def _makeDataSet(self):
        "Returns a list of values used for the call off"
        developer = self._title.split(", ")[0]
        site = self._title.split(", ")[1]
        plotNumber = self._plots[self._currentPlotIndex]
        requiredStages = self._getStages()
        date = self._date.get()
        time = self._time.get()
        manager = jobDetails[developer][site][1]
        notes = self._notes.get()
        return [developer, site, plotNumber, requiredStages, date, time, manager, notes]
        
    def _getStages(self):
        "Returns a list of requried stages for call off"
        # Check the below link for explanation (answer by Tomerikoo)
        # https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
        indices = (index for index, item in
            enumerate(list(map(lambda checkbox : checkbox.get(), self._checkboxes))) if item == True)
        return list(map(lambda index : self._stages[index], indices))

    def _updateDataList(self):
        "Updates the data list"
        self._dataList.update(values=list(map(lambda list : f"{list[3][0]} etc.",
                self._callOffData.readDataSets(self._title, self._plots[self._currentPlotIndex]))))
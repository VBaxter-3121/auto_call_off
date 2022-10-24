import PySimpleGUI as sg
from windows.window import Window

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

    def __init__(self, title, plots):
        """Contructs an instance of the 'PlotData' class
                
        Parameters:
        groupName (str): The name of the current group
        """
        self._title = title
        self._layout = [
            [sg.Push(), sg.Button("Prev", size=(5, 1), disabled=True, key="prevButton"), 
                sg.Text(f"Plot {plots[0]}", key="plotNumber"),
                sg.Button("Next", size=(5, 1), disabled=True, key="nextButton"), sg.Push()],
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
                    [sg.Listbox(values=[], size=(19, 11), key="dataList")],
                    [sg.Button("Delete", size=(8, 1), disabled=True, key="deleteDataSet"),
                        sg.Button("Edit", size=(8, 1), disabled=True, key="editDataSet")]
            ])
            ],
            [sg.Push(), sg.Button("Cancel", size=(14, 1), key="cancelPlot"),
                sg.Button("Confirm", size=(14, 1), disabled=True, key="confirmPlot"), sg.Push()]
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
        self._deleteData = self._window["deleteDataSet"]
        self._editData = self._window["editDataSet"]
        self._cancelPlot = self._window["cancelPlot"]
        self._confirmPlot = self._window["confirmPlot"]
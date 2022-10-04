import PySimpleGUI as sg
from windows.window import Window

class PlotDetails(Window):
    """This window allows the user to enter the call off stages, date,
    time and notes for individual plots. The information can be applied
    to all call off stages, or, in the event that different stages
    require different notes, or even dates/times, this information be be
    applied only to certain stages. In this case, a list of different
    groups of stages will be displayed, allowing the user to go back into
    each one and edit the information. Finally, the user can simply clear
    all detials from the plot and start again. When the information is
    correct, the user can save the details.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self, plot):
        self._title = f"Plot {plot} Details"
        self._layout = [
            [
            sg.Column([
                    [sg.Text("Call Off Stages:")],
                    [sg.Checkbox("Gutter Kit                ", default=False, key="gutter")],
                    [sg.Checkbox("Downpipe Kit         ", default=False, key="downpipe")],
                    [sg.Checkbox("Gas Kit                 ", default=False, key="gasKit")],
                    [sg.Checkbox("1st Fix Kit             ", default=False, key="1stFixKit")],
                    [sg.Checkbox("Soils Kit                ", default=False, key="soilsKit")],
                    [sg.Checkbox("Shower Tray/Mid Fix", default=False, key="midFix")],
                    [sg.Checkbox("Heating & Bath       ", default=False, key="heatingAndBath")],
                    [sg.Checkbox("Fix 2                     ", default=False, key="fix2")],
                    [sg.Checkbox("Sani                      ", default=False, key="sani")],
                    [sg.Checkbox("Fix 3                     ", default=False, key="fix3")],
                    [sg.Checkbox("Finals                   ", default=False, key="finals")],
                    [sg.Checkbox("Fix 4                     ", default=False, key="fix4")],
                    [sg.Button("Clear Selection", key="clearSelection")],
            ]),
            sg.VSeparator(),
            sg.Column([
                    [sg.Text("Date:")],
                    [
                        sg.In(size=(10, 1), key="date"), sg.CalendarButton("📅",
                        close_when_date_chosen=True, target="date", no_titlebar=False,
                        format=("%d/%m/%Y"), key="calendar")],
                    [sg.Text("Time:")],
                    [sg.In(size=(10, 1), key="time")],
                    [sg.Text("Notes:")],
                    [sg.In(size=(25, 1), key="notes")],
                    [sg.Button("Save Details", key="saveDetails")],
                    [sg.Text("_"*27)],
                    [sg.Listbox(values=[], size=(25, 10), key="detailsList")],
                    [sg.Push(), sg.Button("Delete", key="deleteDetails"), sg.Button("Edit", key="editDetails")]
            ])
            ],
            [sg.Text("_"*53)],
            [
                sg.Push(), sg.Button("Clear Details", key="clearPlot"), sg.Button("Cancel",key="cancelPlot"),
                sg.Button("Confirm", key="confirmPlot")
            ]
        ]

        super().__init__(self._title, self._layout)

        ## Key variables

        # Checkboxes
        self._gutter = self._window["gutter"]
        self._downpipe = self._window["downpipe"]
        self._gasKit = self._window["gasKit"]
        self._1stFixKit = self._window["1stFixKit"]
        self._soilsKit = self._window["soilsKit"]
        self._midFix = self._window["midFix"]
        self._heatingAndBath = self._window["heatingAndBath"]
        self._fix2 = self._window["fix2"]
        self._sani = self._window["sani"]
        self._fix3 = self._window["fix3"]
        self._finals = self._window["finals"]
        self._fix4 = self._window["fix4"]

        # Others
        self._clearSelection = self._window["clearSelection"]
        self._date = self._window["date"]
        self._calendar = self._window["calendar"]
        self._time = self._window["time"]
        self._notes = self._window["notes"]
        self._saveDetails = self._window["saveDetails"]
        self._detailsList = self._window["detailsList"]
        self._deleteDetails = self._window["deleteDetails"]
        self._editDetails = self._window["editDetails"]
        self._clearPlot = self._window["clearDetails"]
        self._cancelPlot = self._window["cancelPlot"]
        self._confirmPlot = self._window["confirmPlot"]
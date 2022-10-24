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

    def __init__(self, developer, site, plot):
        """Contructs an instance of the 'PlotDetails' class
        
        Parameters:
        developer:
        site:
        plot:
        """
        self._title = f"Plot {plot} Details"
        self._layout = [
            [
            sg.Column([
                    [sg.Text("Call Off Stages:")],
                    [sg.Checkbox("Gutter Kit                ", default=False, enable_events=True, key="gutter")],
                    [sg.Checkbox("Downpipe Kit         ", default=False, enable_events=True, key="downpipe")],
                    [sg.Checkbox("Gas Kit                 ", default=False, enable_events=True, key="gasKit")],
                    [sg.Checkbox("1st Fix Kit             ", default=False, enable_events=True, key="1stFixKit")],
                    [sg.Checkbox("Soils Kit                ", default=False, enable_events=True, key="soilsKit")],
                    [sg.Checkbox("Shower Tray/Mid Fix", default=False, enable_events=True, key="midFix")],
                    [sg.Checkbox("Heating & Bath       ", default=False, enable_events=True, key="heatingAndBath")],
                    [sg.Checkbox("Fix 2                     ", default=False, enable_events=True, key="fix2")],
                    [sg.Checkbox("Sani                      ", default=False, enable_events=True, key="sani")],
                    [sg.Checkbox("Fix 3                     ", default=False, enable_events=True, key="fix3")],
                    [sg.Checkbox("Finals                   ", default=False, enable_events=True, key="finals")],
                    [sg.Checkbox("Fix 4                     ", default=False, enable_events=True, key="fix4")],
                    [sg.VPush()],
                    [sg.VPush()],
                    [
                        sg.Push(), sg.Button("Clear Details", size=(15, 1), disabled=True,
                        key="clearDetails"), sg.Push()
                    ]
            ]),
            sg.VSeparator(),
            sg.Column([
                    [sg.Text("Date:")],
                    [
                        sg.In(size=(10, 1), enable_events=True, key="date"), sg.CalendarButton("📅",
                        close_when_date_chosen=True, target="date", no_titlebar=False,
                        format=("%d/%m/%Y"), size=(3, 1), key="calendar")
                    ],
                    [sg.Text("Time:")],
                    [sg.In(size=(10, 1), key="time")],
                    [sg.Text("Notes:")],
                    [sg.In(size=(25, 1), key="notes")],
                    [
                        sg.Button("Save Details", size=(21, 1), disabled=True,
                        key="saveDetails"),sg.Push()
                    ],
                    [sg.Text("_"*27), sg.Push()],
                    [sg.Listbox(values=[], size=(25, 10), key="detailsList")],
                    [
                        sg.Button("Delete", size=(10, 1), disabled=True, key="deleteDetails"),
                        sg.Push(), sg.Button("Edit", size=(10, 1), disabled=True, key="editDetails")
                    ]
            ])
            ],
            [sg.Push(), sg.Text("_"*54), sg.Push()],
            [
                sg.Push(), sg.Button("Cancel", size=(14, 1), key="cancelPlot"),
                sg.Button("Confirm", size=(14, 1), key="confirmPlot"), sg.Push()
            ]
        ]

        super().__init__(self._title, self._layout)
        self._window.DisableClose=True

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
        self._clearDetails = self._window["clearDetails"]
        self._date = self._window["date"]
        self._calendar = self._window["calendar"]
        self._time = self._window["time"]
        self._notes = self._window["notes"]
        self._saveDetails = self._window["saveDetails"]
        self._detailsList = self._window["detailsList"]
        self._deleteDetails = self._window["deleteDetails"]
        self._editDetails = self._window["editDetails"]
        self._cancelPlot = self._window["cancelPlot"]
        self._confirmPlot = self._window["confirmPlot"]

        self._checkboxes = [
            self._gutter, self._downpipe,
            self._gasKit, self._1stFixKit, self._soilsKit,
            self._midFix, self._heatingAndBath, self._fix2,
            self._sani, self._fix3, self._finals, self._fix4
        ]

        self._developer = developer
        self._site = site
        self._plot = plot
        self._allDetails = {}

        self._stages = [
            "GUTTER KIT", "DOWNPIPE KIT", "GAS KIT",
            "1ST FIX KIT", "SOILS KIT", "MID FIX", "HEATING & BATH",
            "FIX 2", "SANI", "FIX 3", "FINALS", "FIX 4"
        ]
    ##########

    def clearDetails(self):
        "Sets all checkboxes, date, time and notes to empty"
        for checkbox in self._checkboxes:
            checkbox.update(False)
        self._date.Update("")
        self._time.Update("")
        self._notes.Update("")

    def clearChecks(self):
        "Sets all checkboxes to empty"
        for checkbox in self._checkboxes:
            checkbox.update(False)
    ##########

    def saveDetails(self):
        """Saves details to allDetails, and displays
        call off stages in detailsList. Sets all checkboxes to
        empty but leaves date, time and notes untouched"""
        try:
            stages = []
            counter = 0
            for checkbox in self._checkboxes:
                if checkbox.get() == True:
                    stages.append(self._stages[counter])
                counter += 1
            if len(stages) > 1:
                self._allDetails[f"{stages[0]} etc."] = [self._developer,
                self._site, self._plot, stages,
                self._date.get(), self._time.get(), "", self._notes.get()]
            else:
                self._allDetails[f"{stages[0]}"] = [self._developer,
                self._site, self._plot, stages, self._date.get(),
                self._time.get(), "", self._notes.get()]
            
            self._detailsList.Update(values=self._allDetails.keys())
            print(self._allDetails)
        except:
            pass
    ##########

    def deleteDetails(self):
        "Deletes the currently selected key from allDetails"
        try:
            self._allDetails.pop(self._detailsList.get()[0])
            self._detailsList.Update(values=self._allDetails.keys())
        except:
            pass
    ###########

    def editDetails(self):
        "Brings up the information for the selected details for editing"
        try:
            editList = self._allDetails[self._detailsList.get()[0]]
            self._date.Update(editList[4])
            self._time.Update(editList[5])
            self._notes.Update(editList[7])
            counter = 0
            for stage in self._stages:
                if stage in editList[3]:
                    self._checkboxes[counter].Update(True)
                counter += 1
        except:
            pass
    ##########

    def confirmPlot(self):
        "Adds all details to Data.currentGroupDict"

        returnList = []
        for key in self._allDetails:
            returnList.append(self._allDetails[key])
        return returnList

    def toggleButtons(self):
        """Checks if the clear, save, delete, edit, and confirm
        buttons should be enabled and sets them appropriately"""
        checkMarked = False
        for checkbox in self._checkboxes:
            if checkbox.get() == True:
                checkMarked = True
                break
        if checkMarked:
            self._clearDetails.Update(disabled=False)
        else:
            self._clearDetails.Update(disabled=True)

        if checkMarked and self._date.get() != "":
            self._saveDetails.Update(disabled=False)
        else:
            self._saveDetails.Update(disabled=True)

        if self._detailsList.Values != []:
            self._deleteDetails.Update(disabled=False)
            self._editDetails.Update(disabled=False)
            self._confirmPlot.Update(disabled=False)
        else:
            self._deleteDetails.Update(disabled=True)
            self._editDetails.Update(disabled=True)
            self._confirmPlot.Update(disabled=True)
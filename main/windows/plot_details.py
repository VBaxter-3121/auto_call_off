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
                    [sg.Checkbox("Gutter Kit                ", default=False, key="stage1")],
                    [sg.Checkbox("Downpipe Kit         ", default=False, key="stage2")],
                    [sg.Checkbox("Gas Kit                 ", default=False, key="stage3")],
                    [sg.Checkbox("1st Fix Kit             ", default=False, key="stage4")],
                    [sg.Checkbox("Soils Kit                ", default=False, key="stage5")],
                    [sg.Checkbox("Shower Tray/Mid Fix", default=False, key="stage6")],
                    [sg.Checkbox("Heating & Bath       ", default=False, key="stage7")],
                    [sg.Checkbox("Fix 2                     ", default=False, key="stage8")],
                    [sg.Checkbox("Sani                      ", default=False, key="stage9")],
                    [sg.Checkbox("Fix 3                     ", default=False, key="stage10")],
                    [sg.Checkbox("Finals                   ", default=False, key="stage11")],
                    [sg.Checkbox("Fix 4                     ", default=False, key="stage12")],
                    [sg.Push(), sg.Button("Clear Selection", key="clearSelection")],
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
                    [sg.Push(), sg.Button("Save Details")],
                    [sg.Listbox(values=[], size=(25, 11), key="savedDetails")],
                    [sg.Push(), sg.Button("Delete", key="deleteDetails"), sg.Button("Edit", key="editDetails")]
            ])
            ],
            [sg.Text("_"*53)],
            [
                sg.Push(), sg.Button("Clear Details", key="clearDetails"), sg.Button("Cancel",key="cancelDetails"),
                sg.Button("Save", key="saveDetails")
            ]
        ]
        super().__init__(self._title, self._layout)

    def open(self):
        "Opens the home window and runs the event loop"
        while True:
            event, values = self._window.read()
            if event == sg.WIN_CLOSED:
                break
        self._window.close()
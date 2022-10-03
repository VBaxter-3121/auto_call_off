import PySimpleGUI as sg

class Window:
    """A window will display, and allow the user to add, edit or remove
    information relating to the call off process.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self, title, layout):
        "Constructs a new window"
        self._title = title
        self._layout = layout
        self._window = sg.Window(self._title, self._layout, finalize=True)

    def getWindow(self):
        "Returns the window attribute"
        return self._window
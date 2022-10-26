import PySimpleGUI as sg

class Window:
    """A window will display, and allow the user to add, edit or remove
    information relating to the call off process.
    
    Attributes:
    _title: The title of the window
    _layout: The widgets that make up the window's layout
    """

    def __init__(self, title, layout, returnKeyboard=False):
        """Constructs an instance of the 'Window' class
        
        Parameters:
        title:
        layout:
        """
        self._title = title
        self._layout = layout
        if not returnKeyboard:
            self._window = sg.Window(self._title, self._layout, finalize=True)
        else:
            self._window = sg.Window(self._title, self._layout, return_keyboard_events=True, finalize=True)

    def getWindow(self):
        "Returns the window attribute"
        return self._window

    def read(self):
        "Template to polymorph"

    def _toggleDisabled(self, event, values):
        "Template to polymorph"
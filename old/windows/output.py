from windows.window import Window

class Output(Window):
    ""
    def __init__(self):
        ""
        self._title = "Output Window"
        self._layout = [
            []
        ]

        super().__init__(self._title, self._layout)
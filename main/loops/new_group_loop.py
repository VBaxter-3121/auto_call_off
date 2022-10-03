from loops.loop import Loop
import PySimpleGUI as sg

class NewGroupLoop(Loop):
    """"""

    def __init__(self, window):
        ""
        super().__init__(window)

    def _listenLoop(self, event, values):
        ""

        ## Events

        #
        if event == "cancelGroup":
            ""
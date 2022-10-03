# This class will be used to run the program, looping until it is closed

import PySimpleGUI as sg

from loops.loop import Loop
from loops.home_loop import HomeLoop
from loops.new_group_loop import NewGroupLoop

from windows.window import Window
from windows.home import Home
from windows.new_group import NewGroup

class Organiser():
    """"""

    def __init__(self, data):
        ""
        homeWindow = Home()
        self._currentWindow = homeWindow.getWindow()
        self._data

    def _startProgram(self):
        """Current idea:
        While loop for whole program:
            If window needed:
            Nested while loop for individual windows:"""

        running = True

        while running:
            while True:
                event, values = self._currentWindow.read()

                # For testing
                print(event)

                if event == sg.WIN_CLOSED:
                    break

                self._listenLoop(event, values)
            
            self._window.close()
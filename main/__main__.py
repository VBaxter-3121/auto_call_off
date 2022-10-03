from windows.home import Home
from loops.loop import Loop
from loops.home_loop import HomeLoop

from organiser.organiser import Organiser
from data.data import Data

def main():
    # home = Home()
    # homeWindow = home.getWindow()
    # loop = HomeLoop(homeWindow)
    # loop.startLoop()

    organiser = Organiser()
    data = Data()

    organiser.startProgram()

if __name__ == "__main__":
    main()
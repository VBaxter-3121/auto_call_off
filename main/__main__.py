from windows.home import Home

from organiser.organiser import Organiser
from data.data import Data

def main():
    # home = Home()
    # homeWindow = home.getWindow()
    # loop = HomeLoop(homeWindow)
    # loop.startLoop()
    
    data = Data()
    organiser = Organiser(data)

    organiser.startProgram()

if __name__ == "__main__":
    main()
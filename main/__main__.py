from organiser.gui_organiser import GUIOrganiser
from organiser.call_off_organiser import CallOffOrganiser

from data.data import Data

def main():
    while True:
        data = Data()
        organiser1 = GUIOrganiser(data)
        organiser1.startProgram()
        organiser2 = CallOffOrganiser(data)
        repeat = organiser2.executeCallOffs()
        if not repeat:
            break
##########

if __name__ == "__main__":
    main()
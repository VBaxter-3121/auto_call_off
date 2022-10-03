from windows.home import Home
from loops.loop import Loop
from loops.home_loop import HomeLoop

def main():
    home = Home()
    homeWindow = home.getWindow()
    loop = HomeLoop(homeWindow)
    loop.startLoop()

if __name__ == "__main__":
    main()
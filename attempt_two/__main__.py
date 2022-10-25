from windows.home import Home
from data.call_off_data import CallOffData

callOffData = CallOffData()
home = Home(callOffData)
home.read()
from windows.home import Home
from data.call_off_data import CallOffData
from call_off.filter_records import FilterRecords

def main():
    while True:
        callOffData = CallOffData()
        home = Home(callOffData)
        loop = home.read()
        if loop == False:
            break

if __name__ == "__main__":
    main()
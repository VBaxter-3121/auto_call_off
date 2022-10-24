from call_off.filter_records import FilterRecords
from call_off.read_records import ReadRecords
from call_off.fill_sheets import FillSheets
from call_off.window_selector import WindowSelector

class CallOffOrganiser:
    """Takes the AllGroupsDict from the Data class and uses the 
    information to run the various processes required to complete
    the call off sheets.
    """

    def __init__(self, data):
        """Contructs an instance of the CallOffOrganiser Class
        
        Attributes:
        data: An instance of the Data class
        filter: An instance of the FilterRecords class
        read: An instance of the ReadRecords class
        fill: An instance of the FillSheets class
        selector: An instance of the WindowSelector class"""
        self._data = data
        self._selector = WindowSelector()
        self._filter = FilterRecords(self._selector)
        self._read = ReadRecords(self._selector)
        self._fill = FillSheets(self._selector)

    def executeCallOffs(self):
        "Executes the call off process"
        allGroupsDict = self._data.getAllGroupsDict()
        for group in allGroupsDict:
            firstKey = next(iter(allGroupsDict[group]))
            developer, site = allGroupsDict[group][firstKey][0], allGroupsDict[group][firstKey][1]
            for plot in allGroupsDict[group]:
                currentPlot = allGroupsDict[group][plot]

                # Get the number to filter records by
                plotNumber = self._addZeros(allGroupsDict[group][plot])
                siteNumber = self._data.getSiteNumber(developer, site)
                jobNumber = f"{siteNumber}{plotNumber}"

                # Get the phase numbers to filter by
                phaseNumbers = self._getPhaseNumbers(currentPlot[3])

                recordsFound = self._filter.filterBy(jobNumber, phaseNumbers)
                if recordsFound:
                    sheetGroups = self._read.read()

                    self._fill.fillSheets(currentPlot, sheetGroups)

        return False

    def _addZeros(self, number):
        """Prepares a plot number for use in filtering records
        
        Parameters:
        number: A string referencing a plot number
        
        Returns:
        plotNumber: A string containing a three digit number
        referencing a plot number
        """
        if len(number) == 1:
            plotNumber = f"00{number}"
        elif len(number) == 2:
            plotNumber = f"0{number}"
        else:
            plotNumber = number
        
        return plotNumber
    
    def _getPhaseNumbers(self, stages):
        """Returns a list of relevant phase numbers
        
        Parameters:
        stages: A list of strings used to identify phase numbers
        
        Returns:
        phaseNumbers: A list of phase numbers identified
        """
        phaseNumbers = []
        stageNames = {"GUTTER KIT": "RAIN", "DOWNPIPE KIT": "RAIN",
                        "GAS KIT": "GAS", "1ST FIX KIT": "1ST FIX",
                        "SOILS KIT": "SOIL", "MID FIX": "1ST FIX",
                        "HEATING & BATH": "2ND FIX", "FIX 2": "2ND FIX",
                        "SANI": "2ND FIX", "FIX 3": "2ND FIX",
                        "FINALS": "FINAL FIX","FIX 4": "FINAL FIX"}

        for stage in stages:
            if stageNames[stage] not in phaseNumbers:
                phaseNumbers.append(stageNames[stage])

        return phaseNumbers
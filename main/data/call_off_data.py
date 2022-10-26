from tokenize import group


class CallOffData():
    """Contains a dictionary that holds all the data for
    current call offs. Certain parts of this dictionary
    can be updated or read by certain windows. Windows
    read from the dictionary in order to pre-populate
    values for editing, and they update the dictionary
    to prepare all the data needed to run the call off
    classes
    """

    def __init__(self):
        "Contructs an instance of the CallOffData class"

        self._callOffDict = {}

    def readGroups(self):
        "Returns a list of keys in callOffDict (used by home)"
        return list(map(lambda key : key, self._callOffDict.keys()))

    def groupEmpty(self, groupName):
        "Returns True if specified key has a value of {} (used by home)"
        return self._callOffDict[groupName] == {}

    def writeGroup(self, groupName):
        "Updates the dictionary with a new key (used by home)"
        self._callOffDict.update({groupName: {}})

    def deleteGroup(self, groupName):
        "Removes the specified key from the dictionary (used by home)"
        self._callOffDict.pop(groupName)

    def readPlots(self, groupName):
        """Returns a list of plot numbers belonging to the key
        specified by groupName (used by group data and plot data)"""
        return (list(map(lambda key : key, self._callOffDict[groupName].keys())))

    def writePlot(self, groupName, plotNumber):
        "Updates the dictionary with a new plot number"
        self._callOffDict[groupName].update({plotNumber: []})

    # def writePlots(self, groupName, plotData):
    #     """Updates the dictionary with an existing key (groupName)
    #     followed by values as plot numbers, which themselves are
    #     keys with their own values (used by plot data)
        
    #     Example:
    #     plotData = {"Plot1: ["BDW", "Harbour Place", "1", "FIX 2",
    #     "01/01/2000", "P9D", "Liam Adams", "Please omit traps"]}"""
    #     self._callOffDict.update({groupName: plotData})

    def deletePlot(self, groupName, plotNumber):
        """Removes the specified plot from the dictionary
        (used by group data and plot data)"""
        self._callOffDict[groupName].pop(plotNumber)
        self._printDict()

    def trimPlots(self, groupName, plotNumbers):
        """Removes empty plots from dictionary if user confirms
        plot data without filling some plots (used by plot data)"""
        for plot in plotNumbers:
            self._callOffDict[groupName].pop(plot)

    def readDataSets(self, groupName, plotNumber):
        """Returns a list of data sets for the specified plot
        (used by plot data and group data)"""
        return self._callOffDict[groupName][plotNumber]

    def writeDataSet(self, groupName, plotNumber, dataSet):
        "Saves data from plot data window to callOffDict (used by plot data)"
        self._callOffDict[groupName][plotNumber].append(dataSet)

    def deleteDataSet(self, groupName, plotNumber, index):
        "Deletes a data set from the dictionary (used by plot data)"
        self._callOffDict[groupName][plotNumber].pop(index)

    def _printDict(self):
        "For debugging"
        ###
        print(self._callOffDict)
        ###
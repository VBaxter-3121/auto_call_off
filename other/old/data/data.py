from data.job_details import jobDetails

class Data():
    """This class keeps track of all data that the user inputs to
    the program"""

    def __init__(self):
        "Contructs Contructs an instance of the data class"

        self._allGroupsDict = {}
        print(self._allGroupsDict)
        # currentGroupDict will be reset at the start of making a new group.
        # It will have a key added to it every time a plot is confirmed.
        self._currentGroupDict = {}
        self._jobDetails = jobDetails
    ##########

    def addGroup(self):
        """Adds a new group to the data dictionary
        
        Parameters:
        group: A dictionary of the following format:
        group = {
            Plot x: [developer, site, plotNumber, [callOffStages], date, time, manager, notes],
            Plot y: [developer, site, plotNumber, [callOffStages], date, time, manager, notes],
            Plot z: [developer, site, plotNumber, [callOffStages], date, time, manager, notes]
        }
        orderNumbers will later replace callOffStages
        """
        firstKey = next(iter(self._currentGroupDict))
        groupName = f"{self._currentGroupDict[firstKey][0]}, {self._currentGroupDict[firstKey][1]}"

        self._allGroupsDict[groupName] = self._currentGroupDict
        ## For testing ##
        print(self._allGroupsDict)
    ##########

    def checkConflicts(self):
        """Ensures that the user doesn't try to add two groups for the
        same site. If they do, see if the data can be merged.
        
        Parameters:
        group: A dictionary of the following format:
        group = {
            Plot x: [developer, site, plotNumber, [callOffStages], date, time, manager, notes],
            Plot y: [developer, site, plotNumber, [callOffStages], date, time, manager, notes],
            Plot z: [developer, site, plotNumber, [callOffStages], date, time, manager, notes]
        }
        orderNumbers will later replace callOffStages
        """
        # As all entries in any group will have the same developer and site
        # names, just take the first key and take the information from that one
        # firstKey = next(iter(self._currentGroupDict))
        # groupName = f"{self._currentGroupDict[firstKey][0]}, {self._currentGroupDict[firstKey][1]}"

        # if groupName not in self._allGroupsDict:
        #     self._addGroup(groupName, self._currentGroupDict)
        #     self._currentGroupDict = {}
        #     return True
        # else:
        #     existingKeys = []
        #     newKeys = []

        #     for key in self._allGroupsDict[groupName]:
        #         existingKeys.append(key)
            
        #     for key in self._currentGroupDict:
        #         newKeys.append(key)

        #     for key in newKeys:
        #         if key in existingKeys:

    ##########

    def deleteGroup(self, key):
        """Removes a group from the data dictionary
        
        Parameters:
        key: A string matching one of the keys in the data dictionary
        """
        self._allGroupsDict.pop(key)
    ##########

    def getDevelopers(self):
        "Returns the list of developers"
        developerList = []
        for name in jobDetails.keys():
            developerList.append(name)
        return developerList
    ##########

    def getSites(self, developer):
        """Returns the list of sites pertaining to the developer
        
        Parameters:
        developer: A string referencing the developer key to pull
        a list of sites from
        """
        siteList = []
        for name in jobDetails[developer].keys():
            siteList.append(name)
        return siteList
    ##########

    def addPlot(self, plotInfo, counter):
        """Adds a key to currentGroupDict for a given plot
        
        Parameters:
        plotInfo: A list containing all user input information for the plot
        """
        plotKey = plotInfo[2] + f"-{counter}"
        # Get the contracts manager and insert it into position 6
        self._currentGroupDict[f"Plot {plotKey}"] = plotInfo
    ##########

    def getGroupDetails(self, group):
        """Returns the developer, site and list of plots from a given group
        
        Parameters:
        group: A string matching a key from allGroupsDict
        """
    ##########

    def deleteFromCurrent(self, plots):
        """Deletes specified keys from currentGroupDict
        
        Parameters:
        plots: A list of plot numbers
        """
        for plot in plots:
            for key in self._currentGroupDict:
                if f"Plot {plot}-" in key:
                    self._currentGroupDict.pop(key)
    ##########

    def getAllGroups(self):
        "Returns keys from allGroupsDict"
        returnList = []
        for key in self._allGroupsDict:
            returnList.append(key)
        return returnList

    def getAllGroupsDict(self):
        "Returns allGroupsDict"
        return self._allGroupsDict

    def getSiteNumber(self, developer, site):
        "Returns a site number"
        return self._jobDetails[developer][site][0]
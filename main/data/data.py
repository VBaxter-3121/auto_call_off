from data.job_details import jobDetails

class Data():
    """This class keeps track of all data that the user inputs to
    the program"""

    def __init__(self):
        "Contructs the data class"

        self._allGroupsDict = {}
        # currentGroupDict will be reset at the start of making a new group.
        # It will have a key added to it every time a plot is set
        self._currentGroupDict = {}
        self._jobDetails = jobDetails
    ##########

    def _addGroup(self, groupName, group):
        """Adds a new group to the data dictionary
        
        Parameters:
        group: A dictionary of the following format:
        group = {
            Plot x: [developer, site, plotNumber, orderNumbers, date, time, manager, notes],
            Plot y: [developer, site, plotNumber, orderNumbers, date, time, manager, notes],
            Plot z: [developer, site, plotNumber, orderNumbers, date, time, manager, notes]
        }
        """
        self._allGroupsDict[groupName] = group
        ## For testing ##
        print(self._allGroupsDict)
    ##########

    def checkConflicts(self, group):
        """Ensures that the user doesn't try to add two groups for the
        same site. If they do, see if the data can be merged.
        
        Parameters:
        group: A dictionary of the following format:
        group = {
            Plot x: [developer, site, plotNumber, orderNumbers, date, time, manager, notes],
            Plot y: [developer, site, plotNumber, orderNumbers, date, time, manager, notes],
            Plot z: [developer, site, plotNumber, orderNumbers, date, time, manager, notes]
        }
        """
        # As all entries in any group will have the same developer and site
        # names, just take the first key and take the information from that one
        firstKey = next(iter(group))
        groupName = f"{group[firstKey][0]}, {group[firstKey][1]}"

        if groupName not in self._allGroupsDict:
            self._addGroup(groupName, group)
        else:
            ""
            # Here code for merging will be added
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
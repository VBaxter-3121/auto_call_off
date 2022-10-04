# This class will be used to keep track of the data between windows, being passed between them all

class Data():
    """This class keeps track of all data that the user inputs to
    the program"""

    def __init__(self):
        "Contructs the data class"

        self._data = {}

    def checkConflicts(self, group):
        """Ensures that the user doesn't try to add two groups for the
        same site
        
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
        
        if groupName not in self._data:
            self._addGroup(groupName, group)
        else:
            print("Site already has information in dictionary")
        
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
        self._data[groupName] = group
        print(self._data)

    def deleteGroup(self, key):
        """Removes a group from the data dictionary
        
        Parameters:
        key: A string matching one of the keys in the data dictionary
        """
        self._data.pop(key)
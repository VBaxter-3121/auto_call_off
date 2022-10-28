from pydoc import describe
from call_off.filter_records import FilterRecords
from call_off.read_records import ReadRecords
from call_off.fill_sheet import FillSheet
from data.job_details import jobDetails
from data.phase_details import phaseDetails

class CallOff():
    ""

    def __init__(self, callOffDict):
        ""
        self._data = callOffDict
        self._filter = FilterRecords()
        self._read = ReadRecords()
        self._fill = FillSheet()
        self._recognisedNotes = ["All delivery drivers must report to the site team on arrival, \r\nAll delivery drivers must wear High Viz Vest, Hard Hat, Safety foot wear and gloves.",
        ""]

    def execute(self):
        ""
        for groupName in self._data:
            for plot in self._data[groupName]:
                for dataSet in self._data[groupName][plot]:
                    "[developer, site, plotNumber, requiredStages, date, time, manager, notes, siteNumber]"
                    if self._filter.filter(
                        self._makeJobNumber(dataSet.pop(-1), dataSet[2]), self._getPhaseNumbers(dataSet[3])):
                        requiredPoDict = self._read.read(dataSet[3])
                        self._constructOutput(requiredPoDict, dataSet)
                        suppliers = self._groupBySupplier(requiredPoDict)
                        for supplier in suppliers:
                            fileName = self._getFileName(requiredPoDict, suppliers[supplier])
                            sheetData = dataSet
                            sheetData[3] = ", ".join(suppliers[supplier])
                            if sheetData[5] == "":
                                sheetData[5] = " "
                            if sheetData[7] == "":
                                sheetData[7] = " "
                            self._fill.fillSheet(sheetData, fileName)

    def _makeJobNumber(self, jobNumber, plotNumber):
        ""
        if len(plotNumber) == 3:
            return f"{jobNumber}{plotNumber}"
        elif len(plotNumber) == 2:
            return f"{jobNumber}0{plotNumber}"
        elif len(plotNumber) == 1:
            return f"{jobNumber}00{plotNumber}"

    def _getPhaseNumbers(self, stages):
        ""
        return list(dict.fromkeys(list(map(lambda stage : phaseDetails[stage], stages))))

    def _constructOutput(self, requiredPoDict, dataSet):
        ""
        for po in requiredPoDict:
            if requiredPoDict[po][2] in self._recognisedNotes:
                print(f"{po} - {jobDetails[dataSet[0]][dataSet[1]][2]}/{dataSet[2]}/{requiredPoDict[po][0].capitalize()} - {dataSet[4]} {dataSet[5]}")
            else:
                print(f"{po} - {jobDetails[dataSet[0]][dataSet[1]][2]}/{dataSet[2]}/{requiredPoDict[po][0].capitalize()} - {dataSet[4]} {dataSet[5]} (Check notes)")

        for stage in dataSet[3]:
            stageFound = False
            for po in requiredPoDict:
                if stage == requiredPoDict[po][0]:
                    stageFound = True
                elif stage == "MID FIX" and (
                    requiredPoDict[po][0] == "SHOWER TRAY"):
                    stageFound = True
                elif stage == "HEATING & BATH" and (
                    requiredPoDict[po][0] == "HEATING" or
                    requiredPoDict[po][0] == "BATH" or
                    requiredPoDict[po][0] == "2ND FIX KIT"):
                    stageFound = True
                elif stage == "FIX 2" and (
                    requiredPoDict[po][0] == "2ND FIX FITTINGS"):
                    stageFound = True
                elif stage == "FINALS" and (
                    requiredPoDict[po][0] == "HEATING FINALS" or
                    requiredPoDict[po][0] == "SANI FINALS"):
                    stageFound = True
            if not stageFound:
                print(f"Error: No orders found for {dataSet[0]}/{dataSet[1]}/{dataSet[2]}/{stage.capitalize()}")
        print()
    
    def _groupBySupplier(self, requiredPoDict):
        ""
        suppliers = dict.fromkeys(map(lambda po : requiredPoDict[po][1], requiredPoDict))
        for supplier in suppliers:
            suppliers[supplier] = []
        for po in requiredPoDict:
            suppliers[requiredPoDict[po][1]].append(po)
        return suppliers
    
    def _getFileName(self, requiredPoDict, currentSupplier):
        ""
        fileName = []
        for po in currentSupplier:
            fileName.append(requiredPoDict[po][0])
        return ", ".join(fileName)

"""
requiredPoDict = {
    "300300": ["Heating", "PTS", "Header notes..."],
    "300301": ["Bath", "PCS", "Header notes..."],
    "300302": ["Fix 2", "PTS", "Header notes..."],
    "300303": ["Sani", "PCS", "Header notes..."],
    "300304": ["Fix 3", "PTS", "Header notes..."]
}

alternateStages = ["Heating", "Bath"]

dataSet = ["Crest", "Arbourfield", "100",
    ["HEATING & BATH", "FIX 2", "SANI", "FIX 3", "FIX 4"],
    "31/10/22", "P9D", "Chris Matthews",
    "Please omit x, y, z"]

Desired result:
dataSetPTS = ["Crest", "Arbourfield", "100",
    "300300, 300302, 300304",
    "31/10/22", "P9D", "Chris Matthews",
    "Please omit x, y, z"]
dataSetPCS = ["Crest", "Arbourfield", "100",
    "300301, 300303",
    "31/10/22", "P9D", "Chris Matthews",
    "Please omit x, y, z"]

"300300 - Cr/Ar/100/Heating - 31/10/22 P9D (Check notes)"
"300301 - Cr/Ar/100/Bath - 31/10/22 P9D (Check notes)"
"300302 - Cr/Ar/100/Fix 2 - 31/10/22 P9D (Check notes)"
"300303 - Cr/Ar/100/Sani - 31/10/22 P9D"
"300304 - Cr/Ar/100/Fix 3 - 31/10/22 P9D"
"Error: No orders found for Cr/Ar/100/Fix 4

Steps:
1. Find number of suppliers in requiredPoDict
2. Seperate orders by supplier
3. Duplicate dataSet for each supplier group, replacing stages with PO numbers
"""
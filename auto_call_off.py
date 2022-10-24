### CURRENT PROJECT:
### Put multiple PO numbers on one call off sheet
### in accordance with suppliers

import PySimpleGUI as sg
import pyautogui as pag
import pyperclip as pyp
import keyboard
import time
import os

from dictionaries.dev_names import devNames
from dictionaries.site_names import siteNames
from dictionaries.job_details import jobDetails
from dictionaries.phase_details import phaseDetails

defaultJobNumber = "images/default-job-number.png"
emptyList = "images/empty-list.png"
pegasusBackground = "images/pegasus-background.png"
win1 = "images/win1.png"
win2 = "images/win2.png"
win3 = "images/win3.png"
win4 = "images/win4.png"
win5 = "images/win5.png"
win6 = "images/win6.png"

formTitle = "Auto Call Off"
consoleTitle = "Auto Call Off - python3  auto_call_off.py"

def main():

    devNames = []
    plots = []    
    currentPlot = ""
    plotsIndex = 0
    times = ["First Drop", "P9D", "P10D", "AM", "ATD"]
    callOffDict = {}
    editing = False

    for key in jobDetails:
        devNames.append(key)

    stages = {}

    # Sections of layout
    firstColumn = [
        [sg.Text("Developer:")],
        [sg.Combo(size=(25, 4), enable_events=True, values=(devNames), key="_DEVS_")],
        [sg.Text("Site:")],
        [sg.Combo(size=(25, 4), enable_events=True, values=[], key="_SITES_")],
        [sg.Text("Plot Number:")],
        [sg.In(size=(25, 1), enable_events=True, key="_PLOT_")],
        [sg.Listbox(values=[], size=(25, 11), enable_events=True, key="_PLOTS_")],
        [sg.Button("Delete", disabled=True, key="_DELETE_"), sg.Button("Set Details", disabled=True, key="_SET_")]
    ]

    secondColumn = [
        [sg.Text(f"Call off stages", key="_CHECK TEXT_")],
        [sg.Checkbox("Gutter", default=False, disabled=True, key="_GUTT_")],
        [sg.Checkbox("Downpipe", default=False, disabled=True, key="_DOWN_")],
        [sg.Checkbox("Gas Kit", default=False, disabled=True, key="_GAS_")],
        [sg.Checkbox("1st Fix Kit", default=False, disabled=True, key="_1ST_")],
        [sg.Checkbox("Soils Kit", default=False, disabled=True, key="_SOIL_")],
        [sg.Checkbox("Shower Tray/Mid Fix", default=False, disabled=True, key="_MID_")],
        [sg.Checkbox("Heating & Bath", default=False, disabled=True, key="_HEAT_")],
        [sg.Checkbox("Fix 2 Fittings Kit", default=False, disabled=True, key="_FIX2_")],
        [sg.Checkbox("Sani", default=False, disabled=True, key="_SANI_")],
        [sg.Checkbox("Fix 3 Fittings Kit", default=False, disabled=True, key="_FIX3_")],
        [sg.Checkbox("Finals", default=False, disabled=True, key="_FIN_")],
        [sg.Checkbox("Fix 4 Fittings Kit", default=False, disabled=True, key="_FIX4_")]
    ]

    thirdColumn = [
        [sg.Text("Date:")],
        [
            sg.In(size=(25, 1), disabled=True, key="_DATE_"),
            sg.CalendarButton("Date", close_when_date_chosen=True, target="_DATE_", no_titlebar=False, format=("%d/%m/%Y"), disabled=True, key="_CALENDAR_")
            ],
        [sg.Text("Time:")],
        [sg.Combo(size=(25, 4), enable_events=True, values=(times), disabled=True, key="_TIMES_")],
        [sg.Text("Notes:")],
        [sg.Multiline(size=(25, 12.5), disabled=True, key="_NOTES_")],
        [sg.Button("Cancel", disabled=True, key="_CANCEL_"), sg.Button("Submit Plot", disabled=True, key="_SUBMIT_")]
    ]

    # Layout
    layout = [
        [
            sg.Column(firstColumn),
            sg.VSeperator(),
            sg.Column(secondColumn),
            sg.VSeparator(),
            sg.Column(thirdColumn)
            ]
        ]

    # Window
    window = sg.Window("Auto Call Off", layout, finalize=True)

    window["_PLOT_"].bind("<Return>", " Enter")

    # Event Loop
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        elif event == "_DEVS_":
            siteNames = []
            for key in jobDetails[values["_DEVS_"]]:
                siteNames.append(key)
            window["_SITES_"].update(values=siteNames)

        elif event == "_PLOT_ Enter":
            plotNumber = values["_PLOT_"]
            if plotNumber != "":
                plots.append(plotNumber)
                window["_PLOTS_"].update(plots)
                window["_PLOT_"].update("")

        elif event == "_DELETE_":
            if values["_PLOTS_"] != []:
                plots.remove(values["_PLOTS_"][0])
                window["_PLOTS_"].update(plots)

        elif event == "_SET_":
            for plot in plots:
                callOffDict[plot] = [values["_DEVS_"], values["_SITES_"], plot, "PO NUMBER", "DATE", "TIME", jobDetails[values["_DEVS_"]][values["_SITES_"]][1], "NOTES"]
            currentPlot = plots[plotsIndex]
            disableFirst(window)
            enableSecond(secondColumn, window, currentPlot)
            enableThird(window, currentPlot)
            editing = True

        elif event == "_SUBMIT_":
            callOffDict[currentPlot] = [values["_DEVS_"], values["_SITES_"], currentPlot, "", values["_DATE_"], values["_TIMES_"], jobDetails[values["_DEVS_"]][values["_SITES_"]][1], values["_NOTES_"]]
            stages[currentPlot] = getStages(secondColumn, values)
            if plotsIndex + 1 != len(plots):
                plotsIndex += 1
                currentPlot = plots[plotsIndex]
                window["_CHECK TEXT_"].update(f"Call off stages for plot {currentPlot}:")
                window["_SUBMIT_"].update(f"Submit Plot {currentPlot}")
            else:
                confirmed = confirm(callOffDict, stages)
                if confirmed:
                    callOff(callOffDict, stages)
                    windowSelect("Console")
                    input("""
Have you filled out the progress sheet?""")
                    input("Press 'Enter' to begin new call offs (don't forget to check any important notes before you do!)")
                    clear()
                    windowSelect("Self")
                    window["_CANCEL_"].click()
                    devNames = []
                    siteNames = []
                    plots = []
                    for key in jobDetails:
                        devNames.append(key)
                    window["_DEVS_"].update(values=devNames)
                    window["_SITES_"].update(values=siteNames)
                    window["_PLOT_"].update(value="")
                    window["_PLOTS_"].update(plots)
                else:
                    window["_CANCEL_"].click()

        elif event == "_CANCEL_":
            callOffDict = {}
            plotsIndex = 0
            enableFirst(window)
            disableSecond(secondColumn, window)
            disableThird(window)
            editing = False

        enableDisable(values, window, plots, editing)

    window.close()

def enableDisable(values, window, plots, editing):
    enableDelete(window, plots, editing)
    disableDelete(window, plots)
    enableSet(values, window, plots, editing)
    disableSet(values, window, plots)

def enableDelete(window, plots, editing):
    if len(plots) > 0 and editing == False:
        window["_DELETE_"].update(disabled=False)

def disableDelete(window, plots):
    if len(plots) == 0:
        window["_DELETE_"].update(disabled=True)

def enableSet(values, window, plots, editing):
    if values["_DEVS_"] != "" and values["_SITES_"] != "" and len(plots) > 0 and editing == False:
        window["_SET_"].update(disabled=False)

def disableSet(values, window, plots):
    if values["_DEVS_"] == "" or values["_SITES_"] not in jobDetails[values["_DEVS_"]] or len(plots) == 0:
        window["_SET_"].update(disabled=True)

def enableFirst(window):
    window["_DEVS_"].update(disabled=False)
    window["_SITES_"].update(disabled=False)
    window["_PLOT_"].update(disabled=False)
    window["_PLOTS_"].update(disabled=False)
    window["_DELETE_"].update(disabled=False)
    window["_SET_"].update(disabled=False)

def disableFirst(window):
    window["_DEVS_"].update(disabled=True)
    window["_SITES_"].update(disabled=True)
    window["_PLOT_"].update(disabled=True)
    window["_PLOTS_"].update(disabled=True)
    window["_DELETE_"].update(disabled=True)
    window["_SET_"].update(disabled=True)

def enableSecond(secondColumn, window, currentPlot):
    window["_CHECK TEXT_"].update(f"Call off stages for plot {currentPlot}:")
    for list in secondColumn[1:]:
        for widget in list:
            widget.update(disabled=False)

def disableSecond(secondColumn, window):
    window["_CHECK TEXT_"].update(f"Call off stages")
    for list in secondColumn[1:]:
        for widget in list:
            widget.update(value=False, disabled=True)

def enableThird(window, currentPlot):
    window["_DATE_"].update(disabled=False)
    window["_CALENDAR_"].update(disabled=False)
    window["_TIMES_"].update(disabled=False)
    window["_NOTES_"].update(disabled=False)
    window["_CANCEL_"].update(disabled=False)
    window["_SUBMIT_"].update(f"Submit Plot {currentPlot}", disabled=False)

def disableThird(window):
    window["_DATE_"].update(value="", disabled=True)
    window["_CALENDAR_"].update(disabled=True)
    window["_TIMES_"].update(value="", disabled=True)
    window["_NOTES_"].update(value="", disabled=True)
    window["_CANCEL_"].update(disabled=True)
    window["_SUBMIT_"].update("Submit Plot", disabled=True)


def getStages(secondColumn, values):
    stageOptions = ["GUTTER KIT", "DOWNPIPE KIT", "GAS KIT", "1ST FIX KIT", "SOILS KIT",
        "SHOWER TRAY", "HEATING & BATH", "FIX 2", "SANI", "FIX 3", "FINALS", "FIX 4"]
    stageIndex = 0
    stages = []
    for list in secondColumn[1:]:
        for widget in list:
            if values[widget.key] == True:
                stages.append(stageOptions[stageIndex])
            stageIndex += 1
    return stages

def confirm(callOffDict, stages):
    confirmationList = []
    for plot in callOffDict:
        plotStages = ""
        for stage in stages[plot]:
            plotStages = f"{plotStages}, {stage}"
        plotStages = plotStages[1:]
        confirmationList.append(f"Plot {plot}, {callOffDict[plot][4]} {callOffDict[plot][5]} - {plotStages}")
        confirmationList.append(f"Notes: {callOffDict[plot][7]}")
    confirmationColumn = [
        [sg.Text("Is this information correct?")],
        [sg.Listbox(values=(confirmationList), size=(100,10), key="_CONFIRM LIST_")],
        [sg.Button("Confirm", key="_CONFIRM_"), sg.Button("Cancel", key="_CANCEL CONFIRM_")]
    ]
    confirmWindow = sg.Window("Confirm", confirmationColumn, finalize=True)

    while True:
        event, values = confirmWindow.read()

        if event == sg.WINDOW_CLOSED:
            return False

        if event == "_CONFIRM_":
            confirmWindow.close()
            return True

        if event == "_CANCEL CONFIRM_":
            confirmWindow.close()

def callOff(callOffDict, stages):
    # Loop through all plots in dictionary
    for plot in callOffDict:
        plotStages = stages[plot] 
        # Get developer and site names from the dictionary
        developer = callOffDict[plot][0]
        site = callOffDict[plot][1]
        # Get the plot number from the dictionary
        plotNumber = callOffDict[plot][2]
        # If the plot number is only 1 digit, add two zeros so it can be used
        # to correctly filter results in Pegasus
        if len(plotNumber) == 1:
            paddedNumber = f"00{plotNumber}"
        # If the plot number is only 2 digits, add one zero so it can be used
        # to correctly filter results in Pegasus
        elif len(plotNumber) == 2:
            paddedNumber = f"0{plotNumber}"
        # If the plot number is 3 digits, there is no need to add extra zeros,
        # so for consistancy just make paddedNumber the same as plotNumber
        else:
            paddedNumber = plotNumber
        # Get the first half of the job number for the given site
        siteNumber = jobDetails[developer][site][0]
        contractsManager = jobDetails[developer][site][1]
        # Combine the first half of the job number for the given site with the plot number half
        filterNumber = f"{siteNumber}{paddedNumber}"

        if "SHOWER TRAY" in plotStages:
                plotStages.append("MID FIX")

        phaseNumbers = []
        # Loop through plot stages
        for stage in plotStages:
            # Check if the relevant phase number has already been added to the phaseNumbers list
            if phaseDetails[stage] not in phaseNumbers:
                # Add phase number to phaseNumbers
                phaseNumbers.append(phaseDetails[stage])
        # Filter orders on Pegasus by filterNumber and phaseNumbers
        recordsFound = filter(filterNumber, phaseNumbers)
        # If the list is not empty, read through orders
        if recordsFound:
            requiredOrders = read(plotStages, plot)

            ####### If here we check to see the supplier of each order, we should be able to consolidate all the information
            ####### into just x keys where x is the number of suppliers
            
            suppliers = []
            # Fill out a call off sheet for each order found
            for order in requiredOrders:

                ###
                if requiredOrders[order][1] not in suppliers:
                    suppliers.append(requiredOrders[order][1])
                
            PONumbers = {}
            fileNames = {}

            for supplier in suppliers:
                PONumbers[supplier] = []
                fileNames[supplier] = []
                for order in requiredOrders:
                    if requiredOrders[order][1] == supplier:
                        PONumbers[supplier].append(order)
                        fileNames[supplier].append(requiredOrders[order][0])

            for supplier in PONumbers:
                numberList = ", ".join(PONumbers[supplier])
                filename = ", ".join(fileNames[supplier])
                filename = filename.lower()
                # # This is purely for shortening the length of the code for the next line
                # d = callOffDict[plot]
                # sheetData = [d[0], d[1], d[2], order, d[4], d[5], contractsManager, d[6]]
                callOffDict[plot][3] = numberList
                sheetData = callOffDict[plot]

                if sheetData[5] == "":
                    sheetData[5] = " "
                if sheetData[7] == "":
                    sheetData[7] = " "
                # Fill sheet with data for this order
                # fillSheet(sheetData, requiredOrders[order][0])
                fillSheet(sheetData, filename)
                # print(f"Call off note for {order} ({sheetData[4], sheetData[5]})")
                print(f"Call off note for {numberList} ({sheetData[4], sheetData[5]})")
            windowSelect("Console")


def windowSelect(window):
    """The purpose of this function is to focus the chosen program.
    
    Parameters:
    window(string): The name of the program to focus
    
    Returns:
    Nothing"""
    if window == "Pegasus":
        # Get first window with this title
        pegasus = pag.getWindowsWithTitle("Pegasus CIS - K A Watts Plumbing & Heating Ltd")[0]
        # Maximize and focus this window
        pegasus.maximize()
        pegasus.activate()
    elif window == "Excel":
        # Get first window with this title
        excel = pag.getWindowsWithTitle("Call Off Sheet - Excel")[0]
        # Maximize and focus this window
        excel.maximize()
        excel.activate()
    elif window == "Self":
        # Get first window with this title
        self = pag.getWindowsWithTitle(formTitle)[0]
        # Focus this window
        self.activate()
    elif window == "Console":
        # Get first window with this title
        console = pag.getWindowsWithTitle(consoleTitle)[0]
        # Focus this window
        console.activate()

def pegasusWindowSelect(window):
    """The purpose of this function is to focus the Pegasus program, and
    then focus the needed window within Pegasus. This function assumes
    that the windows were opened in this order:
    'Purchase Orders'
    'Purchase Order List'
    'Purchase Order Items'
    'All Purchase Orders'
    'All Purchase Order List'
    'All Purchase Order Items'

    Parameters:
    window(int): A number from 1-6 referencing one of the six windows in
    Pegasus

    Returns:
    Nothing"""
    # Make sure Pegasus is the active window
    windowSelect("Pegasus")
    # Open the "Window" drop down at the top of the screen
    pag.hotkey("alt", "w")
    # Press the appropriate number for the window desired
    if window == 1:
        pag.press("1")
    elif window == 2:
        pag.press("2")
    elif window == 3:
        pag.press("3")
    elif window == 4:
        pag.press("4")
    elif window == 5:
        pag.press("5")
    elif window == 6:
        pag.press("6")

def filter(jobNumber, phaseNumbers):
    """The purpose of this function is to filter purchase orders by a
    job number and one or more phase numbers.
    
    Parameters:
    jobNumber(string): The job number to filter
    phaseNumbers(list(strings)): The phase number/s to filter
    
    Returns:
    A boolean to indicate whether any records were found for the given filter"""

    # Select the "All Purchase Order List" window
    pegasusWindowSelect(5)

    # Clear existing filter
    pag.hotkey("ctrl", "f6")
    # Open filter window
    pag.press("f6")
    time.sleep(1)
    # Open the advanced section
    pag.hotkey("alt", "v")

    ### Add expression to filter by job number

    # Focus "Field Name" drop down
    pag.hotkey("alt", "n")

    # If "Field Name" not set to "Default Job Number", set it correctly
    if pag.locateOnScreen(defaultJobNumber) == None:
        cycle = True
        while cycle:
            pag.press("d")
            if pag.locateOnScreen(defaultJobNumber) != None:
                cycle = False
    
    # Focus input field
    pag.press("tab", presses=2)
    # Enter job number
    pag.write(jobNumber)
    # Add to filter expressions
    pag.hotkey("alt", "a")
    # pag.press("alt")
    # pag.press("a")

    ### Add one or more expressions to filter by phase numbers

    # Loop x times where x is the number of phase numbers to filter by
    for number in phaseNumbers:
        # Focus "Field Name" drop down
        pag.hotkey("alt", "n")

        # If "Field Name", not set to "Cost Phase Type", set it correctly
        ## This is the only option beginning with "C", meaning there is
        ## no need to cylce through different options until landing on the right one.
        pag.press("c")

        # Focus input field
        pag.press("tab", presses=2)

        # Enter phase number
        pag.write(number)

        # Add to filter expressions
        pag.hotkey("alt", "a")


    # Set and/or logic to filters if filtering by more than one phase number
    if len(phaseNumbers) > 1:
        # Select filters
        pag.hotkey("shift", "tab")

        # Move to first filter
        pag.press("pgup")

        # Move past first filter (job number) and second filter (first phase number)
        pag.press("down", presses=2)


        # Loop x times where x is the number of phase numbers - 1
        for i in range(len(phaseNumbers) - 1):
            # Set relationship to "Or"
            pag.hotkey("alt", "o")
            # Return selection to current filter
            pag.press("tab", presses=5)
            # Move to next filter (if this is the last filter, this won't affect anything)
            pag.press("down")

        # Select all filters
        ## For some reason you need to use both the left and right shift keys in order
        ## to select the items in the list in this instance.
        ## https://stackoverflow.com/questions/56949628/keydown-function-not-working-with-shift-key
        pag.hotkey("shiftleft", "shiftright", "pgup")
        # Remove job number filter from selection
        pag.hotkey("shiftleft", "shiftright", "down")
        # Group phase number filters
        pag.hotkey("alt", "g")

    # Close advanced section
    pag.hotkey("alt", "v")
    # Move selection to "OK"
    pag.press("tab")
    # Filter purchase orders
    pag.press("Enter")

    # Check if any records were found
    time.sleep(0.5)
    if pag.locateOnScreen(emptyList) != None:
        print(f"No records found for the given filter ({jobNumber}, {phaseNumbers}")
        return False
    else:
        return True

def read(stagesRequired, plot):
    """The purpose of this function is to read information from every order
    in a filtered list. It takes the PO number, the 'Manufacturer Code' (the
    name of the stage the order is for) and in the future it should look at
    the supplier to be able to group PO numbers from the same supplier.
    
    Parameters:
    stagesRequired(list(strings)): The stage/s that need to be called off
    plot(string): The number of the current plot
    
    Returns:
    A dictionary containing PO numbers as keys, and stages and suppliers as values
    Dictionary format is as follows:
    requiredOrders = {PONumber: [code, supplier]}"""

    recognisedNotes = ["All delivery drivers must report to the site team on arrival, \r\nAll delivery drivers must wear High Viz Vest, Hard Hat, Safety foot wear and gloves.", ""]
    requiredOrders = {}

    # Create a dictionary used for counting the number of orders placed per stage required
    ordersPerStage = {}
    for stage in stagesRequired:
        ordersPerStage[stage] = 0

    # Select the "All Purchase Orders" window
    pegasusWindowSelect(4)
    # Find location of window
    allPurchaseOrders = pag.locateOnScreen(win4)
    pag.moveTo(allPurchaseOrders)
    pag.move(25, 50)
    headerNotes = pag.position()

    # Select the "All Purchase Order List" window
    pegasusWindowSelect(5)

    # Move selection to the PO column
    pag.press("home")
    ## We need the last PO number in the list, which f12 will take us to, but if the
    ## selection was already in the last row and a column was selected, although the
    ## correct cell will be selected, the number will not be highlighted. To guarantee
    ## selection of the number, first select the first cell in the list, then the last
    pag.press("f9")
    pag.press("f12")
    # Copy PO number to clipboard and save to variable finalPO
    copy()
    finalPO = pyp.paste()
    # Return to the first order in the list
    pag.press("f9")

    # Begin a loop until the final order has been reached
    reading = True
    while reading:
        # Select the "All Purchase Order List" window
        pegasusWindowSelect(5)
        # Copy PO number to clipboard and save to variable currentPO
        copy()
        currentPO = pyp.paste()
        # Select current order
        pag.press("enter")
        # Check header notes
        pegasusWindowSelect(4)
        pag.hotkey("alt", "n")
        pag.click(headerNotes, button="right")
        pag.press("a")
        copy()
        currentNotes = pyp.paste()
        # Select the "All Purchase Order List" window
        pegasusWindowSelect(5)
        # Move to the supplier column, copy the value and save to variable currentSupplier
        ## This assumes that the supplier column is 2 to the right of the PO number. Make
        ## sure that this is the case otherwise it will pick up the wrong information.
        ### Previously used the code "pag.press("right", presses = 2)". For some reason
        ### this caused an error where it would select multiple cells simaltaneously,
        ### something I've not been able to replicate manually. Either way, this seems
        ### to fix it.
        pag.press("right")
        pag.press("right")
        copy()
        currentSupplier = pyp.paste()

        # Change to the "All Purchase Order Items" window
        pegasusWindowSelect(6)
        # Open the "All Purchase Order Item List" window
        pag.hotkey("alt", "l")
        # Move to the "Manufacturer Code" column, copy the value and save to variable
        # currentCode
        # pag.press("right", presses=5)
        # Using this for the same reason as a few lines earlier
        pag.press("right")
        pag.press("right")
        pag.press("right")
        pag.press("right")
        pag.press("right")
        pag.press("right")
        copy()
        currentCode = pyp.paste()
        # Clost the "All Purchase Order Item List" window
        pag.hotkey("alt", "c")

        # Select the "All Purchase Order List" window
        pegasusWindowSelect(5)
        # Return to the PO number coloumn and move to the next order
        pag.press("home")
        pag.press("f11")

        # Check if this purchase order is required
        if currentCode in stagesRequired:
            # Add details of this order to requiredOrders
            requiredOrders[currentPO] = [currentCode, currentSupplier, currentNotes]
            # Keep track of how many orders exist for each code
            ordersPerStage[currentCode] += 1
        # Catch unusual codes
        ## Not the cleanest solution, but it should do for now
        elif currentCode == "HEATING" and "HEATING & BATH" in stagesRequired:
            requiredOrders[currentPO] = [currentCode, currentSupplier, currentNotes]
            if currentCode in ordersPerStage:
                ordersPerStage[currentCode] += 1
            else:
                ordersPerStage[currentCode] = 1
            print(f"Plot {plot}: Found 'HEATING' order ({currentPO})")
        elif currentCode == "BATH" and "HEATING & BATH" in stagesRequired:
            requiredOrders[currentPO] = [currentCode, currentSupplier, currentNotes]
            if currentCode in ordersPerStage:
                ordersPerStage[currentCode] += 1
            else:
                ordersPerStage[currentCode] = 1
            print(f"Plot {plot}: Found 'BATH' order ({currentPO})")
        elif currentCode == "2ND FIX KIT" and "HEATING & BATH" in stagesRequired:
            requiredOrders[currentPO] = [currentCode, currentSupplier, currentNotes]
            if currentCode in ordersPerStage:
                ordersPerStage[currentCode] += 1
            else:
                ordersPerStage[currentCode] = 1
            print(f"Plot {plot}: Found '2ND FIX KIT' order ({currentPO})")
        elif currentCode == "2ND FIX KIT" and "SANI" in stagesRequired:
            requiredOrders[currentPO] = [currentCode, currentSupplier, currentNotes]
            if currentCode in ordersPerStage:
                ordersPerStage[currentCode] += 1
            else:
                ordersPerStage[currentCode] = 1
            print(f"Plot {plot}: Found '2ND FIX KIT' order ({currentPO})")
        elif currentCode == "2ND FIX FITTINGS" and "FIX 2" in stagesRequired:
            requiredOrders[currentPO] = [currentCode, currentSupplier, currentNotes]
            if currentCode in ordersPerStage:
                ordersPerStage[currentCode] += 1
            else:
                ordersPerStage[currentCode] = 1
            print(f"Plot {plot}: Found '2ND FIX FITTINGS' order ({currentPO})")

        # End loop after reading final order in list
        if currentPO == finalPO:
            reading = False

    # Check for any duplicate orders and remove them, printing a note to the console with
    # the relevant details
    ## I'm not very happy with this solution, but it seems to work, so it can stay for now
    
    # A list to contain codes which have more than one order associated with them
    duplicates = []

    # Remove redundant key from ordersPerStage if calling off shower tray/mid fix
    if "SHOWER TRAY" in ordersPerStage and "MID FIX" in ordersPerStage:
        if ordersPerStage["SHOWER TRAY"] != 0 and ordersPerStage["MID FIX"] == 0:
            ordersPerStage.pop("MID FIX")
        elif ordersPerStage["MID FIX"] != 0 and ordersPerStage["SHOWER TRAY"] == 0:
            ordersPerStage.pop("SHOWER TRAY")
            
    # Loop through all orders found
    for key in ordersPerStage:
        # If there is more than one order for this code, add it to duplicates
        if ordersPerStage[key] > 1:
            duplicates.append(key)
        elif ordersPerStage[key] == 0:
            print(f"No orders found for plot {plot} {key}")
    # for stage in stagesRequired:
    #     print(stage, ordersPerStage)
    #     if stage not in ordersPerStage:
    #         print(f"No orders found for plot {plot} {stage}")

    # A list to contain order numbers which need to be removed from the requiredOrders dictionary
    toPop = []
    # Loop through the duplicates list
    for code in duplicates:
        # Loop through the requiredOrders dictionary
        for key in requiredOrders:
            # If the code for this order is on the duplicates list, print the details to the
            # console and add the order number to the toPop list. The reason for not popping it
            # here is that editing the dictionary while looping through it causes errors
            if requiredOrders[key][0] == code:
                print(f"Plot {plot} duplicate order found: {key} - {code}")
                toPop.append(key)
    # Remove all duplicate orders from the requiredOrders dictionary
    for key in toPop:
        requiredOrders.pop(key)

    # Make a note of any orders that have unexpected notes
    for key in requiredOrders:
        if requiredOrders[key][2] not in recognisedNotes:
            print(f"Check {key} notes before sending call off.")
    return requiredOrders

def fillSheet(sheetData, fileName):
    # Select the call off sheet
    windowSelect("Excel")
    # Move select the cell in the top left corner of the sheet
    pag.hotkey("ctrl", "home")
    # Navigate to the developer name cell
    pag.press("right")
    pag.press("down")
    # Move down through the cells on the sheet, filling in the appropriate data for each
    for item in sheetData:
        pag.write(item)
        pag.press("down")
    # Save as
    pag.press("f12")
    # Wait until the "Save As" window has appeared
    waitWindow("Save As")
    # Select the file type drop down
    pag.press("tab")
    # Select PDF as file type
    pag.press("p")
    # Return to the file name input box
    pag.hotkey("shift", "tab")
    # Enter the name of the file
    if fileName != "1ST FIX KIT":
        pag.write(f"Plot {sheetData[2]} {fileName.title()} Call off sheet.pdf")
    else:
        pag.write(f"Plot {sheetData[2]} 1st Fix Kit Call of sheet.pdf")
    # Save
    pag.press("enter")
    # If the file name already exists
    time.sleep(0.1)
    if "Confirm Save As" in pag.getAllTitles():
        # File already exists
        print(f"Tried to save 'Plot {sheetData[2]} {fileName.title()} Call off sheet.pdf', but the file already exists")
        # Print call off sheet data to console so that it isn't lost
        for item in sheetData:
            print(item)
        # Do not overwrite existing file
        pag.press("enter")
        # Close "Save As" window
        pag.press("esc")
    time.sleep(2)

def pegasusSetUp(type):
    """The purpose of this function is to open the necessary windows in Pegasus in the
    correct order so that this program can properly interact with them.
    
    Parameters:
    type(string): Has a value of either 'complete', or 'allPO'. This is used
    to allow this function to either open all the windows, or only some of them.
    
    Returns:
    Nothing"""

    windowSelect("Pegasus")

    # "complete" is for opening all six required windows
    if type == "complete":
        # First ensure that all other windows are closed
        ## In reality this may technically not close all windows if the user has all
        ## sorts of unexpected windows open, but I'm just going to trust that the
        ## user won't be dumb
        # Do this twice
        for i in range (2):
            # Select the first window, should be either purchase orders or all purchase orders
            pegasusWindowSelect(1)
            # Close this window
            pag.hotkey("alt", "c")
        # Wait until the background is visible
        while pag.locateOnScreen(pegasusBackground) == None:
            pass
        # Right click the screen
        pag.click(pag.locateOnScreen(pegasusBackground), button = "right")
        # Do this twice
        for i in range(2):
            # Move to the option for opening the "Purchase Orders" window
            pag.press("down", presses = 2)
            pag.press("right")
        # Open "Purchase Orders"
        pag.press("enter")
        # Wait for "Purchase Orders to open"
        while pag.locateOnScreen(win1) == None:
            pass
        # Open the "Purchase Order List" window and wait for it to open
        pag.hotkey("alt", "l")
        while pag.locateOnScreen(win2) == None:
            pass    
        pegasusWindowSelect(1)
        # Open the "Purchase Order Items" window and wait for it to open
        pag.hotkey("alt", "i")
        pag.press("1")
        while pag.locateOnScreen(win3) == None:
            pass
    
    # "allPO" is for opening only the last 3 windows
    if type == "allPO":
        # Close "All Purchase Orders"
        pegasusWindowSelect(4)
        pag.hotkey("alt", "c")
    # Wait until the background is visible
    while pag.locateOnScreen(pegasusBackground) == None:
        pass
    # Right click the screen
    pag.click(pag.locateOnScreen(pegasusBackground), button = "right")
    # Do this twice
    for i in range(2):
        # Move to the option for opening the "All Purchase Orders" window
        pag.press("down", presses = 2)
        pag.press("right")
    pag.press("up")
    pag.press("right", presses = 2)
    pag.press("up", presses = 2)
    pag.press("right")
    # Open "All Purchase Orders"
    pag.press("enter")
    # Wait for "All Purchase Orders to open"
    while pag.locateOnScreen(win4) == None:
        pass
    # Open the "All Purchase Order List" window and wait for it to open
    pag.hotkey("alt", "l")
    while pag.locateOnScreen(win5) == None:
        pass
    # Open the "Purchase Order Items" window and wait for it to open
    pegasusWindowSelect(4)
    pag.hotkey("alt", "i")
    while pag.locateOnScreen(win6) == None:
        pass


def copy():
    """Uses the keyboard shortcut 'ctrl' + 'c'"""
    pag.hotkey("ctrl", "c")
    time.sleep(0.1)

def clear():
    """Clears the console"""
    os.system('cls')

def input_with_default(prompt_, default_):
    """Takes user input, but pre-fills the text, which the user can either use
    or override"""
    keyboard.write(default_)
    return input(prompt_)

def waitWindow(name):
    """Wait for the specified window to appear"""
    # Loop until window called "name" has appeared
    waiting = True
    while waiting:
        # Get a list of all window titles
        windows = pag.getAllTitles()
        # If the specified name exists in "windows", focus that window and end the loop
        if name in windows:
            window = pag.getWindowsWithTitle(name)[0]
            window.activate()
            waiting = False

if __name__ == "__main__":
    main()
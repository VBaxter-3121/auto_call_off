# If you need to update this, please follow these instructions very carefully:
# First you need to understand the basic structure of the dictionary.
# "jobDetails" is the top level of the dictionary. This contains all the names
# of the developers. Each developer name contains a smaller dictionary, with
# names for each of the sites pertaining to that developer. Each level of the
# dictionary has been indented to try to make it clearer how it is structured.
# Each site contains a list of information in the following order: job number
# (only the first half up to and including the hyphen), the name of the
# contracts manager, and an abbreviation for the site. Each item in the
# dictionary must end with a comma, except for the last item. This means that
# after each site, the closing square bracket must be followed by a comma,
# except the last site. Likewise, after each devloper, the closing curly
# bracket must be followed by a comma, except for the last developer.

# Add a new developer:
# Step 1. Find where in the list of developers the new developer would go
# alphabetically.
# Step 2. Find the closing bracket of the developer that will come immediately
# before the new one.
# Step 3. Press enter to make a new line after this one.
# Step 4. Copy and paste the following template (make sure to remove the "#"
# at the beginning of each line):
# "Developer Name": {
#       "Site Name": ["000-", "Contracts Manager", "Dev-Ste"]
# }
# (You may need to add indentations to make it line up with the rest of the
# dictionary)
# Step 5. Edit the information in the template to suit your needs. You can add as
# many sites as you like, just make sure to end each one except the last with a
# comma
# Step 6. Unless this is the last developer in the list, make sure to place a
# comma after the closing curly bracket. Likewise, if the previous developer was 
# the last in the list before, add a comma after its closing curly bracket.
# Step 7. Save the file and follow the instructions for compiling the application.

# Add a new site:
# Step 1. Find the developer of the new site, and find where in the existing list
# of sites the new one will go alphabetically.
# Step 2. Create a new line for the new site.
# Step 3. Copy and past this template (make sure to remove the "#" at the beginning
# of the line):
# "Site Name": ["000-", "Contracts Manager", "Dev-Ste"]
# (You may need to add indentations to make it line up with the rest of the
# dictionary)
# Step 5. Edit the information in the template to suit your needs. You can add as
# many sites as you like, just make sure to end each one except the last with a
# comma
# Step 6. Save the file and follow the instructions for compiling the application.

# Compile the application:
# Step 1. Open Command Prompt (you can do this by going to the search bar on the
# Windows task bar, typing "cmd" and pressing enter).
# Step 2. In File Explorer, navigate to the "main" folder (this should be one
# level higher than the folder where this file is contained).
# Step 3. Click in the bar at the top of the window, which will select the exact
# file path for the folder. Copy that path.
# Step 4. In Command Prompt, type the following command, and then press enter:
# cd *File Path Here*
# Example: cd C:\Users\vincent.baxter\OneDrive - K A WAtts\Documents\Git\auto_call_off\main
# Step 5. In the main folder, there should be a file called "pyinstaller
# instruction". Open this file, and copy it's entire contents.
# Step 6. Paste your clipboard into Command Prompt and press enter. This may take
# a few moments to complete.
# You may be given the following prompt:
# WARNING: The output directory *Your file path* and ALL ITS CONTENTS will be REMOVED!
# Continue? (y/N)
# If you see this, just type "y" and press enter
# Step 7. When it has finished, refresh File Explorer, and then go to the "dist"
# folder.
# Step 8. Check that the "Auto_Call_Off" has been updated (check the date modified
# column and make sure it shows the current date and time).
# Step 9. Copy that folder, and place it wherever you wish, you can replace your
# previous version with this new version if you like (though you may want to
# confirm that everything works correctly before you do).
# Step 10. Inside that folder is a file called "Auto_Call_Off". This is the file
# that you will run to use the program. You can make a shortcut to this and place
# it anywhere you wish (note: if you replaced the previous folder you had with the
# new one, any existing shortcuts won't work correctly, so you will need to make
# a new one).

# If you encounter any problems, please try to resolve the issue yourself, carefully
# following the instructions, but if you are unable to solve the issues and need
# help, you can contact me with my e-mail address: vmbaxter@hotmail.co.uk

jobDetails = {
    "BDW": {
        "Bordon": ["177-", "Liam Adams", "BDW-Brd"],
        "Canford Paddock": ["171-", "Andy Knight", "BDW-CfP"],
        "Compass Point Ph2": ["182-", "Andy Knight", "BDW-CmP"],
        "Harbour Place": ["179-", "Liam Adams", "BDW-HbP"],
        "Forest Walk": ["254-", "Ben Adams", "BDW-FsW"],
        "Madgwick Park": ["172-", "Liam Adams", "BDW-MwP"],
        "Niveus Walk": ["181-", "Andy Knight", "BDW-NvW"],
        "Park Prewett": ["251-", "Chris Matthews", "BDW-PPw"],
        "Quarter Jack Park": ["175-", "Andy Knight", "BDW-QJP"],
        "SGG Ph2A": ["180-", "Pete Bundy", "BDW-SGG2A"],
        "SGG Ph2B": ["178-", "Pete Bundy", "BDW-SGG2B"]
    },
    "Bellway": {
        "Boorley Park": ["718-", "Andy Knight", "Bel-BlP"],
        "Salisbury": ["714-", "Andy Knight", "Bel-Slb"],
        "Sherfield on Loddon": ["717-", "Andy Knight", "Bel-SoL"],
        "Blandford Ph1": ["713-", "Andy Knight", "Bel-Bfd1"],
        "Blandford Ph2": ["715-", "Andy Knight", "Bel-Bfd2"],
        "Blandford Ph3": ["716-", "Andy Knight", "Bel-Bfd3"],
        "Sturminster": ["719-", "Andy Knight", "Bel-Sms"]
    },
    "Bloor Homes": {
        "Boorley Green": ["736-", "Ben Adams", "Blr-BlG"]
    },
    "Bovis Homes": {
        "WHF 3C": ["6006-", "Ben Gough", "Bvs-WHF3C"]
    },
    "Cala Homes": {
        "Alton": ["512-", "Chris Matthews", "Cal-Atn"],
        "Liss": ["511-", "Chris Matthews", "Cal-Lis"],
        "Deepcut": ["504-", "Chris Matthews", "Cal-Dpc"]
    },
    "Crest Nicholson": {
        "Arbourfield": ["5019-", "Chris Matthews", "CsN-Abf"]
    },
    "Dandara": {
        "Fontwell Ph1": ["7101-", "Ben Gough", "Ddr-Fwl1"],
        "Fontwell Ph2": ["7103-", "Ben Gough", "Ddr-Fwl2"],
        "Drayton": ["7100-", "Liam Adams", "Ddr-Dyt"],
        "Yapton": ["7102-", "Ben Gough", "Ddr-Ypt"]
    },
    "David Wilson Homes": {
        "SGG": ["250-", "Pete Bundy", "DWH-SGG"]
    },
    "Foreman Homes": {
        "Alton": ["6004-", "Chris Matthews", "FmH-Atn"],
        "Alton Ph2": ["6009-", "Chris Matthews", "FmH-Atn2"],
        "Whiteley": ["6008-", "Ben Adams", "FmH-Wtl"]
    },
    "Hampshire Homes": {
        "Fontwell": ["9007-", "Liam Adams", "HpH-Fwl"]
    },
    "Hill Development": {
        "North Town": ["8004-", "Steve Jordan", "Hil-NrT"],
        "Amber House": ["8005-", "Paul Smithson", "Hil-AbH"]
    },
    "Inland Homes": {
        "Meridian Block C": ["3009-", "Reg Noyce", "IlH-Mrd"]
    },
    "Linden Homes": {
        "Alderbury": ["356-", "Andy Knight", "Ldn-Adb"],
        "Boorley PhB4": ["355-", "Ben Adams", "Ldn-BrlB4"],
        "Boorley PhB6": ["352-", "Ben Adams", "Ldn-BrlB6"],
        "WHF Ph2B": ["351-", "Ben Adams", "Ldn-WHF2B"],
        "WHF Ph3C": ["354-", "Ben Gough", "Ldn-WHF3C"],
        "WHF Ph5G": ["357-", "Ben Gough", "Ldn-WHF5G"],
        "WHF Ph6I": ["358-", "Ben Gough", "Ldn-WHF6I"],
        "Whiteley": ["353-", "Ben Adams", "Ldn-Wtl"]
    },
    "McCarthy & Stone": {
        "Alton": ["2007-", "Steve Jordan", "McS-Atn"]
    },
    "Natta Building": {
        "Huxley Court": ["6010-", "Steve Jordan", "Nat-HxC"]
    },
    "Redrow": {
        "Harbour Views": ["7013-", "Chris Matthews", "Rdr-HbV"],
        "Hop Field Place Ph3": ["7008-", "Chris Matthews", "Rdr-HFP"],
        "New Fields": ["7011-", "Chris Matthews", "Rdr-NFd"],
        "Orchids Place": ["7007-", "Chris Matthews", "Rdr-OcP"],
        "Windmill Views": ["7012-", "Chris Matthews", "Rdr-WmV"]
    },
    "Taylor Wimpey": {
        "Broadleaf Park": ["4056-", "Ben Adams", "TlW-BlP"],
        "Shopwhyke Lakes": ["4058-", "Ben Adams", "TlW-SwL"],
        "Westergate": ["4053-", "Ben Adams", "TlW-Wtg"]
    }
}
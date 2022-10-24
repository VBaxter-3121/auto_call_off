from windows.home import Home
from windows.group_data import GroupData
from windows.plot_data import PlotData

home = Home()
group = GroupData("Test Name")
plot = PlotData("Test Name", [1, 2, 3])

homeWindow = home.getWindow()
groupWindow = group.getWindow()
plotWindow = plot.getWindow()

for i in range(100):
    event, values = homeWindow.read()

for i in range(100):
    event, values = groupWindow.read()

for i in range(100):
    event, values = plotWindow.read()
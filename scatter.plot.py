import json
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects


o = open("data.json")
data = json.load(o)
o.close()

precipitationlist = []
for items in data:
    precipitation= items["Precipitation probability"]
    precipitationlist .append(precipitation)

daylist = []
for items in data:
    day = items["Day"]
    daylist.append(day)

colors = precipitationlist

plt.scatter(daylist,precipitationlist ,c=colors,cmap="hsv",)
plt.title("Precipitation probability graph".upper(), color="#8B0000", fontweight="bold",fontsize=12)
plt.ylabel("Precipitation probability %".upper(),color="#8B0000",fontweight="bold",fontsize=12)
plt.xlabel("Day".upper(),fontsize=14, color="#8B0000",fontweight="bold",)

plt.colorbar()
plt.show()

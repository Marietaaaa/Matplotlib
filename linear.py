import json
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.patheffects as path_effects


o = open("data.json")
data = json.load(o) 
o.close()

templist = []
for items in data:
    temp = items["Temperature"]
    templist.append(temp)

daylist = []
for items in data:
    day = items["Day"]
    daylist.append(day)
    
fig, bx = plt.subplots()
line1, = bx.plot([24, 26, 24, 22, 23, 21, 22], marker='o', label='line 1')
bx.legend(handler_map={line1: HandlerLine2D(numpoints=1)})

plt.plot([24, 26, 24, 22, 23, 21, 22], linewidth=5, color='#8B3626',
    path_effects=[path_effects.SimpleLineShadow(),path_effects.Normal()])

plt.plot(daylist,templist, color='#8B3626')
plt.title("TEMPERATURE GRAPH", color='#27408B',fontweight="bold")
plt.ylabel("TEMPERATURE °C",color='#27408B',fontweight="bold")
plt.xlabel("DAY", color='#27408B',fontweight="bold")

plt.show()

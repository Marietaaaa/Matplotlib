import json
import matplotlib
import matplotlib.pyplot as plt

o = open("data.json")
data = json.load(o)
o.close()

windlist = []
for items in data:
    wind = items["Wind speed"]
    windlist.append(wind)

legend = []
for items in windlist:
    items = str(items) + " km/h"
    legend.append(items)


daylist = []
for items in data:
    day = items["Day"]
    daylist.append(day)

plt.title("Wind speed graph".upper(),color='black', size=17, fontweight="bold")
plt.pie(windlist, labels=daylist)
plt.legend(legend)
plt.show()

import json
import matplotlib
import matplotlib.pyplot as plt

o = open("data.json")
data = json.load(o)
o.close()

weatherlist = []
for items in data:
    weather = items["Weather"]
    weatherlist.append(weather)

plt.title("Weather graph", size=17, color='#CD9B1D', fontweight="bold")
plt.ylabel("Days", fontsize="14", color="#CD9B1D", fontweight="bold")
plt.xlabel("Weather", fontsize="14", color="#CD9B1D", fontweight="bold")

plt.hist(weatherlist,color="green")
plt.show()

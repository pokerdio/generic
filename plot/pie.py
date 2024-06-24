"""
===============
Basic pie chart
===============

Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
import matplotlib.pyplot as plt

plt.rcdefaults()
plt.style.use("dark_background")



def getCol(map_name, count): 
    data_values = np.linspace(0, 1, count)  # Example data values from 0 to 1
    cmap = plt.cm.get_cmap(map_name)
    return [cmap(value) for value in data_values]
    
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0.03, 0.15, 0.03, 0.03)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=False, startangle=90)
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90,  
        colors=getCol("magma", len(sizes) + 5)[:len(sizes)],
        wedgeprops={'edgecolor': 'LightGreen', 'linewidth': 1.5})


ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

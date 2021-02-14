import pandas as pd
import csv
import matplotlib.pyplot as plt

point = [[-34.61315, 42.33143, 12.97194, -34.61315], [-58.37723, -83.04575, 77.59369, -58.37723]]
img = plt.imread("res/unnamed.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[-180, 180, -90, 90])

plt.plot(point[1], point[0], marker='o', color='red')
plt.plot(sum(point[1][:-1])/3, sum(point[0][:-1])/3, marker='o', color='red')

plt.xlim(-180, 180)
plt.ylim(-90, 90)

plt.xlabel('γ-Energy, keV')
plt.ylabel('Normilized intensity')
plt.show()

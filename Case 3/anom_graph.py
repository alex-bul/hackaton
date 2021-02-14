import pandas as pd
import csv
import matplotlib.pyplot as plt

lab1, lab2, lab3 = ['data/out' + input() for i in range(3)]

for i in [lab1, lab2, lab3]:
    with open(i, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = [line.split(" ") for line in stripped if line]
        with open('{i}.csv'.format(i=i), "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['energy', 'intensity'])
            for j in lines:
                writer.writerow([j[0], j[1]])

        df = pd.read_csv('{i}.csv'.format(i=i), encoding='cp1251')
        plt.plot(df['energy'], df['intensity'])

ax = plt.gca()


plt.xlabel('γ-Energy, keV')
plt.ylabel('Normilized intensity')
plt.show()
import pandas as pd
import csv
import matplotlib.pyplot as plt

files = [input() for i in range(3)]
end = [0 for i in range(273)]
for i in range(99):
    f = open(f'data/out{i}', 'r')
    data = f.read().split('\n')[:-1]
    for j in range(len(data)):
        end[j] += float(data[j].split()[1])

res = [end[i]/100 for i in range(273)]


for i in files:
    with open(f'data/out{i}', 'r') as file:
        stripped = (line.strip() for line in file)
        lines = [line.split(" ") for line in stripped if line]
        with open('{i}.csv'.format(i=i), "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['energy', 'intensity'])
            for j in lines:
                writer.writerow([j[0], j[1]])

        df = pd.read_csv('{i}.csv'.format(i=i), encoding='cp1251')
        plt.plot(df['energy'], df['intensity'])
f = open('data/out0')
data = [float(i.split()[0]) for i in f.read().split('\n')[:-1]]
plt.plot(data, res, color='red')
ax = plt.gca()


plt.xlabel('γ-Energy, keV')
plt.ylabel('Normilized intensity')
plt.show()
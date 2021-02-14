import csv

f = open('readable.txt', 'w')
with open('data/gamma_observ_dat.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for name, data in enumerate(reader):
        with open(f'data/{data[-1]}', 'r') as end:
            nums = end.read().split('\n')[:-1]
            for i in nums:
                f.write('\t'.join(data[1:-1]) + f' {i}' + '\n')

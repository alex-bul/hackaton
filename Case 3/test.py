end = [0 for i in range(273)]
for i in range(99):
    f = open(f'data/out{i}', 'r')
    data = f.read().split('\n')[:-1]
    for j in range(len(data)):
        end[j] += float(data[j].split()[1])

res = [end[i]/100 for i in range(273)]
flag = False

for i in range(99):
    flag = False
    f = open(f'data/out{i}', 'r')
    data = f.read().split('\n')[:-1]
    for j in range(len(data)):
        if float(data[j].split()[1])/4 > float(res[j]):
            print(i)
            flag = True
            break
    if flag:
        continue
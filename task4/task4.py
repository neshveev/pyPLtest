import sys


class Visitor:
    def __init__(self, time, action):
        self.time = time
        self.action = action


lst = []
f = open(sys.argv[1], 'r')
for line in f:
    times = line.strip().split('-')
    lst.append(Visitor(times[0], 1))
    lst.append(Visitor(times[1], -1))
lst.sort(key=lambda i: i.time)

curV = 0
maxV = 0
for i in range(len(lst)):
    curV += lst[i].action
    if curV > maxV:
        maxV = curV

curV = 0
res = []
for i in range(len(lst)):
    curV += lst[i].action
    if curV == maxV:
        res.append([lst[i].time, lst[i + 1].time])

i = 0
while i < len(res):
    print(res[i][0], end=' ')
    while i + 1 < len(res) and res[i][1] == res[i + 1][0]:
        i += 1
    print(res[i][1])
    i += 1

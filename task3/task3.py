import sys

lst = {}
max = 0
for i in range(1, 6):
    f = open(sys.argv[1] + "/cash{0}".format(i), 'r')
    for ii in range(1, 17):
        if ii not in lst:
            lst[ii] = float(f.readline())
        else:
            lst[ii] += float(f.readline())
        if lst[ii] > max:
            max = lst[ii]

for i in lst:
    if lst.get(i) == max:
        print(i)
        break

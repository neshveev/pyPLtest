import sys
import numpy as np

f = open(sys.argv[1], 'r')
l = []
for n in f:
    l.append(int(n))

print('%.2f' % np.percentile(l, 90))
print('%.2f' % np.median(l))
print('%.2f' % np.max(l))
print('%.2f' % np.min(l))
print('%.2f' % np.average(l))
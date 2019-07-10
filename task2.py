import sys


def solution(a, b, c):
    return (c[0] - a[0]) * (b[1] - a[1]) - (c[1] - a[1]) * (b[0] - a[0])


def edge(a, b, c):
    xmax = a[0] if a[0] >= b[0] else b[0]
    xmin = a[0] if a[0] <= b[0] else b[0]
    ymax = a[1] if a[1] >= b[1] else b[1]
    ymin = a[1] if a[1] <= b[1] else b[1]
    if xmin <= c[0] <= xmax and ymin <= c[1] <= ymax:
        return True
    return False


class Qu:
    def __init__(self):
        f = open(sys.argv[1], 'r')
        self.lst = []
        for dot in f:
            self.lst.append([float(i) for i in dot.split()])
        f.close()

    def where(self, dot):
        for i in range(4):
            if dot in self.lst:
                return 0
            d = solution(self.lst[i], self.lst[i + 1] if i + 1 < 4 else self.lst[0], dot)
            if d == 0:
                if edge(self.lst[i], self.lst[i + 1] if i + 1 < 4 else self.lst[0], dot):
                    return 1
                else:
                    return 3
            elif d < 0:
                return 3
        return 2


qu = Qu()
f = open(sys.argv[2], 'r')
dots = []
for d in f:
    dots.append([float(i) for i in d.split()])
for dot in dots:
    print(qu.where(dot))

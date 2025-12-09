#! /usr/bin/env python3

def find_new_range(a, b):
    if a[0] >= b[0] and a[0] <= b[1]:
        if a[1] >= b[1]:
            return [b[0], a[1]]
        return b

    if a[1] >= b[0] and a[1] <= b[1]:
        if a[0] <= b[0]:
            return [a[0], b[1]]
        return b
    
    if b[0] >= a[0] and b[0] <= a[1]:
        if b[1] >= a[1]:
            return [a[0], b[1]]
        return a

    if b[1] >= a[0] and b[1] <= a[1]:
        if b[0] <= a[0]:
            return [b[0], a[1]]
        return a

ranges = []
nx = ""
while nx := input():
    nx = nx.split("-")
    a = [int(nx[0]), int(nx[1])]
    changed = True
    while changed:
        i = 0
        changed = False
        while i < len(ranges):
            b = ranges[i]
            if b[0] >= a[0] and b[1] <= a[1]:
                ranges.remove(b)
                changed = True
                continue
            if b[0] > a[1] or b[1] < a[0]:
                i += 1
                continue
            new_range = [min(a[0], b[0]), max(a[1], b[1])]
            ranges.remove(b)
            a = new_range
            changed = True
    ranges.append(a)

tot = 0
for r in ranges:
    tot += r[1] - r[0] + 1
print(tot)

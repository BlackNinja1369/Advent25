#! /usr/bin/env python3

inp = input("")
count = 0

for ids in inp.split(","):
    ids = ids.split("-")
    for i in range(int(ids[0]), int(ids[1]) + 1):
        x = str(i)
        for j in range(1, len(x)):
            if x == x[j:] + x[:j]:
                count += i
                break

print(count)
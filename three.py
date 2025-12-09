#! /usr/bin/env python3

nx = ""
tot = 0
while nx := input(""):
    cur = ""
    idx = -1
    previdx = -1
    mx = -1
    for i in range(11, -1, -1):
        for j in range(previdx+1, len(nx) - i):
            if int(nx[j]) > mx:
                idx = j
                mx = int(nx[j])
        cur += str(mx)
        previdx = idx
        idx = -1
        mx = -1
    tot += int(cur)

            

print(tot)
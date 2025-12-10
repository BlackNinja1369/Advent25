#! /usr/bin/env python3

grid = []
nx = ""

while nx := input():
    nx = list(nx)
    grid.append(nx)

ops = []
for i in grid[-1]:
    if i != " ": ops.append(i)
grid = grid[:-1]
tot = 0
to_add = []
for j in range(len(grid[0])):
    cur = ""
    empty = True
    for i in range(len(grid)):
        if grid[i][j] != " ": empty = False
        cur += grid[i][j]
    if empty:
        if ops.pop(0) == "+":
            sum_tot = 0
            for k in to_add:
                sum_tot += int(k.strip())
            tot += sum_tot
        else:
            prod_tot = 1
            for k in to_add:
                prod_tot *= int(k.strip())
            tot += prod_tot
        to_add = []
    else:
        to_add.append(cur)

if ops.pop(0) == "+":
    sum_tot = 0
    for k in to_add:
        sum_tot += int(k.strip())
    tot += sum_tot
else:
    prod_tot = 1
    for k in to_add:
        prod_tot *= int(k.strip())
    tot += prod_tot


print(tot)
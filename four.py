#! /usr/bin/env python3

grid = []
gridcheck = []

nx = ""
while nx := input():
    nx = list(nx)
    grid.append(nx)
    gridcheck.append(nx.copy())

tot = 0
curtot = 0
while True:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.': continue
            cur = 0
            if i > 0:
                if j > 0 and grid[i-1][j-1] == '@':
                    cur += 1
                if j < len(grid[0]) - 1 and grid[i-1][j+1] == '@':
                    cur += 1
                if grid[i-1][j] == '@':
                    cur += 1
            
            if i < len(grid) - 1:
                if j > 0 and grid[i+1][j-1] == '@':
                    cur += 1
                if j < len(grid[0]) - 1 and grid[i+1][j+1] == '@':
                    cur += 1
                if grid[i+1][j] == '@':
                    cur += 1
            
            if j > 0 and grid[i][j-1] == '@':
                cur += 1
            if j < len(grid[0]) - 1 and grid[i][j+1] == '@':
                cur += 1

            if cur < 4:
                curtot += 1
                grid[i][j] = '.'
    if curtot == 0:
        break
    tot += curtot
    curtot = 0

print(tot)
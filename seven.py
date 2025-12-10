#! /usr/bin/env python3

q = []
grid = []
nx = ""
while nx := input():
    grid.append(list(nx))

start = None

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)
            break
    if start != None:
        break

cache = {}

def dfs(y, x):
    res = cache.get((y, x), -1)
    if res != -1: return res
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return 1
    if grid[y][x] == '^':
        cur = 0
        cur += dfs(y, x+1)
        cur += dfs(y, x-1)
        cache[(y, x)] = cur
        return cur
    else:
        cur = dfs(y+1, x)
        cache[(y, x)] = cur
        return cur
print(dfs(start[0], start[1]))

#! /usr/bin/env python3

def fill_edges(k, j, pos, grid):
    a = pos[k]
    b = pos[j]
    grid[a[1]][a[0]] = '#'
    grid[b[1]][b[0]] = '#'
    if a[0] == b[0]:
        mx = max(a[1], b[1])
        mn = min(a[1], b[1])
        for i in range(mn + 1, mx):
            grid[i][a[0]] = "X"
    else:
        mx = max(a[0], b[0])
        mn = min(a[0], b[0])
        for i in range(mn + 1, mx):
            grid[a[1]][i] = "X"

def check_down(y, x, grid):
    if y >= len(grid) or x >= len(grid[0]) or y < 0 or x < 0: return False
    if grid[y][x] == 'X': return True
    return check_down(y + 1, x, grid)

def check_up(y, x, grid):
    if y >= len(grid) or x >= len(grid[0]) or y < 0 or x < 0: return False
    if grid[y][x] == 'X': return True
    return check_up(y - 1, x, grid)

def check_left(y, x, grid):
    if y >= len(grid) or x >= len(grid[0]) or y < 0 or x < 0: return False
    if grid[y][x] == 'X': return True
    return check_left(y, x - 1, grid)

def check_right(y, x, grid):
    if y >= len(grid) or x >= len(grid[0]) or y < 0 or x < 0: return False
    if grid[y][x] == 'X': return True
    return check_right(y, x + 1, grid)

def fill(y, x, grid):
    if grid[y][x] == 'X' or grid[y][x] == '#': return
    grid[y][x] = 'X'
    fill(y + 1, x, grid)
    fill(y - 1, x, grid)
    fill(y, x + 1, grid)
    fill(y, x - 1, grid)

def check_rect(a, b, grid):
    if grid[a[1]][a[0]] != 'X' and grid[a[1]][a[0]] != '#':
        return False
    if grid[b[1]][b[0]] != 'X' and grid[b[1]][b[0]] != '#':
        return False
    if grid[b[1]][a[0]] != 'X' and grid[b[1]][a[0]] != '#':
        return False
    if grid[a[1]][b[0]] != 'X' and grid[a[1]][b[0]] != '#':
        return False
    return True


pos = []
nx = ""
mxx = -1
mxy = -1
while nx := input():
    pos.append(tuple([int(i) for i in nx.split(",")]))
    mxx = max(mxx, pos[-1][0])
    mxy = max(mxy, pos[-1][1])

# mx = 0
# for i in range(len(pos) - 1):
#     for j in range(i + 1, len(pos)):
#         mx = max(mx, (abs(pos[i][0] - pos[j][0]) + 1) * (abs(pos[i][1] - pos[j][1]) + 1))
# print(mx)

grid = []
for i in range(mxy + 2):
    grid.append(['.'] * (mxx + 2))

for i in range(len(pos) - 1):
    fill_edges(i, i+1, pos, grid)
fill_edges(0, len(pos) - 1, pos, grid)

for i in grid:
    print("".join(i))

a = pos[0]
ep = None
if grid[a[1]][a[0] + 1] == 'X':
    ep = (a[1], a[0] + 1)
elif grid[a[1]][a[0] - 1] == 'X':
    ep = (a[1], a[0] - 1)
elif grid[a[1] + 1][a[0]] == 'X':
    ep = (a[1] + 1, a[0])
elif grid[a[1] - 1][a[0]] == 'X':
    ep = (a[1] - 1, a[0])

if check_down(ep[0], ep[1], grid):
    fill(ep[0] + 1, ep[1], grid)
elif check_up(ep[0], ep[1], grid):
    fill(ep[0] - 1, ep[1], grid)
elif check_left(ep[0], ep[1], grid):
    fill(ep[0], ep[1] - 1, grid)
elif check_right(ep[0], ep[1], grid):
    fill(ep[0], ep[1] + 1, grid)

mx = 0
for i in range(len(pos) - 1):
    for j in range(i + 1, len(pos)):
        if check_rect(pos[i], pos[j], grid):
            mx = max(mx, (abs(pos[i][0] - pos[j][0]) + 1) * (abs(pos[i][1] - pos[j][1]) + 1))
print(mx)
#! /usr/bin/env python3

import heapq

class UnionFind():
    def __init__(self, size):
        self.parent = list(range(size))
        self.groups = set(range(size))
        self.sizes = [1] * size 
    
    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
    
    def join(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        
        if self.sizes[x] < self.sizes[y]:
            self.parent[x] = y
            self.sizes[y] += self.sizes[x]
            self.groups.remove(x)
        else:
            self.parent[y] = x
            self.sizes[x] += self.sizes[y]
            self.groups.remove(y)
    
    def find(self, x, y):
        return self.root(x) == self.root(y)

def sqr(x):
    return x * x

boxes = []
nx = ""
while nx := input():
    boxes.append(tuple([int(i) for i in nx.split(',')]))

q = []

for i in range(len(boxes) - 1):
    for j in range(i+1, len(boxes)):
        dist =  sqr(boxes[i][0] - boxes[j][0]) + sqr(boxes[i][1] - boxes[j][1]) + sqr(boxes[i][2] - boxes[j][2])
        heapq.heappush(q, (dist, i, j))

count = 0
track = UnionFind(len(boxes))
i = -1
j = -1
while len(track.groups) > 1:
    item = heapq.heappop(q)
    count += 1
    track.join(item[1], item[2])
    i = item[1]
    j = item[2]

print(boxes[i][0] * boxes[j][0])

# groups = set()
# for i in track.parent:
#     groups.add(i)

# one = 0
# two = 0
# three = 0
# for i in groups:
#     size = track.sizes[i]
#     if size > one:
#         three = two
#         two = one
#         one = size
#     elif size > two:
#         three = two
#         two = size
#     elif size > three:
#         three = size
# print(one * two * three)
#! /usr/bin/env python3

count = 0
cur = 50
nx = ""
prev = -1

while nx := input(""):
    direction = nx[0]
    steps = int(nx[1:])

    if direction == "L":
        for i in range(steps):
            cur -= 1
            if cur == 0: count += 1
            if cur == -1: cur = 99
    else:
        for i in range(steps):
            cur += 1
            if cur == 100: cur = 0
            if cur == 0: count += 1

print(count)
#!/usr/bin/env python3
import numpy as np

with open('input.txt') as f:
    data = [line.rstrip() for line in f]

m = np.array(data, dtype='U3000')

idx = 0
for i in m:
    m[idx] = m[idx]*96
    idx += 1


def ski_slope(right):
    idx = 2
    step = right+1
    trees = 0
    for x in m[1:]:
        if idx > 323:
            break
        #print('idx: ' + str(idx))
        x[step-1]
        if x[step-1] == '#':
            trees += 1
        idx += 1
        step += right
    return trees

r1 = ski_slope(1)
r3 = ski_slope(3)
r5 = ski_slope(5)
r7 = ski_slope(7)


def moguls(right):
    idx = 3
    step = right+1
    trees = 0
    for x in m[2:]:
        if idx > 323:
            break
        #print('loop idx: ' + str(idx))
        if idx % 2 == 0:
            #print('skipping')
            idx += 1
            continue
        x[step-1]
        #print('current step: ' + str(step-1))
        if x[step-1] == '#':
            trees += 1
        idx += 1
        step += right
    return trees

m1 = moguls(1)

print(r1 * r3 * r5 * r7 * m1)

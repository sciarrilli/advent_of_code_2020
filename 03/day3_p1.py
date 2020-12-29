#!/usr/bin/env python3
import numpy as np

with open('input.txt') as f:
    data = [line.rstrip() for line in f]

m = np.array(data, dtype='U1000')

idx = 0
for i in m:
    m[idx] = m[idx]*32
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
        step += 3
    return trees

print(ski_slope(3))

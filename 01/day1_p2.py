#!/usr/bin/env python3

with open('input.txt') as f:
    data = [int(line.rstrip()) for line in f]

def answer(data):
    for x in data:
        for y in data:
            for z in data:
                if x+y+z == 2020:
                    return x*y*z

if __name__ == '__main__':
    print(answer(data))
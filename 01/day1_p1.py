#!/usr/bin/env python3

with open('input.txt') as f:
    data = [int(line.rstrip()) for line in f]

def answer(data):
    for x in data:
        for y in data:
            if x+y == 2020:
                return x*y

if __name__ == '__main__':
    print(answer(data))
#!/usr/bin/env python3

with open('sample.txt') as f:
    data = [line.rstrip() for line in f]

group = []
groups = []
for i in data:
    if i == '':
        groups.append(group)
        group = []
        continue
    else:
        group.append(i)
groups.append(group)


idx = 0
group_set = set()
count = 0

for group in groups:
    print('')
    print(f'index #{idx}')
    idx += 1
    group_set = set()
    print(f'group level: {group}')
    if len(group) == 1:
        for i in group:
            print(f'item level: {i}')
            for char in i:
                print(f'char level: {char}')
                group_set.add(char)
            print(f'group set 1: {group_set}')
            count += len(group_set)
            print(f'count: {count}')
    else:
        for i in group:
            print(f'item level 2 {i}')
            if len(i) > 1:
                for char in i:
                    print(f'char level 2 {char}')        
                    group_set.add(char)
            else:
                for char in i:
                    group_set.add(i)
        print(f'group set 2: {group_set}')
        count += len(group_set)
        print(f'count 2: {count}')

print('')
print(count)

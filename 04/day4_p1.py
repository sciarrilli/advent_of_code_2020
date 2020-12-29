#!/usr/bin/env python3

with open('input.txt') as f:
    data = f.read().replace(' ', '\n')

valid_fields = {'eyr', 'iyr', 'byr', 'ecl', 'pid', 'hcl', 'hgt'}

passports = [[] for x in range(500)]
idx = 0
for item in data.split('\n'):
    if item == '':
        idx += 1
        continue
    k,v = item.split(':')
    passports[idx].append({k:v}) 


total = 0
for passport in passports:
    fields = set()
    for items in passport:
        for key in items.keys():
            fields.add(key)
    if 'cid' in fields:
        fields.remove('cid')
    if fields == valid_fields:
        total += 1

print(total)

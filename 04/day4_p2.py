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
        for key,value in items.items():
            if key == 'byr':
                #print('byr = ' + value)
                if eval(value) < 1920 or eval(value) > 2002:
                    #print('invalid birth year')
                    continue
            if key == 'iyr':
                #print('iyr = ' + value)
                if eval(value) < 2010 or eval(value) > 2020:
                    #print('invalid issue year')
                    continue
            if key == 'eyr':
                #print('eyr = ' + value)
                if eval(value) < 2020 or eval(value) > 2030:
                    #print('invalid expire year')
                    continue
            if key == 'hgt':
                print('hgt ' + value)
                # this one bit me in the ass! the total went from 199 to 198
                try:
                    if isinstance(eval(value), int):
                        print('invalid height missing cm or in')
                        continue
                except:
                    pass
                if value[-2:] == 'cm':
                    if eval(value[:-2]) < 150 or eval(value[:-2]) > 193:
                        print('invalid height in cm') 
                        continue
                if value[-2:] == 'in':
                    if eval(value[:-2]) < 59 or eval(value[:-2]) > 76:
                        print('invalid height in cm') 
                        continue
            if key == 'hcl':
                if value[0] != '#' or len(value[1:]) != 6:
                    #print('invalid hair color')
                    continue
            if key == 'ecl':
                if len(value) != 3 or value not in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                    #print('invalid eye color')
                    continue
            if key == 'pid':
                if len(value) != 9:
                    #print('invalid passport id')
                    continue
            fields.add(key)
    if 'cid' in fields:
        fields.remove('cid')
    if fields == valid_fields:
        total += 1 

#!/usr/bin/env python3
import sys

with open('input.txt') as f:
    data = [line.rstrip() for line in f]

parsed_data=[]

idx = 0

for item in data:
    p = item.split()
    char_qty = [eval(x) for x in p[0].split('-')]
    char = p[1].rstrip(':')
    password = p[2]
    parsed_data.append((char_qty, char, password))
    idx += 1

password_count = 0
passwords = []
failed_passwords = []

for item in parsed_data:
    char = item[1]
    pos1 = item[0][0]
    pos2 = item[0][1]
    password = item[2]
    try: 
        if password[pos1-1] == char and password[pos2-1] == char:
            failed_passwords.append(password)
            continue
        if password[pos1-1] == char or password[pos2-1] == char:
            passwords.append(password)
    except:
        e = sys.exc_info()[0]
        print(e)
        failed_passwords.append(password)

if __name__ == '__main__':
    print(len(passwords))
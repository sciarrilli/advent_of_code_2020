#!/usr/bin/env python3

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
    qty = item[0]
    password = item[2]
    letters_in_pass = 0
    all_letters = 0
    for letter in password:
        all_letters += 1
        if letter == char:
            letters_in_pass += 1
        if all_letters == len(password):
            if letters_in_pass >= qty[0] and letters_in_pass <= qty[1]:
                password_count += 1
                passwords.append(password)
            else:
                failed_passwords.append(password)


if __name__ == '__main__':
    print(password_count)
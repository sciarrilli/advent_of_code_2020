#!/usr/bin/env python3

# i cheated on day 5

with open('input.txt') as f:
    tickets = [line.rstrip() for line in f]

# find row, 
# 0 to 127 rows
# f means lower half (0-63)
# b means upper half (63-127)
# r upper half of column (4-7)
# l lower half of column (0-3)

seat_ids = []
for line in tickets:
    r = line[:7]
    start = 0
    end = 127
    row, col = 0, 0
    for char in r:
        #print(f'Char: {char}')
        if char == "F":
            end = int((start+end+1)/2) - 1
        elif char == "B":
            start = int((start+end+1)/2)
        #print(f"Start: {start} End: {end}")
    #print("\n")
    row = start
    # to get col, take last 3 chars
    c = line[7:]
    start = 0
    end = 7
    for char in c:
        #print(f"Char: {char}")
        if char == "L":
            end = int((start+end+1)/2) - 1
        elif char == "R":
            start = int((start+end+1)/2)
        #print(f"Start: {start} End: {end}")
    col = start
    # seat ID: multiply the row by 8, then add the column
    sid = row*8 + col
    seat_ids.append(sid)
    print(f"Row: {row} Column: {col} Seat ID:{sid}")
    print("\n")

print(f"Solution 1: {max(seat_ids)}")
print(f"Solution 2: {[seat for seat in range(min(seat_ids), max(seat_ids)) if seat not in seat_ids][0]}")
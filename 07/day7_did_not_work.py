 #!/usr/bin/env python3

with open('input.txt') as f:
    data = [line.rstrip() for line in f]

baglist = data
ending_with_gold = []
bagset = []

print(f'length of baglist: {len(baglist)}')

for item in baglist:
    if ' shiny gold bags.' in item:
        ending_with_gold.append(item)
    if ' shiny gold bag.' in item:
        ending_with_gold.append(item)
    if ' shiny gold bags,' in item:
        ending_with_gold.append(item)
    if ' shiny gold bag,' in item:
        ending_with_gold.append(item)

search_bags = []
#print(f'ending with gold count: {len(ending_with_gold)}')
for item in ending_with_gold:
    cur_list = []
    sentence = item.split()
    #print(sentence)
    for word in sentence:
        if word == 'contain':
            break
        else:
            #print(word)
            cur_list.append(word)
    search_bags.append(cur_list)


for bags in ending_with_gold:
    #print(bags)
    baglist.remove(bags)

print(f'length of baglist: {len(baglist)}')

first_bag = []
for words in search_bags:
    bag = ' '.join(words)
    first_bag.append(bag)


for f_bag in first_bag:
    for bags in baglist:
        if f_bag[:-4] in bags:
            bagset.append(bags)

print('')
print(f'ending with gold count: {len(ending_with_gold)}')
print(f'bagset count: {len(bagset)}')
print(f'total count: {len(ending_with_gold) + len(bagset)}')

print('')
print('ending with gold:')
for i in ending_with_gold:
    print(i)

print('')
print('bagsets:')
for i in bagset:
    print(i)


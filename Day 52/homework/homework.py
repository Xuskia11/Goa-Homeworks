# Vowel Count
def get_count(sentence):
    vows = "aeiou"
    sums = 0
    for i in sentence:
        for vow in vows:
            if i == vow:
                sums = sums + 1
    return sums


#Descending Order
def descending_order(num):
    
    return int("".join(sorted([num for num in str(num)], reverse=True)))

#List Filtering
def filter_list(l):
    return [i for i in l if type(i) != str]

#Find the odd int
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
        

#Sum of Digits / Digital Root
def digital_root(n):
    
    sums = sum([int(num) for num in str(n)])
    if len(str(sums)) >= 2:
        sums = digital_root(sums)
    return sums

def get_count(sentence):
    vows = "aeiou"
    sums = 0
    for i in sentence:
        for vow in vows:
            if i == vow:
                sums = sums + 1
    return sums
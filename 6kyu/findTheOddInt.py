from collections import Counter
def find_it(seq):
    seq = Counter(seq)
    seq = dict(seq)
    for keys,values in seq.items():
        if values % 2 == 1:
            return keys

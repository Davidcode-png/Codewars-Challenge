from collections import Counter
def duplicate_count(text):
    total = 0
    text = text.lower()
    text = list(text)
    text = Counter(text)
    text = dict(text)
    for i,j in text.items():
        if j > 1:
            total += 1
    return total

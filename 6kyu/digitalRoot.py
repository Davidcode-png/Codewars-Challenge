def digital_root(n):
    total = sum([int(i) for i in str(n)])
    if (total // 10) == 0:
        return total
    return digital_root(total)

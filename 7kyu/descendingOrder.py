def descending_order(num):
    # Bust a move right here
    x = str(num)
    x = sorted(x,reverse=True)
    x = ''.join(x)
    x = int(x)
    return x

fib_cache = {0 : 0, 1 : 1}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    fib_cache[n] = result = fib(n-1) + fib(n-2)
    return result

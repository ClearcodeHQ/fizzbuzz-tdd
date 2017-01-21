def fizzbuzz(n):
    s = ''
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            s += 'fizzbuzz'
        elif i % 3 == 0:
            s += 'fizz'
        elif i % 5 == 0:
            s += 'buzz'
        else:
            s += str(i)
        s += '\n'
    return s


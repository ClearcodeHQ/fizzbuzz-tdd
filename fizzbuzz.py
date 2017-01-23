def fizzbuzz(n, fizz='fizz', buzz='buzz'):
    return '\n'.join(fizzbuzz_list(n, fizz, buzz)) + '\n'

def fizzbuzz_list(n, fizz='fizz', buzz='buzz'):
    return [fizzbuzz_single(i, fizz, buzz) for i in range(1, n+1)]

def fizzbuzz_single(i, fizz='fizz', buzz='buzz'):
    if i % 3 == 0 and i % 5 == 0:
        return fizz + buzz
    elif i % 3 == 0:
        return fizz
    elif i % 5 == 0:
        return buzz
    else:
        return str(i)


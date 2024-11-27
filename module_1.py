def dig_pow(n, p):
    sum_sqrt = 0
    x = 0
    list_dig = [int(d) for d in str(n)]
    for i, v in enumerate(list_dig):
        sum_sqrt += v ** (p + i)

    if sum_sqrt % n == 0:
        k = sum_sqrt // n
    else:
        k = -1
    return k

print(dig_pow(46288, 3))
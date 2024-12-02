def xo(s):
    return s.lower().count('o') == s.lower().count('x')

s = 'ooxXm'
print(xo(s))
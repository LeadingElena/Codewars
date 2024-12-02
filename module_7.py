import re

def solution_1(s):
    if len(s) % 2 != 0:
        s += '_'
    return [s[i:i + 2] for i in range(0, len(s), 2)]

def solution_2(s):
    return re.findall(".{2}", s + "_")

def solution_3(s):
    return re.findall('..', s + '_')

def solution_4(s):
    return list(map(''.join, zip(*[iter(s + '_')] * 2)))

print(solution_1('asdfads'))
print(solution_2('asdfads'))
print(solution_3('asdfads'))
print(solution_4('asdfads'))

# вернуть попарно список 'asdfads' -> ['as', 'df', 'ad', 's_']
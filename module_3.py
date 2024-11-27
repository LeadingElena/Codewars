# 1-й вариант
def create_phone_number_1(n):
    phone = ['(']
    for i, v in enumerate(n):
        if i == 2:
            phone.append(str(v))
            phone.append(') ')
        elif i == 5:
            phone.append(str(v))
            phone.append('-')
        else:
            phone.append(str(v))
    phone_number = ''.join(map(str, phone))
    return phone_number

# 2-й вариант
def create_phone_number_2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number_1([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

print(create_phone_number_2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

#1-й вариант
def likes(names):
    text_0 = 'no one likes this'
    text_1 = 'likes this'
    text_2_and_more = 'like this'
    if len(names) == 0:
        return text_0
    if len(names) == 1:
        names.append(text_1)
        return ' '.join(names)
    if len(names) == 2:
        names.append(text_2_and_more)
        return '{} and {} {}'.format(*names)
    if len(names) == 3:
        names.append(text_2_and_more)
        return '{}, {} and {} {}'.format(*names)
    if len(names) > 3:
        names.insert(2, len(names)-2)
        names.insert(3, text_2_and_more)
        return '{}, {} and {} others {}'.format(*names)

#2-й вариант
def likes_1(names):
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'

#3-й вариант
def likes_2(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)

list_names = ["Alex", "Jacob", "Mark", "Max", "Elena"]
print(likes(list_names))
print(likes_1(list_names))
print(likes_2(list_names))
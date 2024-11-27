def solution(number):
    sum = 0
    for number_test in range(1, number):
        if number_test % 3 == 0 or number_test % 5 == 0:
            sum += number_test

    return sum

print(solution(16))
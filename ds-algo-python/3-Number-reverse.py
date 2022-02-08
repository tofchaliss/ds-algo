def reverseTheNumber(number):
    rev = 0
    remainder = 0
    while number > 0:
        remainder = number % 10
        number = number // 10
        rev = rev * 10 + remainder
    return rev

print(reverseTheNumber(1234))
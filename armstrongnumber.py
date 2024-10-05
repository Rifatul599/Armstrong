def is_armstrong(number):
    num_digits = len(str(number))
    sum_of_cubes = 0

    for digit in str(number):
        sum_of_cubes += int(digit)**num_digits

    if sum_of_cubes == number:
        return True
    else:
        return False

print(is_armstrong(153))
print(is_armstrong(123))
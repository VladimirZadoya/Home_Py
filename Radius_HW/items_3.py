def min_number(lst):
    min_value = lst[0]
    for number in lst:
        if number < min_value:
            min_value = number
    return min_value


numbers = [5, 3, 8, 1, 9]
result = min_number(numbers)
print(result)


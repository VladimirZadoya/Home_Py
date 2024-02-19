def multiply_list(lst):
    result = 1
    for element in lst:
        result *= element
    return result


numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print(result)

def squared_list(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result

print(squared_list([3, 12, 5, 2, 6]))

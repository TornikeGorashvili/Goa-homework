def append_all_elements(list1, list2):
    for element in list2:
        list1.append(element)
    
    return list1

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(append_all_elements(list_a, list_b))

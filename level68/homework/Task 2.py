def append_items(list, items_to_add):
    for item in items_to_add:
        list.append(item)
    
    return list

my_list = [1, 2, 3]
items = [4, 5, 6]
print(append_items(my_list, items))

def insert_item(list, index, item):
    new_list = []
    for i in range(len(list)):
        if i == index:
            new_list.append(item)
        
        new_list.append(list[i])
    if index == len(list):
        new_list.append(item)
    return new_list

my_list = [1, 2, 3, 4, 5]
print(insert_item(my_list, 2, 99))

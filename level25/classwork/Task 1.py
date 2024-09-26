# სიას ვქმნით და ვამატებთ 5 ელემენტს
my_list = [10, 20, 30, 40, 50]

# ვბეჭდავთ მესამე და მეოთხე ელემენტებს
print(my_list[2])  # მესამე ელემენტი 
print(my_list[3])  # მეოთხე ელემენტი


# list = [1, 2, 3, 4, 5]

# list1 = [0, 1, 2, 3, 4]

# input = int(input("შეიყვანე ციფრი 1 იდან 5 ამდე"))

# print(list1[input])

my_list = [10, 20, 30, 40, 50]
user_input = int(input("Enter a number: "))
for i in range(len(my_list)): 
    if my_list[i] == user_input: print("Index:", i)

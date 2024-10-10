# შექმენით 4 ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა

list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c', 'd']
list_3 = [True, False]
list_4 = [5.5, 6.7, 7.8, 8.9, 9.1]

print("list_1-ის ზომა:", len(list_1))
print("list_2-ის ზომა:", len(list_2))
print("list_3-ის ზომა:", len(list_3))
print("list_4-ის ზომა:", len(list_4))

# შექმენთ 2 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაამატეთ 3-3 ცვლადი

list_1 = []
list_2 = []

list_1.append(10)
list_1.append(20)
list_1.append(30)

list_2.append('a')
list_2.append('b')
list_2.append('c')

print("list_1:", list_1)
print("list_2:", list_2)

# შექმენით 2 ლისტი. პირველს მე5ე და მე2ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე3ე და მე4ე ადგილას

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']

list_1.insert(4, 100) 
list_1.insert(1, 200) 

list_2.insert(2, 'x') 
list_2.insert(3, 'y')  

print("list_1:", list_1)
print("list_2:", list_2)

# შექმენით 2 ლისტი და ორივედან ამოშალეთ 2-2 ცვლადი pop ფუნქციის გამოყენებით

list1 = ["ვაშლი", "ბანანი", "ატამი", "მსხალი"]
list2 = [10, 20, 30, 40]

list1.pop() 
list1.pop(1)  

list2.pop()  
list2.pop(0) 

print("პირველი ლისტი: ", list1)
print("მეორე ლისტი: ", list2)

# შექმენით 1 ლისტი და გამოიყენეთ ყველა ფუნქცია რაც დღეს გავიარეთ

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "კივი"]

fruits.pop(0) 

fruits.pop()  

fruits.pop(1) 

fruits.pop() 

print("ლისტი:", fruits)

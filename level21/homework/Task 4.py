
products = ["მახიტო: N1", "ცივი ჩაი: N2", "ნატახტარი: N3", "წყალი: N4", " წვენი: N5"]

print(products)

choice = int(input("შეიყვანეთ პროდუქტის ნომერი: "))
    
print(products[choice-1])


basket = [choice]

if basket == 1:
    print("coca-cola")

if basket == 2:
    print("pepsi")

if basket == 3:
    print("coca-cola")

if basket == 4:
    print("water")

if basket == 5:
    print("juice")


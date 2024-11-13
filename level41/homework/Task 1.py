products = ["წყალი", "ჩიფსები", "შოკოლადი", "სოდის სასმელი", "ენერგეტიკული სასმელი"]
prices = [1.5, 2.0, 2.5, 1.75, 3.0]

user_money = 5.0

print("ხელმისაწვდომი პროდუქტები:")
for i, (product, price) in enumerate(zip(products, prices)):
    print(f"{i} - {product}: {price} ₾")

index = int(input("აირჩიეთ პროდუქტის ინდექსი 0-დან 4-მდე: "))

if index < 0:
    print("აირჩიეთ ინდექსი 0-ზე მეტი!")
elif index >= len(products):
    print("აირჩიეთ ინდექსი ნაკლები პროდუქტების რაოდენობაზე!")
elif user_money < prices[index]:
    print("თქვენ არ გაქვთ საკმარისი ფული ამ პროდუქტის შესაძენად.")
else:
    print(f"თქვენ მიიღეთ: {products[index]}")
    user_money -= prices[index]
    print(f"დარჩენილი თანხა: {user_money} ₾")

    



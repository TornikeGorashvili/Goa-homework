# 1. ცვლადში შეინახეთ რიცხვი, თუ ეს რიცხვი ნაკლები იქნება 18-ზე, დაპრინტეთ (underage),
# თუ იქნება 18-ის ტოლი, დაპრინტეთ (teen), თუ იქნება 18-ზე მეტი (adult).

age = 17  # აქ ჩაწერეთ რიცხვი

if age < 18:
    print("underage")
elif age == 18:
    print("teen")
else:
    print("adult")

number = int(input("Enter a number: "))  # აქ მომხმარებელს შეაქვს რიცხვი

if number < 0:
    print("negative")
elif number > 0:
    print("positive")
else:
    print("zero")

goa = 0
while goa < 10:
    print(goa)
    goa = goa + 1
    
goa = 20
while goa > 9:
    print(goa)
    goa = goa - 1

goa = 0
while goa < 5:
    print("goa")
    goa = goa + 1

secret_word = "password123"
user_word = input("გთხოვთ, შეიტანეთ საიდუმლო სიტყვა: ")

while user_word != secret_word:
    print(" სცადეთ კიდევ.")
    user_word = input("გთხოვთ, შეიტანეთ საიდუმლო სიტყვა: ")

print("match")

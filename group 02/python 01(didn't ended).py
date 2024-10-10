import random
import time

def get_user_data():
    print("კეთილი იყოს თქვენი მობრძანება ავიაბილეთების ონლაინ დაჯავშნაზე!")

    # ნაბიჯი 1: ბილეთის კლასის არჩევა
    print("აირჩიეთ ავიაბილეთის კლასი:")
    print("1. ეკონომი \n2. ბიზნესი \n3. პირველი კლასი")
    class_choice = input("შეიყვანეთ კლასის ნომერი (1-3): ")
    
    if class_choice == "1":
        ticket_class = "ეკონომი"
    elif class_choice == "2":
        ticket_class = "ბიზნესი"
    elif class_choice == "3":
        ticket_class = "პირველი კლასი"
    else:
        print("არასწორი არჩევანი, ავტომატურად არჩეულია ეკონომი.")
        ticket_class = "ეკონომი"
    
    # ნაბიჯი 2: პირადი მონაცემების შეყვანა
    first_name = input("შეიყვანეთ თქვენი სახელი: ").strip()
    while not first_name:
        first_name = input("გთხოვთ, შეიყვანეთ თქვენი სახელი: ").strip()

    last_name = input("შეიყვანეთ თქვენი გვარი: ").strip()
    while not last_name:
        last_name = input("გთხოვთ, შეიყვანეთ თქვენი გვარი: ").strip()

    # ნაბიჯი 3: ბარათის ნომრის შეყვანა და ვალიდაცია
    card_number = input("შეიყვანეთ თქვენი ბარათის ნომერი (10 ციფრი): ").strip()
    while len(card_number) != 10 or not card_number.isdigit():
        card_number = input("ბარათის ნომერი არასწორია, სცადეთ თავიდან (10 ციფრი): ").strip()
    
    cvv_cvc = input("შეიყვანე CVV ან CVC: ").strip()
    while len(cvv_cvc) != 3 or not cvv_cvc.isdigit():
        cvv_cvc = input("ბარათის CVV/CVC არასწორია, სცადეთ თავიდან (3 ციფრი): ").strip()

    card_date = input("შეიყვანეთ ბარათის ვადა (ფორმატი: DD-MM-YYYY): ").strip()

    # ნაბიჯი 4: მიმართულების არჩევა
    print("აირჩიეთ მიმართულება:")
    print("1. თბილისი -> ბერლინი \n2. ბათუმი -> ლონდონი \n3. ქუთაისი -> პარიზი")
    direction_choice = input("შეიყვანეთ მიმართულების ნომერი (1-3): ")
    
    if direction_choice == "1":
        direction = "თბილისი -> ბერლინი"
    elif direction_choice == "2":
        direction = "ბათუმი -> ლონდონი"
    elif direction_choice == "3":
        direction = "ქუთაისი -> პარიზი"
    else:
        print("არასწორი არჩევანი, ავტომატურად არჩეულია თბილისი -> ბერლინი.")
        direction = "თბილისი -> ბერლინი"
    
    # ნაბიჯი 5: თარიღის არჩევა
    flight_date = input("შეიყვანეთ ფრენის თარიღი (ფორმატი: DD-MM-YYYY): ").strip()

    # ნაბიჯი 6: რიგისა და ადგილის არჩევა
    row = input("შეიყვანეთ რიგი (1-30): ").strip()
    while not row.isdigit() or not (1 <= int(row) <= 30):
        row = input("არასწორი შეყვანა. შეიყვანეთ რიგი 1-დან 30-მდე: ").strip()

    seat = input("შეიყვანეთ ადგილი (A-F): ").strip().upper()
    while seat not in ['A', 'B', 'C', 'D', 'E', 'F']:
        seat = input("არასწორი შეყვანა. შეიყვანეთ ადგილი A-დან F-მდე: ").strip().upper()

    return {
        "სახელი": first_name,
        "გვარი": last_name,
        "ბარათის ნომერი": card_number, 
        "ბარათის CVV/CVC": cvv_cvc,
        "ბარათის ვადა": card_date, 
        "ბილეთის კლასი": ticket_class,
        "მიმართულება": direction,
        "თარიღი": flight_date,
        "რიგი": row,
        "ადგილი": seat
    }

def generate_ticket(user_data):
    print("------ თქვენი ავიაბილეთი ------")
    print(f"სახელი: {user_data['სახელი']}")
    print(f"გვარი: {user_data['გვარი']}")
    print(f"ბილეთის კლასი: {user_data['ბილეთის კლასი']}")
    print(f"მიმართულება: {user_data['მიმართულება']}")
    print(f"თარიღი: {user_data['თარიღი']}")
    print(f"რიგი: {user_data['რიგი']}, ადგილი: {user_data['ადგილი']}")
    print("_____________________________________")
    print(f"ბარათის ნომერი: {user_data['ბარათის ნომერი'][:4]} **** **** ****")
    print(f"ბარათის CVV/CVC: {user_data['ბარათის CVV/CVC']}")
    print(f"ბარათის ვადა: {user_data['ბარათის ვადა']}")
    print("_____________________________________")
    print("გმადლობთ, რომ აირჩიეთ ჩვენი ავიაკომპანია!")
    print("-------------------------------")

def minute_timer():
    timer = 0  
    while timer <= 100:
        print(f"{timer}%")
        time.sleep(1)
        timer += 5
    print("ფრენა დასრულებულია. გმადლობთ რომ გამოიყენათ ჩვენი ავიაკომპანია")

def guess_number():
    secret_number = random.randint(1, 20)
    print("გამარჯობა! გამოიცანით რიცხვი 1-დან 20-მდე.")
    
    while True: 
        guess = input("შეიყვანეთ თქვენი ციფრი ან 'დასრულება': ")
        
        if guess == "დასრულება":
            minute_timer()
            break
            
        guess = int(guess)
        if guess < secret_number:
            print("თქვენი რიცხვი ძალიან მცირეა!")
        elif guess > secret_number:
            print("თქვენი რიცხვი ძალიან დიდია!")
        else:
            print(f"გილოცავთ! თქვენ გამოიცანით რიცხვი {secret_number}!")
            break  

def wordle():
    words = ['apple', 'grape', 'peach', 'melon', 'lemon', 'mango', 'berry', 'cherry', 'plumb', 'olive']
    secret_word = random.choice(words)
    attempts = 6  

    print("გამარჯობა! ითამაშეთ Wordle. გამოიცანით 5-ბგერიანი სიტყვა.")

    while attempts > 0:
        guess = input(f"\nთქვენი მცდელობა ({attempts} დარჩა): ").lower()

        if len(guess) != 5:
            print("გთხოვთ შეიყვანოთ ზუსტად 5-ბგერიანი სიტყვა.")
            continue

        if guess == secret_word:
            print(f"გილოცავთ! თქვენ სწორად გამოიცანით სიტყვა '{secret_word}'!")
            break

        feedback = []
        for i in range(5):
            if guess[i] == secret_word[i]:
                feedback.append(guess[i].upper())  
            elif guess[i] in secret_word:
                feedback.append(guess[i].lower())  
            else:
                feedback.append("_")  

        print(" ".join(feedback))  
        attempts -= 1

    if attempts == 0:
        print(f"სამწუხაროდ, თქვენ ვერ გამოიცანით სიტყვა. სწორი პასუხი იყო '{secret_word}'.")

def game():
    question = input("გსურს თამაშის გააქტიურება? (დიახ/არა): ")
    if question == "დიახ":
        guess_number()
    else:
        minute_timer()

def choice():
    choice_game = input("აირჩიე თამაში (1. ციფრის გამოცნობა, 2. Wordle): ")
    if choice_game == "1":
        game()
    elif choice_game == "2":
        wordle()
    else:
        print("არასწორი არჩევანი.")

start_fly = input("გსურთ ფრენის დაწყება? (დიახ/არა): ")
if start_fly == "დიახ":
    
    timer = 10  
    while timer > 0:
     print(timer)
     time.sleep(1)
     timer -= 1

  
    


 

print("Time's up!")



if start_fly == "დიახ":
    user_data = get_user_data()
    generate_ticket(user_data)
    choice()
else:
    print("პროცესი დასრულებულია. გმადლობთ.")
    print("გვენდეთ 100%!")
# ---------------------------------------------
rating = int(input("როგორ იფრინეთ? (1-10): "))

if 1 <= rating <= 10:
    print(f"თქვენ შეიყვანეთ {rating} 10-დან")

    if rating > 7:
        print(":)")  
    elif rating < 7:
        print(":(")  
        if rating < 3:  
            feedback = input("გთხოვთ გვითხრათ, რა არ მოგეწონათ?: ")
            print("მადლობა გამოხმაურებისთვის. ვიმუშავებთ ამ საკითხზე.")
    else:
        print(":/")  
else:
    print("გთხოვთ შეიყვანეთ ციფრი 1-10: ")

#----------------------------------------

print('''ხელმისაწვდომი პროდუქტები: 
      
სასმელები: Cola(1), Fanta(2), Pepsi(3), Sprite(4)
ჩიფსი: Lays(5), Pringles(6), Doritos(7), Chips(8)
ტკბილეულები: Bounty(9), Snikers(10), Twix(11), Kinder(12) 
      ''')

user_choise=int(input('დაწერეთ პროდუქტის ნომერი: '))

products= ['Cola', 'Fanta', 'Pepsi', 'Sprite',
'Lays', 'Pringles', 'Doritos', 'Chips',
'Bounty', 'Snikers', 'Twix', 'Kinder']

poduct_to_user=(products[user_choise-1])
print(' ')
print('თქვენი პროდუქტი: ' + poduct_to_user + '!')

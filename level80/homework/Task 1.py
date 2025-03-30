import random

secret_number = random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("შეიყვანე შენი გამოცნობა (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("გთხოვ შეიყვანე რიცხვი 1-დან 100-მდე!")
        except ValueError:
            print("გთხოვ შეიყვანე მხოლოდ რიცხვი!")

def check_guess(guess):
    if guess < secret_number:
        print("შენი გამოცნობა ძალიან მცირეა! სცადე უფრო დიდი რიცხვი.")
        return False
    elif guess > secret_number:
        print("შენი გამოცნობა ძალიან დიდია! სცადე უფრო პატარა რიცხვი.")
        return False
    else:
        print(f"გილოცავ! სწორად გამოიცანი საიდუმლო რიცხვი: {secret_number}")
        return True

def play_game():
    guessed_correctly = False

    while not guessed_correctly:
        user_guess = get_user_guess()
        guessed_correctly = check_guess(user_guess)

play_game()

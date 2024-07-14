# მომხმარებელს მოთხოვნილია შეიყვანოს ორი რიცხვი
num1 = int(input("Enter the first number: "))  # პირველი რიცხვი გადაყვანილია int ტიპში
num2 = int(input("Enter the second number: ")) # მეორე რიცხვი გადაყვანილია int ტიპში

# ვასრულებთ არითმეტიკულ ოპერაციებს
addition = num1 + num2         # შეკრება
subtraction = num1 - num2      # გამოკლება
multiplication = num1 * num2   # გამრავლება
division = num1 / num2         # გაყოფა

# ვბეჭდავთ შედეგებს
print("The sum is: " + str(addition))               # დაბეჭდავს შეკრების შედეგს
print("The difference is: " + str(subtraction))     # დაბეჭდავს გამოკლების შედეგს
print("The product is: + " + str(multiplication))     # დაბეჭდავს გამრავლების შედეგს
print("The quotient is: + " + str(division))          # დაბეჭდავს გაყოფის შედეგს

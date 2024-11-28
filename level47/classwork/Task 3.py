number = int(input("შეიყვანეთ რიცხვი: "))

factorial = 1
i = 1

while i <= number:
    factorial *= i  
    i += 1  
print(f"{number}-ის factoriali არის: {factorial}")

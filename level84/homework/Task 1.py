start = int(input("შეიყვანე პირველი რიცხვი (საიდან დავიწყოთ ამოჭრა): "))
end = int(input("შეიყვანე მეორე რიცხვი (სად დავამთავროთ ამოჭრა): "))
name = input("შეიყვანე რაიმე სახელი: ")

sliced_name = name[start:end]

print("ამოჭრილი მონაკვეთი არის:", sliced_name)

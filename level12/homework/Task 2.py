
# მომხმარებლის ასაკის და მამამისის ასაკის შეყვანა
user_age = int(input("შენი ასაკი: "))
father_age = int(input("მამის ასაკი: "))

# ასაკის გაზრდა 23 წლით
user_age_in_23_years = user_age + 23
father_age_in_23_years = father_age + 23

# რამდენჯერ დიდი იქნება მამა შვილისგან 23 წლის შემდეგ
age_ratio = father_age_in_23_years / user_age_in_23_years

# შედეგის დაბეჭვდა
print(f"23 წლის შემდეგ მამა იქნება {age_ratio}-ჯერ დიდი შენგან.")

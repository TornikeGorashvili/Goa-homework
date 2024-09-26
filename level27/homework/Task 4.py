# მომხმარებელს შემოაქვს სახელი და გვარი ცალ-ცალკე.
first_name = input("შეიყვანეთ თქვენი სახელი: ").strip()
last_name = input("შეიყვანეთ თქვენი გვარი: ").strip()

# სახელი კონვერტირდება პატარა ასოებად, ხოლო გვარი რჩება უცვლელად.
full_name = first_name.lower() + " " + last_name
print(full_name)  # მაგალითად, 'giorgi BERIDZE'

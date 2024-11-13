def print_word():
    words = ["სიხარული", "ბედნიერება", "სიყვარული", "მეგობრობა", "განვითარება"]
    index = int(input("შეიყვანეთ რიცხვი 0-დან 4-მდე: "))
    if 0 <= index < len(words):
        print(words[index])
    else:
        print("არასწორი რიცხვი! გთხოვთ, სცადოთ 0-დან 4-მდე.")

print_word()

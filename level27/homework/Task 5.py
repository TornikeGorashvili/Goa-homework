# ვქმნით სტრინგს.
name = 'goalorienteacademy'

# .find() ფუნქცია პოულობს სტრინგში სიმბოლოს პირველ ადგილმდებარეობას.
# თუ სიმბოლო არ არის სტრინგში, ფუნქცია აბრუნებს -1.

# ვპოულობთ 'o'-ს.
print(name.find('o'))  # 1 (პირველი 'o' სტრინგში)

# ვპოულობთ 'a'-ს.
print(name.find('a'))  # 4 (პირველი 'a' სტრინგში)

# ვპოულობთ 'y'-ს.
print(name.find('y'))  # 16 (პირველი 'y' სტრინგში)

# ვცდილობთ ვიპოვოთ 'x', რომელიც სტრინგში არ არსებობს.
print(name.find('x'))  # -1 (სიმბოლო არ არის სტრინგში)
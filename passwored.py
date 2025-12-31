import random

num1 = ['1','2','3','4','5','6','7','8','9','0','#','@','*']
user = int(input("Enter password length (max 13): "))

if user > len(num1):
    print("Error: Password length cannot be greater than available unique characters.")
else:
    password_list = random.sample(num1, user)  # Picks unique elements only
    password = "".join(password_list)
    print("Generated Password:", password)

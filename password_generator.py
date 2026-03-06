import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("🔐 Welcome to the Python Password Generator!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

password = []

for i in range(nr_letters):
    password.append(random.choice(letters))

for i in range(nr_symbols):
    password.append(random.choice(symbols))

for i in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

final_password = "".join(password)

print("Your generated password is:", final_password)

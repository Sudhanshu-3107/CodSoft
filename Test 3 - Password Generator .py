import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password(password):
    print("Generated Password:", password)

def user_input():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    display_password(password)

user_input()
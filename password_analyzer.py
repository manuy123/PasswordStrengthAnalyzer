import re
import random
import string

# Load old passwords
try:
    with open("old_passwords.txt", "r") as file:
        old_passwords = file.read().splitlines()
except:
    old_passwords = []

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for i in range(12))
    return password

def check_password(password):

    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase check
    if re.search("[A-Z]", password):
        score += 1

    # Lowercase check
    if re.search("[a-z]", password):
        score += 1

    # Number check
    if re.search("[0-9]", password):
        score += 1

    # Special character check
    if re.search("[!@#$%^&*()_+=-]", password):
        score += 1

    # Password reuse check
    if password in old_passwords:
        print("⚠ Password already used before!")
        return

    # Result
    if score <= 2:
        print("Weak Password")
        print("Suggested Strong Password:", generate_strong_password())

    elif score == 3 or score == 4:
        print("Medium Password")

    else:
        print("Strong Password")

    # Save password
    with open("old_passwords.txt", "a") as file:
        file.write(password + "\n")

password = input("Enter Password: ")

check_password(password)
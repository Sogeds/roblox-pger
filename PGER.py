import colorama
from colorama import Fore, Style
import random
import string
from time import sleep

colorama.init()

# Function to generate a random password with letters, numbers, and symbols
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to validate the username
def is_valid_username(username):
    # Check if the username is at least 4 characters long
    if len(username) < 4:
        return False
    # Check if the username contains only English letters and numbers
    if not username.isalnum():
        return False
    return True

# Main program
print(Fore.GREEN + """
                      -- ACCOUNT PASSWORD GUESSER --
                      -- OFFICIAL MADE BY HPYD    --
                      -- GITHUB.COM/SOGEDS        --
""")
print(Fore.RED + """
                      -- MADE ON AN OPEN-SOURCED SOFTWARE --
""")

print(Fore.BLUE + "Enter the account name")
account = input("Username: ")

# Validate the username
if not is_valid_username(account):
    print(Fore.RED + "Unknown Username")
    exit()

print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)
print(Fore.RED + "Trying to PG..."); sleep(1)

# Generate a list of random passwords
passwords = [generate_random_password() for _ in range(10)]

# Pick a random password from the list and display it
password = random.choice(passwords)
print(Fore.GREEN + "PG'ed!")
print(Fore.GREEN + "The password is: " + password)



print(Fore.WHITE + "WARNING: THIS PROGRAM IS A JOKE, PLEASE DO NOT TAKE IT SERIOUSLY.")
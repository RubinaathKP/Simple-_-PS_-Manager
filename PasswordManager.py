# A password generator tool
import random
import string
import csv

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a random password."""
    if length < 1:
        raise ValueError("Password length must be at least 1")
    char_pool = ""
    site = input("Enter the site name: ")
    username = input("Enter the username: ")

    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    if not char_pool:
        raise ValueError("At least one character type must be selected")
    password = ''.join(random.choice(char_pool) for _ in range(length))
    store_password(site, username, password)
    print(f"Generated password: {password}")
    return password

def store_password(site, username, password, filename="passwords.csv"):
    """Store the generated password in a csvfile."""
    if not site or not username or not password:
        raise ValueError("Site, username, and password must be provided")
    if password == "":
        password = generate_password()
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([site], [username], [password])
    print(f"Password for {site} stored successfully.")


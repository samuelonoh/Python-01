# Demonstrates str functions
# spilt user's name into first name and last name

name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")

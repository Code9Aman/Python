import re

password = input("Enter a password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check lowercase letters
if re.search(r"[a-z]", password):
    score += 1

# Check uppercase letters
if re.search(r"[A-Z]", password):
    score += 1

# Check digits
if re.search(r"\d", password):
    score += 1

# Check special characters
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

# Decide strength
if score <= 2:
    print("Weak")
elif score == 3 or score == 4:
    print("Medium")
else:
    print("Strong")

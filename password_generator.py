import random
import string

def pass_generate(length = 15, use_symbols = True):
    
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    chars = letters + numbers 
    if use_symbols:
        chars += symbols
    
    password = "".join(random.choice(chars) for _ in 
range(length))
    
    return password

def strength_checker(password):
    score = 0
    
    if len(password) >=12:
        score +=1
    if any(c.islower() for c in password):
        score +=1
    if any(c.isupper() for c in password):
        score +=1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
        
    if score <= 2:
        return "WEAK 🟥"
    elif score <=4:
        return "MEDIUM 🟨"
    else:
        return "STRONG 🟩"


print("password genarator")

length = int(input("panjang pass: "))
symbols_choice = input("guna symbol ? y/n: ").lower()

use_symbols = symbols_choice == "y"
print("gagal")

result = pass_generate(length)
strength = strength_checker(result)

print("\npass berhasi dibuat:", result)
print("\nmeter strength pass: ", strength)
password = input()

error = 0
def is_valid(word):  #  checking length of password

    return 6 <= len(word) <= 10

def is_digit_letter(word):  #  checking if its only digits and letters

    is_True = word.isalnum()
    return is_True

def is_two_digits(word): #  checking if there are at least 2 digits
    is_true = False
    digits = 0
    for n in word:
        if n.isdigit():
            digits += 1

    if digits >= 2:
        is_true = True
    return is_true

if not is_valid(password):
    error += 1
    print(f'Password must be between 6 and 10 characters')

if not is_digit_letter(password):
    error += 1
    print(f"Password must consist only of letters and digits")

if not is_two_digits(password):
    error += 1
    print("Password must have at least 2 digits")

if error == 0:
    print(f'Password is valid')









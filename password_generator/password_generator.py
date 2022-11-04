import random

lower_letters = ['a','b','c','d',]
upper_letters = ['A','B','C','D']
numbers = ['1','2','3','4','5']
special_char = ['!','@','#','*']

comp_low_letters = ""
comp_cap_letters = ""
comp_numbers = ""
comp_spchar = ""
user_pw = ""

user_low_letter = int(input("How many lower letters do you want? "))
user_cap_letter = int(input("How many capital letters do you want? "))
user_numbers = int(input("How many numbers do you want? "))
user_spchar = int(input("How many special characters do you want? "))


if user_low_letter > 0:
    for l in range(user_low_letter):
        comp_letters = random.choice(lower_letters)
        user_pw += comp_letters
if user_cap_letter > 0:
    for l in range(user_cap_letter):
        comp_cap_letters = random.choice(upper_letters)
        user_pw += comp_cap_letters
if user_numbers > 0:
    for l in range(user_numbers):
        comp_numbers = random.choice(numbers)
        user_pw += comp_numbers
if user_spchar > 0:
    for l in range(user_spchar):
        comp_spchar = random.choice(special_char)
        user_pw += comp_spchar
else:
    ("Please select a number.")

list_user_pw = list(user_pw)
random.shuffle(list_user_pw)
user_pw = ''.join(list_user_pw)

print(f"Your password is: {user_pw} ")
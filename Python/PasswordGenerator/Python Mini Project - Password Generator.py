import string
def get_char_type(char):
    if(char in string.digits):
        return "Number"
    if(char in string.ascii_lowercase):
        return "Lower"
    if(char in string.ascii_uppercase):
        return "Upper"
    return "Special"

def get_char_type_count(string):
    charCounter = {"Number":0, "Lower":0, "Upper":0, "Special":0}
    for char in string:
        charType = get_char_type(char)
        charCounter[charType] += 1
    return charCounter

def calculate_password_strength(password):
    if(len(password) < 8):
        return 0
    return sum(value > 0 for value in get_char_type_count(password).values())

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice, randint

def gen_password(strength):
    chars = ascii_lowercase+ascii_uppercase+digits+punctuation
    while(True):
        password_list = [choice(chars) for i in range(randint(8,10))]
        new_password = "".join(password_list)
        if(calculate_password_strength(new_password) == strength):
            return new_password

print(gen_password(1))
print(gen_password(2))
print(gen_password(3))
print(gen_password(4))


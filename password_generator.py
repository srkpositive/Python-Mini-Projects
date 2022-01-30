#import the necessary libraries
import string
import random

if __name__ == "__main__":
    set1 = string.ascii_lowercase
    set2 = string.ascii_uppercase
    set3 = string.digits
    set4 = string.punctuation
    while True:
        try:
            password_length = int(input("Enter the password length: "))
            password_set = []
            password_set.extend(list(set1))
            password_set.extend(list(set2))
            password_set.extend(list(set3))
            password_set.extend(list(set4))
            random.shuffle(password_set)
            print("Your auto generated password is:")
            print("".join(password_set[0:password_length]))
        except Exception as e:
            print("Not a valid input!\nTry only numbers.")
        
#imports
import random
import string

path = "venv/passwords.txt"

def input_requirements():
    while True:
        try:
            length = int(input('Good day!, please input the length of your required password : '))
            break
        except ValueError:
            print('Words are invalid, Please choose a number between 3 to 10 : ')
            continue

    if length <= 3:
        print('Too short, please try again')

    elif length >= 10:
        print('Whoa, Thats too long, please pick between 3 to 10')
    else:
        ()
def file_reader():
    open(path)
def inArray(x,y):
    x = [given]
    x.append(given)

def password_generator(lines, given):
    words = []  # this is an empty list, the next 3 lines of code fills it
    for word in given:  # for every word in our list above 'given'
        if len(word) == lines:  # if a word length in 'given' matches the value that was given in 'lines ' .For example 3, then every 3 letter word
            words.append(word)  # is added to words[]
    for x in words:  # for every word in our newly created list words[]
        print('We have selected ')

lines = file_reader()
letters = input_requirements()
given = [path]
count = 0

while count < 3:
    count = count + 1
    password = password_generator(lines,given)
    print("Your new password is: ", password)
    satisfied = input("Are you satisfied with your password?, please enter yes or no\n")
    if satisfied == "yes":
        break
    elif satisfied == "no":
        continue

import random

path = ('/home/l4st1/PycharmProjects/wethinkcode/venv/passwords.txt')

def file_reader():
        File_object = open(path,"r")
        for line in File_object:
            b = line.strip()
            given = b.split()
        return given

def input_requirements():
        print('Good day')
        print('Welcome to password manager.')
        selection = int(input('Please select the character length you would like your password to be ranging from 3 to 10 characters '))
        while (selection < 3) or (selection> 10):
            print('Selection is of an inappropriate length.')
            selection = int(input('Please select the character length you would like your password to be ranging from 1 to 10 characters '))
            
        return selection

def password_generator(lines,given): # 'lines' will be 'password_generator' and 'given' is the list above.
        words = []                    # this is an empty list, the next 3 lines of code fills it  
        for word in given:            # for every word in our list above 'given'
            if len(word) == lines:    #if a word length in 'given' matches the value that was given in 'lines ' .For example 3, then every 3 letter word
                words.append(word)    # is added to words[] 
        print('We have selected')
        print(random.choice(words))
        confirm = input('If you are happy with selection type yes. If you would like another option type no ' )
        count = 0
        while (confirm == 'no') and (count <2):
                print('We have selected')
                print(random.choice(words))
                confirm = input('If you are happy with selection type yes. If you would like another option type no ' )
                count +=1
        

file_reader()
input_requirements()
password_generator(lines,given)

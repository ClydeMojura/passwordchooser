# passwordchooser

Password Chooser

Goal

A user can input three the length of a password they would like between 3 and 10
characters. The program reads words from a list that have characters 3 to 10. There
are three options for each word length (3 words of 3 characters, 3 words with 3
characters etc.) If they are satisfied with their word the program ends, if they are not
they will be assigned another password until there are no options available.

Your program will do the following:

● Load a file of words
● Ask the user for a number of characters and accept them (3 - 10 characters)
● Select one of the words in the list that meets the requirement
● Ask the user if they are satisfied with the password, if they are not the
program reassigns a password, if they are satisfied with the password the
program ends.

The program will be split into 4 functions:
You will be divided into teams of four for this project. The project will be split into the
following tasks
● file_reader()
This function will open a file, read its contents, store it in an array and return the
array.
● input_requirements()

This function will welcome the user to the program and input the number of
characters between 3 and 10 and return the value.

● password_generator(lines, given)
This function will pick a password from the array of passwords based on the number
of characters the user entered. It will ask the user if they are satisfied with the
passwords, if they aren’t it will pick a different password with the same character
length until there are no more passwords.
● inArray(x,y)
This function will ensure that the password chosen has not been assigned before
when the user is not satisfied with their password and return whether free if the
password is new and taken if it has been used.

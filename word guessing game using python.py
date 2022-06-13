#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
words=['apple','ball','cat','dog','elephant','fun','gun','hat','ice','jug','kite','lion','monkey','nannu','orange','piya','queen','rat','sun','ten','umbrella','van','watch','yogurt','zoo']
guessed_word=random.choice(words)
hint=guessed_word[0]+guessed_word[-1]


l=[]
try_p=6
a=input("enter your name")
print("welcome to the game world",a)
print("we are going to give you 6 attempts for guessing")

for guess in range(try_p):
    while True:
        letter=input("Guess the letter:" )
        
        if len(letter)==1:
            break
        else:
            print("Oops!! please Guess a letter again")
            
    if letter in guessed_word:
        print("yes!")
        l.append(letter)
    else:
        print("no!")
        
    if guess==3:
        print()
        clue_request=input("would you like a clue")
        if clue_request.lower().startswith('y'):
            print()
            print("CLUE:The first and last letter of the word is:",hint)
        else:
            print("you're very confident")

print() 
print("NOW let's see what have guessed so far. ",len(l),"letter correctly")
print("These letters are:",l)
        
word_guess=input("Guess the whole word: ")
if word_guess.lower()==guessed_word:
    print("Congrats!! you are correct")
else:
    print("Sorry! The answer was:",guessed_word)
print()
input("Please press Enter to leave the program")


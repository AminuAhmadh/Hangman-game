# a hangman game by aminu ahmadh
# GITHUB @AminuAhmadh



import random
import pyinputplus



animals = ['ant', 'bat', 'beetle', 'bird', 'buffalo', 'cat', 'chicken', 'cocktail', 'cow', 
'dog', 'donkey', 'duck', 'elephant', 'fish', 'frog', 'goat', 'giraffe', 'goose', 
'hyena', 'kangaroo', 'leopard', 'lobster', 'ostrich' , 'oyster', 'parrot', 
'pig', 'rabbit','tiger', 'wasp', 'wolf', 'zebra']
fruits = ['apple', 'avocado', 'banana', 'cherry', 'cantaloupe', 'grape', 'guava', 'kiwi', 'lime', 
'mango', 'papaya', 'raspberry', 'tart', 'watermelon', 'orange', ]
secretWordList = [] 

print('Hangman Game. The objective of the game is to guess the right word choosing by the computer.')
print('You can only guess one word/letter at a time')
print("let's get started")



category = pyinputplus.inputChoice(['A', 'F'], prompt="Enter 'A' for animals category or 'F' for fruits: ")
if category == 'A':
    secretWord = random.choice(animals)
    print("You choose the Animals category")
elif category == 'F':
    secretWord = random.choice(fruits)
    print("You choose the Fruits category")
    
for i in range(len(secretWord)):
    secretWordList.append('*')

def secretword():
    print('The secret Word is:', ''.join(secretWordList) )

guessesAllowed = len(secretWord) + 2

while guessesAllowed != 0:
    word = input('guess a word: ')


    if word in secretWord:
        print('Nice guess')
        guessesAllowed -= 1
        print('You have',str(guessesAllowed),'Guesses left')
        if guessesAllowed == 0:
            print('Sorry you lose. the secret word is', secretWord)
        else:
            for i in range(len(secretWord)):
                if secretWord[i] == word:
                    secretWordList[i] = word.upper()
                    secretword()
    else:
        print('Bad guess, try again,')
        guessesAllowed -= 1
        print('You have',str(guessesAllowed),'Guesses left')
        if guessesAllowed == 0:
            print('Sorry you lose. the secret word is', secretWord)
        else:
            secretword()
            continue

    
    joinedLetters = ''.join(secretWordList)
    if joinedLetters.upper() == secretWord.upper():
        print("You're amazing, you guessed the word right")
        break
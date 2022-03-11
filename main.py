import random
from collections import Counter
from replit import db

'''
wordlist = x = {"name" : "John", "age" : 36}	dict !!!  dict key value is the generic term for the hint e.g. Car contains then brands, car is the indication, ist der Oberbegriff für den Hinweis zb. Auto enthalt dann marken, Auto ist der Hinweis


1. randomly worth key,
2. random word from keyword,


other possibility

DB with keyword's 

for the counter problem

if len(word) != len(letterGuessed):
correctly_advised = len(word) - len(guess)
print(correctly_advised)'''

db["car"] = "Audi", "BMW", "Mercedes",
db["animal"] = "Dog", "Cat",
dbkey = db.keys

# dbkey = random.choice(dbkey)
print(dbkey())
dbkeylen = len(dbkey())
dbkeylen = random.randint(0, dbkeylen - 1)
print(dbkeylen)

key = list(db.keys())[dbkeylen]
print(key)


value = db.get(key)
print(value)

value = random.choice(value)
print(value)




wordlist = ['one', 'two', 'tree']

word = random.choice(wordlist) #choose a secret random word

print(f'test display {word} {value}') #test display


print('''
__          __  _                            _          _               _               _    _                                         
\ \        / / | |                          | |        | |             | |             | |  | |                                        
 \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |     ___| |_ ___   _ __ | | __ _ _   _  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |    / _ \ __/ __| | '_ \| |/ _` | | | | |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
   \  /\  /  __/ | (_| (_) | | | | | |  __/ | |___|  __/ |_\__ \ | |_) | | (_| | |_| | | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    \/  \/ \___|_|\___\___/|_| |_| |_|\___| |______\___|\__|___/ | .__/|_|\__,_|\__, | |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                                                 | |             __/ |                      __/ |                      
                                                                 |_|            |___/                      |___/        
''')


if __name__ == '__main__':
  hint = input("Would you like a hint?\ntype Y = Yes or N = No\nEnter:").lower() #hint will be implemented later
  if hint == 'y':
    print("Guess the word! HINT: word is a PLACEHOLDER_FOR_HINT")

  else:
    print("Okay, let's start") #...with the first letter

  print(f"\nThe word we were looking for has {len(word)} letters ", '_ ' * len(word)) #display the empty spaces for letters of the word
  #for i in word: 
    #print('_', end = ' ')
  #print() maybe for a paragraph?
  
  
  playing = True# list for storing the letters guessed by the player
  letterGuessed = ''                
  chances = len(word) + 2 #Number of attempts = word length + 2
  correct = 0
  flag = 0
  try:
      while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed 
          chances -= 1
          
          try:
              print(f'\n\nCorrect:{correct} Flag:{flag}\n{chances} more attempts left')
              guess = str(input(f'Enter a letter to guess: ')).lower()
              
          except:
              print('Enter only a letter!')
              continue
  
          if not guess.isalpha(): # Validation of the guess
              print('Enter only a LETTER')
              continue
          elif len(guess) > 1:
              print('Enter only a SINGLE letter')
              continue
          elif guess in letterGuessed:
              print('You have already guessed that letter')
              continue
  
  
          # If letter is guessed correctly !!! Wenn der Buchstabe richtig erraten wird
          if guess in word:
            k = word.count(guess) #k stores the number of times the guessed letter occurs in the word !!!k speichert die Häufigkeit, mit der der erratene Buchstabe im Wort vorkommt
            for _ in range(k):    
                letterGuessed += guess # The guess letter is added as many times as it occurs  !!!Der Ratebuchstabe wird so oft hinzugefügt, wie er vorkommt

          if len(word) !=  len(guess): # this is how it works ;)
            print(len(word) - len(guess))
                
          # Print the word
          for char in word:
              if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): # If user has guessed all the letters Wenn der Benutzer alle Buchstaben erraten hat
                  print(char, end = ' ')
                  correct += 1
             
              elif (Counter(letterGuessed) == Counter(word)): # Once the correct word is guessed fully, !!! Sobald das richtige Wort vollständig erraten ist,
                                                                # the game ends, even if chances remain  !!! das Spiel endet, auch wenn die Chancen bleiben
                  print("\nThe word is: ", end=' ')
                  print(word)
                  flag = 1
                  print('''
__     __                                                 
\ \   / /                                                 
 \ \_/ /__  ___   _   _  ___  _   _  __      _____  _ __  
  \   / _ \/ __| | | | |/ _ \| | | | \ \ /\ / / _ \| '_ \ 
   | |  __/\__ \ | |_| | (_) | |_| |  \ V  V / (_) | | | |
   |_|\___||___/  \__, |\___/ \__,_|   \_/\_/ \___/|_| |_|
                   __/ |                                  
                  |___/    

Congratulations!''')
                  break # To break out of the for loop
                  break # To break out of the while loop
              else:
                  print('_', end = ' ')
  
              
      if chances <= 0 and (Counter(letterGuessed) != Counter(word)): # If user has used all of his chances
          print()
          print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
                
You lost! Try again


''',f"The word you are looking for is {word}")
          
  except KeyboardInterrupt:
      print('\nBye! Try again.')
      exit()
    



#cookbook
#https://www.geeksforgeeks.org/hangman-game-python/
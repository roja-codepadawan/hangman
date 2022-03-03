import random
from collections import Counter

wordlist = ['one', 'two', 'tree']

word = random.choice(wordlist) #choose a secret random word

print(f'test display {word}') #test display


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
              guess = str(input(f'Enter a letter to guess: '))
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
  
  
          # If letter is guessed correctly
          if guess in word:
              k = word.count(guess) #k stores the number of times the guessed letter occurs in the word
              for _ in range(k):    
                  letterGuessed += guess # The guess letter is added as many times as it occurs
  
          # Print the word
          for char in word:
              if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): # If user has guessed all the letters
                  print(char, end = ' ')
                  correct += 1
             
              elif (Counter(letterGuessed) == Counter(word)): # Once the correct word is guessed fully, 
                                                                # the game ends, even if chances remain
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
      print()
      print('Bye! Try again.')
      exit()
    





#cookbook
#https://www.geeksforgeeks.org/hangman-game-python/
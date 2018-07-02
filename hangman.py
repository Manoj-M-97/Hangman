# Libraries to be imported:
import random

# User Interface on start of the game
print(format('-','->40'))
print(format(' ','>10'),'Welcome to Hangman!',"\n")
print("The game goes like this.","\n","\n","You will be given a word and a hint in the form of its definition.","\n",
    "You will have to guess the word by guessing one letter at a time.","\n"
    "The number of wrong guesses you can make will be three fewer than the number of letters in the word.")

# The while loop is for playing the game again or not according to the user's choice.
again=True
while(again==True):
 print("\n","Here you go....","\n")
# The following lists have all the words and their meanings respectively. TO extend the game, words and their definitions can be added accordingly
 word_list = ["quorum", "cabal", "prolix", "rhythm", "bayou", "foxglove", "bevel", "logorrhea", "ornery", "bloviate"]
 definitions =["the minimum number of members of an assembly or society that must be present at any of its meetings to make the proceedings of that meeting valid",
              "a secret political clique or faction",
			  "(of speech or writing) using or containing too many words; tediously lengthy.",
			  "a strong, regular repeated pattern of movement or sound",
			  "a marshy outlet of a lake or river",
			  "a tall Eurasian plant with erect spikes of pinkish-purple (or white) flowers shaped like the fingers of gloves",
			  "a sloping surface or edge",
			  "a tendency to extreme loquacity",
			  "bad-tempered or difficult to deal with",
			  "talk at length, especially in an inflated or empty way"]
 diction = zip(word_list, definitions)
 guesses = 0
 win = 0
 separated_letters = []
 already_guessed = []
 every_key_value = {}
 # Random function is to generate a random number which is used as the index of the list to get the corresponding word.
 # This is to randomize the words that are given to the player.
 rand_index = random.randint(0, 9)
 word = word_list[rand_index]
 meaning = definitions[rand_index]
 print("The meaning of your word is: ", meaning)
 for a in word:
  separated_letters.append(a)
 l = len(word)
 print('_ '*l)

 # The following (l-3) is the number of wrong letter guessess the player is allowed before the player loses.
 while guesses <= l - 3:
  flag = 0
  guess = input('Guess a letter: ')
  if guess in already_guessed:
   print('You have already guessed this. Try again.')
   continue
  if guess.isalpha() and (guess not in already_guessed):
   for index, item in enumerate(separated_letters):
    if item == guess:
     flag = 1
     every_key_value[index] = item
  if flag == 0:
   print("The word doesn't have that letter. Try again.")
   guesses += 1
   already_guessed.append(guess)
   #even if the letter is not in the word, this adds it to the 'already_guessed' list so that the player isn't penalized for accidentally guessing it again
   continue
  for i in range(l):
   if i in every_key_value.keys():
    print (every_key_value[i], ' ', end = '')
   else:
    print ('_ ', end = '') 
  already_guessed.append(guess)
  if len(every_key_value.keys()) == l and guesses <= l - 3: 
   print("You win!")
   win = 1
   break
 if win == 0:
  print("You lose!")
  print ("Your word was '", word, "'.", sep = '')
  print("Better luck next time!")
 print("That was fun.")
 try1=input("Would you like to play again? (YES or NO): ")
#For wrong input for 'yes' or 'no'
 while try1.lower()!="yes" and try1.lower()!="no":
  print("Invalid entry")
  try1=input("Enter either 'yes' or 'no': ")
 if try1.lower()=="yes":
  again=True
 elif try1.lower()=="no":
  again=False
  print(format('-','->30'))
  print('Waiting for you to come back next time')
 

   
  
  
  

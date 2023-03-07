secretWord = "python"
guess = " "
guessCount = 0
guessLimit = 3
outOfGuesses = False

while guess != secretWord and not(outOfGuesses): #This line says while guess is not equal to the secret word and they are not out of guesses
    if guessCount < guessLimit:                  #If the guess count is less than the guess limit continue
        guess = input("Enter Guess: ")           #Asks user to input guess which then goes down to the next line
        guessCount += 1                          #This adds 1 onto the guess count after the user has guess
    else:
        outOfGuesses = True                      #This means if out of guesses becomes True

if outOfGuesses:                                 #If statement now says if the user is out of guesses print You lose!
    print("You lose!")
else:
    print("You win!")                            #else print You win if you wasn't out of guesses cause you guessed correctly
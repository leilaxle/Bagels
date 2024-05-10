import random 

NUM_DIGITS = 3 # define a variable called num of digits that user has to eventually guess
MAX_GUESSES = 10 # this is the max attempt a user has 

# introduce the progam!
def main():
    print('''Bagels, a detective logic game by Al Sweigart al@inventwithpython.com

          I am thinking of a {}-digit number with no repeated digits. Try to guess what it is!
          Here are some clues: 
          When I say:   That means: 
          Pico          One digit is correct, but in the wrong position. 
          Fermi         One digit is correct, and in the right position. 
          Bagels        No digit is correct.

          For example, if your secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))
    
# this is a while loop - while the loop is true, do the following below 

    while True: 
        # stores the secret the player needs to guess
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = '' # keep looping until valid guess is entered
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                print("You got it!")
                break 
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses!')
                print('The answer was {}.'.format(secretNum))

        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')


# define functions 

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range (NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
        
def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels!'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()

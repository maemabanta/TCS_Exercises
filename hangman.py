import getpass

# INITIALIZE VARIABLES
lives = 5
blank = []
char = []
#PRINT START GAME
print("Let's play hangman!")
print("LIVES: ", lives)

#PROMPT FOR SECRET WORD
word = getpass.getpass(prompt = "What is the secret word? ")
blank = ' _'*len(word)
blanklist = list(blank)

#MAIN LOOP FOR ASKING INPUTS, CHECKING IF GUESS LETTER IN STRING, TERMINATING CONDIITONS
while lives > 0:
    i = 0
    blank = "".join(blanklist)
    print(blank)
    guess = input("Guess a letter: ")
    
    g = word.find(guess) 
    print("_______________________________")    

    if word[g] == guess:    
        print("Correct!")

        #CHECKS FOR MULTIPLE INSTANCES OF THE SAME LETTER
        for n, i in enumerate(word):
            if i == guess:
                blanklist[(n*2)+1] = guess
        
        char.append(guess)
        print("guesses: ", char)
        print("LIVES: ", lives)
        if '_' not in str(blanklist):
            print('YOU WIN!')
            print('Answer: ', word)
            break
            
    elif g == -1:
        char.append(guess)
        print("-1 life")
        print("guesses: ", char)
        lives -= 1
        print("LIVES: ", lives)

if lives == 0:
    print("Game over")
    print("_______________________________\n")
    print("Answer: ", word)

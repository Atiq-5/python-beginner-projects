from random import randint

r = randint(1,10)
g = 0
while True:
    if g==0:
        print("Make a guess between 1 to 10: ")
    else:
        print("Guess again: ")
    g +=1
    
    guess = input()

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number next time.")
        continue

    if r == guess:
        print("You go it.")
        break
    elif r>guess:
        print("Guess a bit higher.")
    else:
        print("Guess a bit lower.")


if g==1:
    print("It took you only 1 guess")
else:   
    print(f"It took you {g} guesses")

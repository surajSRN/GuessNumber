
n=18
number_of_guess=1
print("Remember you have 5 no. of guesses")
while number_of_guess<=5:
    print("Enter the number you want to guess")
    guessnumber=int(input())

    if guessnumber<n:
        print("The number is incorrect.Please guess a higher number")
    elif guessnumber>n:
        print("The number is incorrect. please guess a lesser number")
    else:
        print("You guess the correct number /nYou won the game")
        print("The no of guesses you took: ",number_of_guess)
        break
    no_of_guesses=5-number_of_guess
    print("The no.of guesses left: ",no_of_guesses)
    number_of_guess= number_of_guess+1
if number_of_guess>5:
    print("Game Over")












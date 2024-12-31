n=16
num_of_guesses=1
print("number of guesses is limited to 9 times")
while(num_of_guesses<=9):
    guess_num=int(input("guess the number:\n"))
    if guess_num<16:
        print("you entered lesser number plz input greater number")
    elif guess_num>16:
        print("you entered greater number plz enter lesser number")
    else:
        print("you won \n")
        print(num_of_guesses, "no.of guesses he took to finish.")10
        break
    print(9-num_of_guesses, "number of guesses left")
    num_of_guesses=num_of_guesses +1
if (num_of_guesses>9):
    print("game over")


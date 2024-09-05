import random

def script():
    # Write Your code here....
    # ....
    # ....
    # # 17-Aug-20 ( Monday )
    yrname = input("Hello You are ..?\n")
    if yrname == "Lovishm" or yrname == "k":
        print("___________Welcome________\n| | | | | | | | | | | | | | | |\n| | | | | | | | | | | | | | | |\n⌄ "
              "⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄ ⌄")

        print("Guess The Number Game")

        hidden_number = int(random.randint(1, 100))
        number_of_lives = 1
        print("Number of Lives are 9")
        while number_of_lives <= 6:
            guess_numb = int(input())
            if guess_numb < hidden_number:
                print("Guess a bigger number")
            elif guess_numb > hidden_number:
                print("Guess a smaller number")
            else:
                print("You Won     Number of lives left", 6 - number_of_lives)
                break
            print(9 - number_of_lives, "number of lives left")
            number_of_lives = number_of_lives + 1
        if number_of_lives > 9:
            print("Game Over")

    else:
        exit("Go back.... & Leave Myyy Computerrr.....")

    restart = input("\nWould you like to restart this program?  ")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        exit("ok bye ....Goodbye.")


script()

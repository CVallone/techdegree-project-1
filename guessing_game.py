import random


guess_list = []


def start_game():
    print("------------------------------------\n Welcome to the number guessing game! \n-----------------------------------")
    rand_num = random.randint(1,10)
    guess_num = (input("guess a number from 1 to 10:  "))
    guess_count = 1
    while True:
        try:
            guess_num = int(guess_num)
        except ValueError:
            print("Oh no that's not a number, try again!")
            guess_num = (input("Try Again:  "))
        else:
            if int(guess_num) > 10 or int(guess_num) < 1:
                print("That guess is outside of our range...keep it between 1 and 10, please:")
                guess_num = (input("Try Again:  "))
            else:
                if int(guess_num) > rand_num:
                    guess_num = input("It's lower than that, try again:  ")
                    guess_count += 1
                    print("You've made {} tries.".format(guess_count))
                elif int(guess_num) < rand_num:
                    guess_num = input("It's higher than that, try again:  ")
                    guess_count += 1
                    print("You've made {} tries.".format(guess_count))
                else:
                    print("You got it with {} tries!".format(guess_count))
                    again = input("Would you like to play again?  [y]es/[n]o:  ")
                    if again.lower() == 'y':
                        print("Your last score was: {}".format(guess_count))
                        guess_list.append(guess_count)
                        print("The lowest number of guesses so far was: {}".format(min(guess_list)))
                        start_game()
                    else:
                        guess_list.append(guess_count)
                        print("The lowest number of guesses: {}".format(min(guess_list)))
                        print("Thanks! Hope you had fun!")
                        guess_list.clear()
                        break

start_game()


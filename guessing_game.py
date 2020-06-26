import random


def start_game():
    print("------------------------------------\n Welcome to the number game! \n-----------------------------------")
    rand_num = random.randint(1,10)
    guess_num = (input("guess a number from 1 to 10:  "))
    try:
        guess_num = int(guess_num)
    except ValueError:
        print("Oh no that's not a number, try again!")
        start_game()
    else:
        if guess_num > 10:
            print("That guess is too high...keep it at 10 or below, please:")
            start_game()
        else:            
            guess_count = 1
            while rand_num != guess_num:
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
                            start_game()
                        else:
                            print("Thanks! Hope you had fun!")
                            break
    

start_game()

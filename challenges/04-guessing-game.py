from random import randint

MIN = 1
MAX = 100
num_guessed = 0
real_num = randint(MIN, MAX)

def guess_a_number():
    global num_guessed
    guess = input("Guess a number between %d and %d\n" % (MIN, MAX))
    guess = (int(guess))
    if guess == real_num:
        print("you guess it in", num_guessed, "guesses")
        print("Great guess!")
    elif guess > real_num:
        print("The real number is lower")
        num_guessed += 1
        print("you're on guess #", num_guessed)
        guess_a_number()
    else:
        print("The real number is higher")
        num_guessed += 1
        print("you're on guess #", num_guessed)
        guess_a_number()

guess_a_number()
# def how_can_i_help_you():
#     action = input
#     if action == 'deposit':
#         dep = input("how much would you like to deposit?\n")
#         deposit(int(dep))
#         print('Your balance is ')
#         print(check_balance())
#         print(done())
#     elif action == 'withdraw':
#         withdr = input("how much would you like to withdraw?")

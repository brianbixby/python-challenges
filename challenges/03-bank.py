balance = 400

def deposit(num):
    global balance
    balance = balance + num
    return balance

def withdraw(num):
    global balance
    balance = balance - num
    return balance

def check_balance():
    global balance
    return balance

def how_can_i_help_you():
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if action == 'deposit':
        dep = input("how much would you like to deposit?\n")
        deposit(int(dep))
        print('Your balance is ')
        print(check_balance())
        print(done())
    elif action == 'withdraw':
        withdr = input("how much would you like to withdraw?")
        withdraw(int(withdr))
        print('Your balance is ')
        print(check_balance())
        print(done())
    elif action == 'check_balance':
        print('Your balance is ')
        print(check_balance())
        print(done())
    else:
        print("please respond with exact spelling and capitalization.")
        print(how_can_i_help_you())

def done():
    cust_re = input("Can we help you with anything else? (yes, no)\n")
    if cust_re == 'yes':
        print(how_can_i_help_you())
    elif cust_re == 'no':
        print("Have a nice day!")
    else:
        print("please respond with exact spelling and capitalization.")
        print(done())

print("Welcome to Chase bank.")
how_can_i_help_you()

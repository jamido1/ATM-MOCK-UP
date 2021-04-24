import datetime
import random

today = datetime.datetime.now()

current_time = today.strftime("%Y-%m-%d\n%H:%M:%S")

database = {}


def init():
    print('*****' * 30)
    print(f"***** *WELCOME TO PHOENIX BANK* *****\n{current_time}")

    print("Do you have an account with us?")
    print("                                        ")

    reply = int(input("\nPress (1) for YES\nPress (2) for NO\nPress (3) to EXIT.... \n "))

    if reply == 1:
        login()
    elif reply == 2:
        accountRegister()
    elif reply == 3:
        quit()
    else:
        print("Invalid Option Selected")
        init()


def accountRegister():
    print('*****' * 20)
    print("***** Registration Portal *****")

    first_name = input("Enter your First Name\n")
    last_name = input("Enter your Last Name\n ")
    email = input("Enter your Email address\n")
    password = input(" Create your password\n ")

    account_num = generate_random_number()
    card_num = generate_random_number()
    balance = 0
    database[account_num] = [first_name, last_name, email, password, card_num, balance]

    print("**** Your account has been successfully created ****")
    print(f"Your account number is: {account_num}")
    print(" Kindly deposit into your account to activate it")

    login()


def login():
    print("                                               ")
    print("*************** WELCOME TO THE LOGIN PORTAL ******************")

    user_account_number = int(input("Kindly enter your Account Number to login\n"))

    if user_account_number in database.keys():
        user_password = input('Enter your password\n ')
        for user_details in database.values():
            if user_password == user_details[3]:
                print("                     ")
                print("Login Successful")
                print(f'Welcome {user_details[0]} {user_details[1]}\n')
                bank_operations(user_details)
            else:
                print("Invalid password.....")
                print("Press 1 to try again\nPress 2 to exit")
                response = int(input("Press (1) to Try Again\nPress (2) to Exit"))
                if response == 1:
                    login()
                else:
                    quit()
    else:
        print("Invalid Account Number")
        print("Press 1 to try again")
        print("Press 2 to exit")
        response = int(input("Your response: "))
        if response == 1:
            login()
        else:
            quit()


def logout():
    print("                                       ")
    print("Logout Successful")
    print("                                        ")
    init()


def quit():
    print("We hate that you have to go, see you some other time")


def bank_operations(user):
    print('*********What would you like to do?*********')
    print("                                                                ")

    pick = int(input(
        "\nPress (1) to deposit\nPress (2) to withdraw\nPress (3) to check balance\nPress (4) for complaint\nPress (5) to logout\nPress (6) to exit\n"))

    if pick == 1:
        deposit(user)
    elif pick == 2:
        withdrawal(user)
    elif pick == 3:
        balance_enquiry(user)
    elif pick == 4:
        customer_care(user)
    elif pick == 5:
        logout()
    elif pick == 6:
        quit()
    else:
        print("Invalid option selected")
        bank_operations(user)


def withdrawal(user):
    print("                                            ")
    print("*****Withdrawal*****")
    with_amount = int(input("How much would you like to withdraw?\n"))
    if user[-1] == 0:
        print("Your balance is empty. Please make deposits")
    elif user[-1] < with_amount:
        print("Insufficient funds. Make more deposits")
    else:
        user[-1] -= with_amount
        print(f"Take your cash\n${with_amount}")

    bank_operations(user)


def balance_enquiry(user):
    print(f"Your balance is ${user[-1]}")
    bank_operations(user)


def deposit(user):
    print("                                         ")
    print("*****Deposit*****")
    deposit_amount = int(input("How much would you like to deposit?\n"))
    user[-1] += deposit_amount

    print(f"Your deposit of ${deposit_amount} was successful.")
    bank_operations(user)


def customer_care(user):
    print('This is the Customer Care Unit')
    complaint = input("how may we be of help?\n")
    print("Your complaint has been noted. You will be contacted shortly")
    print("Thank you")
    bank_operations(user)


def generate_random_number():
    return random.randrange(0000000000, 9999999999)


init()
# @jamido

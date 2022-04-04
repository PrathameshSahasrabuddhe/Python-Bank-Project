import datetime
import ImpProgs

count = int(1001)

def Deposit(balance:int, amount:int)->int:
    """
    Function to increase the balance according to given amount

    Args:
        balance (int): Balance before depositing the amount
        amount (int): Amount of money to be deposited

    Returns:
        int: Returns the new balance
    """
    balance+=amount
    return balance


def Withdraw(balance:int, amount:int)->int:
    """
    Function to decrease the balance according to given amount

    Args:
        balance (int): Balance before depositing the amount
        amount (int): Amount of money to be withdrawn

    Returns:
        int: Returns the new balance after withdrawal
    """
    balance-=amount
    return balance


def Show()->None:
    """
    Function to show all the details
    """
    pass


def CreateAccount():
    name = str(input("Enter full name: "))
    initial_bal = int(input("Enter initial deposit: "))
    global count
    acc_no = str(count)
    count+=1
    now = datetime.datetime.now()
    transactions = [f"{initial_bal} on {now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}"]


def login():
    account_num = str(input("Enter Your Account Number: "))
    if ImpProgs.FileCheck(account_num):
        print("Account Found!")
    else:
        print("Account Not Found!")
        choice = str(input("Do you want to open a new account?(Yes/No) "))
        if choice.casefold()=="yes":
            pass
        else:
            BasicOptions()
    


def BasicOptions():
    print(f"********** Welcome **********")
    choice = int(input("If you have an account, enter \"1\"\n"
                        "If you want to open an account, enter \"2\"\n"
                        "To exit, enter \"0\"\n"
                        "Enter your choice: "))

    if choice==1:
        pass
    elif choice==0:
        exit()


if __name__ == '__main__':
    BasicOptions()
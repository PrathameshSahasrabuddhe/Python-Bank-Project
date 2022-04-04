import datetime
import ImpProgs


def CreateAccount():
    name = str(input("Enter your full name: "))
    initial_balance = int(input("Enter initial deposit: "))
    x = Bank(name, initial_balance)


class Bank:

    acc_count = int(0)
    #### Remove Static Method and add file to read last assigned account number ####
    def AccountNumber():
        acc_no = int(0)
        data = str(0)
        complete = ImpProgs.FullPath("LastAccNumber")

        with open(complete,"r") as file:
            data = int(file.readline())
            acc_no = data
            Bank.acc_count = acc_no
            data+=1

        with open(complete, "w") as file:
            data = str(data)
            file.write(data)

    def __init__(self, name, balance):
        Bank.AccountNumber()
        self.acc_no = str(Bank.acc_count)
        self.name = name
        self.balance = balance
        self.now = datetime.datetime.now()
        self._transaction_list = [f"{balance} on {self.now.day}-{self.now.month}-{self.now.year} {self.now.hour}:{self.now.minute}:{self.now.second}"]
        ImpProgs.CreateNewFile(self.name, self.acc_no, self.balance, self._transaction_list)
        self.balance = int(self.balance)
        print("Your account Number is: ", self.acc_no)
        Bank.BankBasedOptions(self.name, self.acc_no, self.balance, self._transaction_list)

    def deposit(name:str, acc_no:str, balance:int, amount:int, transaction_list:list):
        now = datetime.datetime.now()
        if amount<=0:
            print("Amount should be greater than 0")
        else:
            balance+=amount
            transaction_list.append(f"{amount} on {now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}")
            ImpProgs.WriteToFile(acc_no, name, acc_no, balance, transaction_list)
            print("Deposit Successful!")
            Bank.BankBasedOptions(name, acc_no, balance, transaction_list)

    def withdraw(name:str, acc_no:str, balance:int, amount:int, transaction_list:list):
        now = datetime.datetime.now()
        if amount>balance:
            print("Not Enough Balance!")
        else:
            balance-=amount
            amount*=-1
            transaction_list.append(f"{amount} on {now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}")
            ImpProgs.WriteToFile(acc_no, name, acc_no, balance, transaction_list)
            print("Withdrawal Successful!")
            Bank.BankBasedOptions(name, acc_no, balance, transaction_list)

    def login():
        account_number = str(input("Enter Account Number: "))
        if ImpProgs.FileCheck(account_number):
            print("Account Found!")
            name, acc_no, balance, transaction_list = ImpProgs.ReadFromFile(account_number)
            Bank.BankBasedOptions(name, acc_no, balance, transaction_list)

        

        else:
            print("Account does not exist!")
            ch = str(input("Do you want to create an account?(Yes/No) "))
            if ch.casefold()=="yes":
                CreateAccount()
            else:
                Bank.EntryOptions()


    def show(name:str, acc_no:str, balance:int, transaction_list:list):
        print(f"Name: {name}")
        print(f"Account Number: {acc_no}")
        print(f"Balance: {balance}")
        for i in transaction_list:
            print("   ",i)
        print("\n\n")



    def BankBasedOptions(name:str, acc_no:str, balance:int, trasaction_list:list):
        while True:
            print("Select an option from below")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                amount = int(input("Enter amount to be deposited: "))
                Bank.deposit(name, acc_no, balance, amount, trasaction_list)
            elif choice == 2:
                amount = int(input("Enter amount to be withdrawn: "))
                Bank.withdraw(name, acc_no, balance, amount, trasaction_list)
            elif choice == 3:
                Bank.show(name, acc_no, balance, trasaction_list)
            elif choice == 4:
                print("\n\n")
                Bank.EntryOptions()



    def EntryOptions():
        print(f"********** Welcome **********")
        choice = int(input("If you have an account, enter \"1\"\n"
                            "If you want to open an account, enter \"2\"\n"
                            "To exit the Bank, enter \"0\"\n"
                            "Enter your choice: "))

        if choice==1:
            Bank.login()
        elif choice==2:
            CreateAccount()
        elif choice==0:
            exit()
        else:
            exit()


if __name__ == '__main__':
    Bank.EntryOptions()
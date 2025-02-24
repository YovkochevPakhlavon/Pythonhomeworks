class Account:
    def __init__(self,account_number,name,balance: float):
        self.account_number=account_number
        self.name= name
        self.balance = balance
    def __str__(self):
        return f'{self.account_number}: {self.name}, {self.balance}'
class Bank:
    file_name = 'accounts.txt'
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    def load_from_file(self):
        try:
            with open(self.file_name,'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(", ")
                    self.accounts[data[0]]=[data[1],float(data[2])]
        except FileNotFoundError:
            self.accounts = {}
    def create_account(self,new_account: Account):
        if new_account.account_number in self.accounts.keys():
            print("There is an account with the given account number!\n")
        else:
            self.accounts[new_account.account_number]=[new_account.name,new_account.balance]
            print("The account added successfully!\n")
    def view_account(self,acc_num):
        if acc_num in self.accounts.keys():
            return f'Account Number: {acc_num}, Name: {self.accounts[acc_num][0]}, Balance: {self.accounts[acc_num][1]}\n'
        else:
            return f"There is no account with '{acc_num}' account number!\n"
    def deposit(self,acc_num,amount):
        if acc_num in self.accounts.keys() and amount >= 0:
            self.accounts[acc_num][1] += amount
            print("The amount added successfully to the balance!\n")         
        elif amount < 0:
            print(f"Deposit amount cannot be negative!\n")
        else:
            print(f"There is no account with '{acc_num}' account number!\n")   
    def withdraw(self,acc_num,amount):
        if acc_num in self.accounts.keys() and self.accounts[acc_num][1] >= amount and amount >=0:
            self.accounts[acc_num][1] -= amount
            print(f"The amount withdrew successfully!\n")  
        elif self.accounts[acc_num][1] < amount:
            print(f"You do not have enough money to withdraw {amount}\n")    
        elif amount < 0:
            print(f"Withdraw amount cannot be negative !\n")  
        else:
            print(f"There is no account with '{acc_num}' account number!\n")  
    def save_to_file(self):
            with open(self.file_name,'w') as file:
                for acc_num, data in self.accounts.items():
                    file.write(f'{acc_num}, {data[0]}, {data[1]}\n')    
            print(f"The accounts saved to the {self.file_name}!\n")  

    def run(self):
        while True:
            print("Welcome!")
            print("1. Create a new account")
            print("2. View an account details")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Save accounts")
            print("6. Load accounts")
            print("7. Exit")            
            option = int(input("Enter the option number: "))
            if option == 1:
                new_acc_num = input("Enter a new account number: ")
                new_name = input("Enter owner name: ")
                new_balance = float(input("Enter balance:"))
                new_account = Account(new_acc_num,new_name,new_balance)
                self.create_account(new_account)
            elif option == 2:
                acc_num = input("Enter Account number: ")
                print(self.view_account(acc_num))
            elif option == 3:
                acc_num = input("Enter Account number: ")
                amount = float(input("Enter the amount you want to deposit:"))
                self.deposit(acc_num,amount)
            elif option == 4:
                acc_num = input("Enter Account number: ")
                amount = float(input("Enter the amount you want to withdraw:"))
                self.withdraw(acc_num,amount)   
            elif option == 5:
                self.save_to_file()  
            elif option == 6:
                self.load_from_file()
            elif option == 7:
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again!\n")                     

if __name__ == "__main__":
    app = Bank()
    app.run()



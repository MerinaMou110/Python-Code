
from abc import ABC, abstractmethod
#User
class User_Account(ABC):
    accounts=[]
    loan_limit=2
    account_counter=0
    is_bankrupt=False
    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        User_Account.account_counter+=1
        self.account_number=User_Account.account_counter
        self._balance = 0
        self._transactions=[]
        self._loan_taken=0
        self._total_loan_amount=0

        
    def deposit(self,amount):
        if amount >= 0:
            self._balance += amount
            self._transactions.append(f"Deposited ${amount}")
            print(f"\n--> Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("\n--> Invalid deposit amount")

    # @abstractmethod
    def withdraw(self,amount):
        if amount >=0 and amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrew ${amount}")
            print(f"\nWithdrew ${amount}. New balance: ${self._balance}")
        elif self._balance==0:
            print("The bank is bankrupt")
            User_Account.is_bankrupt=True
        else:
            print("\nWithdrawal amount exceeded")
            print(f"\nYour Bank balance ${self._balance}")


    def check_balance(self):
        return f"Available balance: {self._balance}"
    
    def check_transection(self):
        return self._transactions
    
    def take_loan(self,loan_amount):
        if self._loan_taken<User_Account.loan_limit:
            self._loan_taken+=1
            self._total_loan_amount+=loan_amount
            self.deposit(loan_amount)
            self._transactions.append(f"Loan taken:${loan_amount}")
            return f"Loan of ${loan_amount} taken successfully"
        else:
            return "You have reached the maximum limit for loans"
    
    def transfer(self,amount,recipient):
        if self._balance >= amount:
            self.withdraw(amount)
            recipient.deposit(amount)
            self._transactions.append(f"Transferred ${amount} to {recipient.name}")
            recipient._transactions.append(f"Received ${amount} from {self.name}")
            return f"Transferred ${amount} to {recipient.name} successfully"
        else:
            return "Insufficient funds for transfer"
        
    
    def __str__(self):
        return f"Account Type: {self.account_type}\nName: {self.name}\nEmail: {self.email}\nAccount Number: {self.account_number}"


class SavingsAccount(User_Account):
    def __init__(self, name, email, address,interestRate):
        super().__init__(name, email, address, "Savings")
        self.interestRate = interestRate

    def apply_interest(self):
        interest = self._balance*(self.interestRate/100)
        print("\n--> Interest is applied !")
        self.deposit(interest)


class CurrentAccount(User_Account):
    def __init__(self, name, email, address,limit):
        super().__init__(name, email, address,"Current")
        self.limit=limit

    def withdraw(self, amount):
        if amount > 0 and (self._balance - amount) >= -self.limit:
            self._balance -= amount
            self._transactions.append(f"Withdrew ${amount}")
            print(f"\nWithdrew ${amount}. New balance: ${self._balance}")
        else:
            print("\n--> Invalid withdrawal amount or overdraft limit reached")
            



class BankAdmin:
    user_accounts=[]
    def __init__(self) -> None:
        # self.user_accounts=[]
        self._total_balance = 0
        self._total_loan_amount = 0

    def create_account(self,name,email,address,account_type):
        if account_type=='Savings':
            ItRate=int(input("Interest rate:"))
            account=SavingsAccount(name,email,address,ItRate)
        elif account_type=='Current':
            limit=int(input("Overdraft Limit:"))
            account=CurrentAccount(name,email,address,limit)
        else:
            return "Invalid account type"
        BankAdmin.user_accounts.append(account)
        # return f"Account created successfully.\n{account}"
        return account
    
    def delete_account(self, account_number):
        for acc in BankAdmin.user_accounts:
            if acc.account_number == account_number:
                BankAdmin.user_accounts.remove(acc)
                return f"Account {account_number} deleted successfully"
        return f"Account {account_number} not found" 
    def view_all_accounts(self):
        account_list=[]
        for account in BankAdmin.user_accounts:
            account_list.append(account)
        return account_list
    
    
    def check_total_balance(self):
        # print(self.user_accounts)
      
        for account in BankAdmin.user_accounts:
      
            self._total_balance += account._balance
            print(f"Account {account.account_number} Balance: {account._balance}")  


        return f"Total balance of the bank: {self._total_balance}"

    def check_total_loans(self):
        total_loans = 0
        for account in BankAdmin.user_accounts:
            total_loans += account._total_loan_amount
        return f"Total loan amount taken by all users: {total_loans}"

    def toggle_loan_feature(self, status):
        if status == 'on':
            User_Account.loan_limit = 2
            return "Loan feature enabled"
        elif status== 'off':
            User_Account.loan_limit = 0
            return "Loan feature disabled"
        else:
            return "Invalid input"
   
def user_system():
    user = None
    admin = BankAdmin()
    while True:
        if user is None:
            print("\n1. Register\n2. Login\n3. Exit")
            choice = input("Enter choice: ")
            
            if choice == '1':
                name = input("Name: ")
                email = input("Email: ")
                address = input("Address: ")
                acc_type = input("Account Type (Savings/Current): ")
                user = admin.create_account(name, email, address, acc_type)
                print(f"Account created successfully!\n{user}")

            
            elif choice == '2':
                acc_no = int(input("Enter account number: "))
                accounts=admin.view_all_accounts()
                for acc in accounts:
                    if acc.account_number == acc_no:
                        user = acc
                        break
                else:
                    print("Account not found.")
            
            elif choice == '3':
                break
        else:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Take Loan\n5. Transfer\n6. Logout")
            option = input("Enter option: ")
            
            if option == '1':
                amount = float(input("Enter deposit amount: "))
                user.deposit(amount)
            
            elif option == '2':
                amount = float(input("Enter withdrawal amount: "))
                user.withdraw(amount)
            
            elif option == '3':
                print(user.check_balance())
            
            elif option == '4':
                loan_amount = float(input("Enter loan amount: "))
                print(user.take_loan(loan_amount))
            
            elif option == '5':
                recipient_acc_no = int(input("Enter recipient's account number: "))
                amount = float(input("Enter transfer amount: "))
                for acc in admin.view_all_accounts():
                    if acc.account_number == recipient_acc_no:
                        recipient = acc
                        break
                else:
                    print("Account does not exist.")
                    continue
                print(user.transfer(amount, recipient))
            
            elif option == '6':
                user = None
            
            else:
                print("Invalid option.")

# Admin 
def admin_system():
    admin = BankAdmin()
    while True:
        print("\n1. View All Accounts\n2. Delete Account\n3. Total Balance\n4. Total Loans\n5. Toggle Loan Feature\n6. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            show_acc=admin.view_all_accounts()
            for acc in show_acc:
                print(f"Account Number: {acc.account_number}, Name: {acc.name},Email: {acc.email} Type: {acc.account_type}")
        
        elif choice == '2':
            acc_no = int(input("Enter account number to delete: "))
            print(admin.delete_account(acc_no))
        
        elif choice == '3':
            print(admin.check_total_balance())
        
        elif choice == '4':
            print(admin.check_total_loans())
        
        elif choice == '5':
            status = input("Enter 'on' to enable or 'off' to disable loan feature: ")
            print(admin.toggle_loan_feature(status))
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n1. User System\n2. Admin System\n3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            user_system()
        
        elif choice == '2':
            admin_system()
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
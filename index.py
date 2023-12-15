class ATM :
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"your balance is ${self.balance}")

    def deposit(self,amount):
     self.balance +=amount
     print(f"${amount} has been deposited. Your new balance is ${self.balance}")

    def withdraw(self,amount):
         if amount > self.balance:
             print("Insufficient funds.")

         else:
            self.balance -=amount
            print(f"${amount} has been withdraw. Your new balance is ${self.balance}")

def main():
    atm = ATM()

    while True:
        print("\nWelcome to Simple ATM")
        print("1. check balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choise = input("enter your choise (1-4): ")

        if choise == "1":
            atm.check_balance()

        elif choise == "2":
            amount = float(input("enter deposit amount : $ "))
            atm.deposit(amount)

        elif choise == "3":
            amount = float(input("enter withdrawal amount : $ "))
            atm.withdraw(amount)
            

        elif choise == "4":
            print("Thank you for using ATM. Thank You. ")
            break

        else:
            print("invalid choice")
            

if __name__ == "__main__":
    main()



            



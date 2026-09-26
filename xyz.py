class Atm:
    #constructor := it is special type of function that help to create and initialize the object value
    def __init__(self):  #when we want to declare the varible we declare those in the init method

        self.pin=""
        self.balance=0

        self.menu()

    def menu(self):
        while True:

            user_input=input(""" hello ,how would you like to proceeds
            1.enter to create pin
            2.enter to deposit
            3.enter to withdraw
            4.enter to check balance
            5.enter to exit """)

            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
            elif user_input=="5":
                print("bye")
                break
            else:
                print("invalid number")

    def create_pin(self):
        self.pin=input("enter your pin:").strip()
        print("pin create succefully")

    def deposit(self):
        temp=input("enter your pin").strip()

        print("debugging stored pin:",repr(self.pin))
        print("debugging enter pin: ",repr(temp))
        if self.pin==temp:
            amount=int(input("enter amount"))
            self.balance+=amount
            print("deposite amount successfully")
        else:
            print("invaid pin")
            
    def withdraw(self):
        temp=input("enter yout pin").strip()
        
        print("debugging stored pin:",repr(self.pin))
        print("debugging enter pin: ",repr(temp))
        if self.pin==temp:
            amount=int(input("enter the how much amount you want to withdraw"))
            if amount<= self.balance:
                self.balance-=amount
                print("withdraw amount successfully")
            else:
                print("insufficient balance")
        else:
            print("invalid pin")

    def check_balance(self):
        temp=input("enter your pin")
        
        print("Entered PIN :", repr(temp))
        print("Stored PIN  :", repr(self.pin))
        if self.pin==temp:
            print("balance:",self.balance)
        else:
            print("invalid pin")
    
    
sbi=Atm()



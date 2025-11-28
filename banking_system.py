print(f"Welcome to Bank!")

class Banking:
    
    def __init__(self, name, initial_amount = 0):
        self.name = name
        self.balance = initial_amount
        
    
    def deposit(self, deposit_amount):
        if deposit_amount >= 500:
            self.balance += deposit_amount
            return self.balance
            
        else:
            print("You can't deposit less than BDT 500")
          
    def withdraw(self, withdraw_amount):
        if self.balance > 0:
            if self.balance  >= withdraw_amount:
                self.balance -= withdraw_amount
                return self.balance
            else:
                print("You request amount exceed your current balance.")
        else:
            print("You can't withdraw BDT 0!!!") 
    
    def __str__(self):
        return f"Hello {self.name}, Balace: ৳ {self.balance}"
    
name = input("Enter your name: ")
balance = int(input("Enter initial amount(BDT): "))


obj_bank = Banking(name, balance)
print(obj_bank)

deposit_amount = 0

while deposit_amount < 500:
    deposit_amount = int(input("Enter deposit amount(BDT) must >= 500: "))
    if deposit_amount < 500:
        break
    print("Please deposit at least 500.")
    

obj_bank.deposit(deposit_amount)
print(obj_bank)

withdraw_amount = int(input("Enter your withdraw amount(BDT): "))
obj_bank.withdraw(withdraw_amount)

print(obj_bank)


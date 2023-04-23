
class BankAccount:
    def __init__(self,acc_no,bal,doo,name):
        self.acc_no = acc_no
        self.bal = bal
        self.date_of_opening=doo
        self.customer_name=name

    def deposit(self,damount):
        self.bal = self.bal + damount
        print(f"${damount} has been deposited in your account.")

    def withdraw(self,wamount):
        if wamount > self.bal:
            print("Insufficient Balance.")
        else:
            self.bal = self.bal - wamount
            print(f"${wamount} has been withdrawn from your account.")

    def check_balance(self):
        print(f"Current Balance:${self.bal}")

    def print_customer_details(self):
        print("Name:",self.customer_name)
        print("Account Number:",self.acc_no)
        print("Date of opening:",self.date_of_opening)
        print(f"Balance:${self.bal}")
        print("-------------------------------------------------------")
    
        
# Input customer details
ac_no_1 = BankAccount(2345,1000 ,"01-01-2011", "Toninho Takeo")
ac_no_2 = BankAccount(1234,2000, "11-03-2011", "Astrid Rugile")
ac_no_3 = BankAccount(2312,3000, "12-01-2009", "Orli Kerenza")
ac_no_4 = BankAccount(1395,3000, "01-01-2011", "Luciana Chika")
ac_no_5 = BankAccount(6345,4000, "01-05-2011", "Toninho Takeo")
print("Customer Details:")
ac_no_1.print_customer_details()
ac_no_2.print_customer_details()
ac_no_3.print_customer_details()
ac_no_4.print_customer_details()
ac_no_5.print_customer_details()
print("=============================")
ac_no_4.print_customer_details()
# Current balance is $3000.
# $1000 has been deposited in your account.
ac_no_4.deposit(1000)
ac_no_4.check_balance()
# Your current balance $4000.
# You want to withdraw $5000
ac_no_4.withdraw(5000)
# Output:
# Insufficient balance.
#The customer withdraw $3400.
ac_no_4.withdraw(3400)
ac_no_4.check_balance()

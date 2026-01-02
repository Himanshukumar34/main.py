import random 
print("welcome to sasta atm")
pin=6696968
while True:
      num1=int(input("Enter your pin"))
      if num1==pin:
        print("your password is correct ")
        break
      else:
         print("Your password is invalid")
current_balance=10000
def check_balance():
  
    print(f" your balance is {current_balance}")
def deposit_money():
    deposit=int(input("Enter your amount: "))
    if num1>10000 or num1<500:
        print(f"your limit is cross ")
    else:
        current_balance+=deposit
    +  print(f"succesfully deposit{current_balance}")
def withdraw_money():
    withdraw=int(input("Enter your amount :"))
    if withdraw>10000 or withdraw<500:
        print(f"your amount is invalid ")
    elif withdraw>current_balance:
        print("you have not sufficent money")
    else:
        current_balance-=withdraw
        print("succesfully withdraw")
while True:
    print("1.check_balance")
    print("2.Deposit_money")
    print("3.withdrw money")
    print("4.exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        check_balance()
    elif choice==2:
        deposit_money()
    elif choice==3:
        withdraw_money()
    elif choice==4:
        print("Thank you ")
        break
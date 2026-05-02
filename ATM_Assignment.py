balance=0
balance=int(input("enetr balance:"))
print("Welcome to Habib Bank Limited:")
while True:
    print(" \n menu:")
    print("1. check balance")
    print("2. deposit money")
    print("3. withdraw money")
    print("4. exit")
    choice=int(input("enetr choice:"))
    if choice==1 :
     print(" your current balance is:",balance)
    elif choice==2:
     depositamount=int(input("enetr amount you waant to deposit:"))
     print("privious balance is :",balance)
     balance=balance+depositamount
     print("updated balance is :",balance)
     print("deposited amount is :",depositamount)
    elif choice==3:
     withdrawamount=int(input("enter amount you want to withdraw"))
     if withdrawamount>balance:
         print(" insufficient balance:")
     else:
        print("privious balance is :",balance)
        balance=balance-withdrawamount
        print("updated balance is :",balance)
        print(" withdraw amount is :",withdrawamount)
    elif choice==4:
     print(" EXIT")
     print(" THNK YOU")
     break
    else:
     print(" invalid choice")
     
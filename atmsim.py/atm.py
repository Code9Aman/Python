#Generating a program to stimulate a ATM machine
#Pin,Check Balance, Deposit, Withdrawl,

balance = 10000
while True:
    print("#####SBK ATM####")
    print("1.Check Balance")
    print("2.Quick Withdrawal")
    print("3.Deposit")
    print("4.Exit")

    choice = input("Enter your Operations(1-4):")
    if choice== "1":
        print(f"{balance}")


    elif choice== "2":
        amount=float(input("Enter Ammount:"))
        if amount<0:
            print("Error, please enter a valid ammount.")
        elif amount>balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"${amount} Successfully Withdrawn!!\n")


    elif choice=="3":
        deposit=float(input("Enter the ammount to deposit:"))
        if deposit<0:
            print("Error, please enter a valid ammount", end="")
        else:
            balance += deposit
            print(f"Updated Balance: ${balance}")
            
    elif choice == "4":
        print("Thank you for using SBK ATM.")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
            
        



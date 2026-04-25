def atm():
    correct_pin = "1234"
    balance =   # Initial balance
    attempts = 0
    max_attempts = 3

    # 🔐 PIN Authentication
    while attempts < max_attempts:
        pin = input("Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("\n✅ Login Successful!\n")
            break
        else:
            attempts += 1
            print(f"❌ Incorrect PIN. Attempts left: {max_attempts - attempts}")

    if attempts == max_attempts:
        print("\n🚫 Too many incorrect attempts. Card blocked.")
        return

    # 🔁 ATM Menu Loop
    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        # 💰 Check Balance
        if choice == "1":
            print(f"\n💰 Your balance is: ₹{balance}")

        # ➕ Deposit
        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"✅ ₹{amount} deposited successfully.")
            else:
                print("❌ Invalid amount.")

        # ➖ Withdraw
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("❌ Invalid amount.")
            elif amount > balance:
                print("⚠️ Insufficient balance! Transaction denied.")
            else:
                balance -= amount
                print(f"✅ ₹{amount} withdrawn successfully.")

        # 🚪 Exit
        elif choice == "4":
            print("\n👋 Thank you for using the ATM!")
            break

        else:
            print("❌ Invalid option. Please choose between 1-4.")


# 🚀 Run the ATM
atm()
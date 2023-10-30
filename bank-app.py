# Define the file names for bank data and transaction log
bank_data_file = "Bank Data.txt"
transaction_log_file = "Transaction Log.txt"

# Function to get the current balance
def get_balance():
    try:
        with open(bank_data_file, "r") as file:
            balance = float(file.read())
            return balance
    except FileNotFoundError:
        return 0.0

# Function to make a deposity
def make_deposit():
    amount = input("How much would you like to deposit? $")
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please provide a valid positive number for the deposit.")
        return

    balance = get_balance()
    balance += amount

    with open(bank_data_file, "w") as file:
        file.write(str(balance))

    with open(transaction_log_file, "a") as file:
        file.write(f"Deposit: +R{amount}\n")

    print(f"Current Balance: R{balance}")

# Function to make a withdrawal
def make_withdrawal():
    amount = input("How much would you like to withdraw? $")
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please provide a valid positive number for the withdrawal.")
        return

    balance = get_balance()
    if amount > balance:
        print("Insufficient funds for the withdrawal.")
        return

    balance -= amount

    with open(bank_data_file, "w") as file:
        file.write(str(balance))

    with open(transaction_log_file, "a") as file:
        file.write(f"Withdrawal: -R{amount}\n")

    print(f"Current Balance: R{balance}")

# Main program
while True:
    print("Would you like to make a transaction? (Yes or No)")
    user_choice = input().strip().lower()

    if user_choice != "yes":
        break

    print("Would you like to make a deposit or withdrawal? (Deposit or Withdrawal)")
    transaction_type = input().strip().lower()

    if transaction_type == "deposit":
        print(f"Current Balance: R{get_balance()}")
        make_deposit()
    elif transaction_type == "withdrawal":
        print(f"Current Balance: R{get_balance()}")
        make_withdrawal()
    else:
        print("You provided an invalid input. Please choose 'Deposit' or 'Withdrawal'.")

print("Thank you for using the banking application.")
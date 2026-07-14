# Create a Simple ATM Withdrawal Program.

balance = 50000

while True:
    try:
        withdrawal_amount = int(input("Enter the amount to withdraw: "))
        if withdrawal_amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        elif withdrawal_amount > balance:
            raise ValueError(f"Insufficient funds. Your current balance is: #{balance}")
        else:
            new_balance = balance - withdrawal_amount
            print("Withdrawal successful. Your new balance is:", new_balance)
            break
    except ValueError as error:
        print(error)
    finally:
        print("Thank you for using the ATM withdrawal program.")

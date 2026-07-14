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
            balance -= withdrawal_amount
            print("Withdrawal successful. Your new balance is:", balance)
    except ValueError as error:
        print(error)

    finally:
        print("Thank you for using the ATM withdrawal program.")
    if balance <= 0:
        print("Your account balance is zero. You cannot make further withdrawals.")
        break


    Question =  input("Do you want to try again? (yes/no): ").lower()
    if Question == "no":
        print("Thank you for using the ATM withdrawal program.")
        break
    else:
        continue
        
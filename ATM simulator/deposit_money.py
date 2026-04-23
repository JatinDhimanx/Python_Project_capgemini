import datetime


def deposit(balance, transaction_history):
    amount_str = input("Enter the amount to deposit: RS.")
    amount = float(amount_str)
    
    if amount > 0:
        balance = balance + amount
        current_time = datetime.datetime.now()
        transaction_history.append(f"Deposited: RS.{amount} at {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\nSuccessfully deposited RS.{amount}. Your new balance is RS.{balance}")
    else:
        print("\nInvalid amount. Please enter a positive number.")
        
    return balance, transaction_history

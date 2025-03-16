
def deposit():
    while True:
        amount = input("Please enter your deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be more than zero")
        else:
            print("Please enter a number")
    return amount

deposit()
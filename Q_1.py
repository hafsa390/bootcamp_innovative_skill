# A banking application allows users to withdraw money. The function withdraw(balance,
# amount) should check if the withdrawal amount is greater than the balance. If yes, it should
# raise an exception "Insufficient funds", otherwise return the new balance.

def  withdraw(balance, amount):  # the total amount and withdrawal amount is passed to the withdraw() function

    print("Your balance is", balance, "and the withdrawal amount is:", amount)

    if amount > balance:
        raise Exception("Insufficient funds")
    else:
        return balance - amount


if __name__ == "__main__":

    total_balance = 1000
    print("Your total balance is", total_balance)
    withdrawal = int(input("Enter the amount you want to withdraw: "))  # Taking the withdrawal amount as user input
    print("You want to withdraw", withdrawal)

    new_balance = withdraw(total_balance, withdrawal)   # The new balance after withdrawal

    print("Your new balance is", new_balance)




MAX_LINES = 3


def deposit():
    while True:

        amount = input("What would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)    # convertendo string para valor numérico

            if amount > 0:
                break

            else:
                print("Amount must be greater than 0")

        else:
            print("Please enter a number")

    return amount


deposit()

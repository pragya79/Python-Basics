MAX_LINES=5 
MIN_BET=50
MAX_BET=1000
def deposit():
    while True:
        amount=input("How much you want to deposit? Rs ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:print("Sorry!Amount must be greater than 0.")
        else:("Please enter a number")
    return amount
def get_no_of_lines():
    while True:
        lines=input("Enter number of lines to bet on(1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:print("Enter a valid number of lines.")
        else:("Please enter a number")
    return lines
def get_bet():
     while True:
        amount=input("How much do you wanna bet? ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:print(f"Amount must be between Rs{MIN_BET}-Rs{MAX_BET}")
        else:("Please enter a number")
     return amount

def main():
    balance=deposit()
    lines=get_no_of_lines()
    total_bet=bet*lines
    bet=get_bet()
    print(f"You are betting {bet} on {lines}.Total bet is = Rs {total_bet}.")
main()
    
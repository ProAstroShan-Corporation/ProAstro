import random
from IPython.display import clear_output

# Function to clear the output
def clear():
    clear_output(wait=True)

# Get starting money
while True:
    try:
        money_input = int(input("Enter your starting money: "))
        if money_input > 0:
            if money_input <= 1000:
                if money_input >= 20:
                    money = money_input
                    break
                else:
                    print("Too less, go big or go home")
            else:
                print("Stop Capping!")
        else:
            print("Please enter a positive numerical value.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

clear()
print(f"Starting money: {money}")

win_streak = 0
loss_streak = 0

# Game loop
while True:
    # Check for win/loss conditions at the start of the loop
    if money <= 0:
        print("You've run out of money!")
        break

    if money > 1000:
        print("Get Out!")
        break

    if money < 50 and money > 0:
        print("You are running out")
        while True:
            choice = input("Please reconsider your choices, do you want to continue? Type yes or no: ").lower()
            if choice in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please type yes or no.")
        if choice == "no":
            print("Come back when you have more money")
            break
        else:
            clear() # Clear after user decides to continue

    secret_number = random.randint(1, 50)

    # Get bet amount
    while True:
        try:
            bet = int(input(f"You have {money} money. Enter your bet: "))
            if bet > 0 and bet <= money:
                break
            else:
                print("Invalid bet amount.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    print(f"Secret number is: {secret_number}")

    # Check if user wants to continue
    while True:
        choice = input("Do u want to continue? Type yes or no: ").lower()
        if choice in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please type yes or no.")

    if choice == "no":
        print("Remember 90% of Gamblers Quit Before They Win Big ")
        break

    # Clear only after the user has chosen to continue
    clear()

    if secret_number < 40:
        print("You fail")
        money -= bet
        win_streak = 0
        loss_streak += 1
        print(f"Current money: {money}")
        print(f"Loss streak: {loss_streak}")
    else:
        print("You win")
        money += bet
        loss_streak = 0
        win_streak += 1
        print(f"Current money: {money}")
        print(f"Win streak: {win_streak}")

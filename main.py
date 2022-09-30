## credit and gratitude to Tech With Tim #
#
#
#
#
import random


MAX_LINES = 4
MAX_BET = 1000000
MIN_BET = 4

ROWS = 4
COLS = 4

symbol_count = {
    "L": 2,
    "E": 4,
    "V": 4,
    "I": 4,
    "7": 1,
    "2": 3,
    "9": 5,


}

symbol_value = {
    "L": 500,
    "E": 75,
    "V": 50,
    "I": 25,
    "7": 1000,
    "2": 250,
    "9": 100,

}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
         for i, column in enumerate(columns):
             if i != len(columns) - 1:
                 print(column[row], end=" | ")
             else:
                 print(column[row], end="")

         print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(" Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(" Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:        
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break

            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = int(bet) * int(lines)
        if total_bet > balance <= 0:
            print(f" You do not have enough to bet that amount, your current balance is: ${balance}")
            main()
        else:
            break
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, int(lines), int(bet), symbol_value)
    print(f"you won ${winnings}.")
    print(f" you won on lines: \n", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is : ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            quit()
        balance += spin(balance)

    print(f"You left with ${balance} ")


main()

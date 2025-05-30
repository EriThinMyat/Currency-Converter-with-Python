def show_help():
    print(
        "help        -> to see available command\n"
        "currencies  -> to see available currencies\n"
        "exchange    -> to exchange currencies\n"
        "history     -> to see exchange history\n"
        "clear       -> to clear history\n"
        "exit/quit   -> to exit program\n"
    )

def empty_history(history):
    if not history:
        print("No exchange history yet.")
        return True
    return False

def display_result(amount,from_currency,to_currency,converted):
    result = f"{amount:,.2f} {from_currency} is {converted:,.2f} {to_currency}"
    return result


def show_history(history):
    if empty_history(history): return
    print("Your Exchange History")
    for ind,record in enumerate(history,1):
        print(f"{ind}. {record}")

def show_currencies(rates):
    print("Available Currencies and Rates (related to MMK)")
    for currency,rate in rates.items():
        print(f"- {currency} : {rate}")

def currency_exchange(rates,history):
    try:
        amount = float(input("Enter amount: "))

    except ValueError:
        print("Invalid amount. Please enter valid amount.")
        return
    
    if amount <= 0:
        print("Error: amount can't be zero or negative.")
        return

    from_currency = input("From: ").strip().upper()
    to_currency = input("To: ").strip().upper()

    if from_currency not in rates or to_currency not in rates:
        print("Unsupported currency. Type 'currencies' to see available currencies.")
        return

    amount_in_mmk = amount * rates[from_currency]
    converted = amount_in_mmk / rates[to_currency]

    result = display_result(amount,from_currency,to_currency,converted)
    print(result)
    history.append(result)

def clear_history(history):
    if empty_history(history): return
    history.clear()
    print("All histories cleared.")

def currency_converter():

     #exchange rates relative to mmk

    rates = {
    "MMK" : 1.0,
    "USD" : 2100.0,
    "EUR" : 2375.0,
    "JPY" : 15.0,
    "KRW" : 1.53,
    "SGD" : 1550.0,
    "CNY" : 295.0,
    "THB" : 60.0
}

    history = []
    quit_command = ["exit","quit"]

    while True:

        user_input = input("> ").strip().lower()

        if user_input in quit_command:
            break

        elif user_input == "help":
            show_help()
            continue

        elif user_input == "currencies":
            show_currencies(rates)

        elif user_input == "exchange":
            currency_exchange(rates,history)
            continue

        elif user_input == "history":
            show_history(history)
            continue

        elif user_input == "clear":
            clear_history(history)
            continue

        else:
            print("Invalid input. Type 'help' to view valid command.")

    
if __name__ == "__main__":
    currency_converter()

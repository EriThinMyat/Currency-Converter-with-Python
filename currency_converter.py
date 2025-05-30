def show_supported_currencies(rates):
    print(f"Supported currencies: {', '.join(rates.keys())}")


def currency_converter():

    #exchange rates relative to mmk
    rates = {
        "MMK": 1.0,
        "USD": 0.000476,
        "EUR": 0.000421,
        "JPY" : 0.068,
        "KRW" : 0.6533,
        "SGD" : 0.000613,
        "CNY" : 0.0034,
        "THB" : 0.0155
    }

    quit_command = ["exit","quit"]
   
    while True:

        user_input = input("Enter amount to exchange: ").strip().lower()

        if user_input in quit_command:
            break

        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid input. Please enter like '1 usd' or '1 USD'.")
            continue
        
        try:
            amount = float(parts[0])
            from_currency = parts[1].upper()

        except ValueError:
            print("Invalid input. Please enter valid amount.")
            continue

        to_currency = input("Converted to: ").strip().upper()

        if from_currency not in rates:
            show_supported_currencies(rates)
            continue

        if to_currency not in rates:
            show_supported_currencies(rates)
            continue

        amount_in_mmk = amount / rates[from_currency]
        converted = amount_in_mmk * rates[to_currency]

        print(f"{amount:.2f} {from_currency} is {converted:.2f} {to_currency}")

if __name__ == "__main__":
    currency_converter()
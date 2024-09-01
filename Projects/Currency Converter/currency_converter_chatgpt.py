import requests

def get_currency_input(prompt):
    """Prompt the user for a currency input and return the uppercase version."""
    return input(prompt).upper()

def get_valid_amount():
    """Prompt the user for a valid numeric amount greater than 0."""
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("The amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("The amount must be a numeric value!")

def perform_currency_conversion(init_currency, target_currency, amount, api_key):
    """Perform currency conversion and return the converted amount."""
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    headers = {'apikey': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Sorry, there was a problem: {e}")
        quit()

    result = response.json()

    if 'result' in result:
        return result['result']
    else:
        print("Sorry, there was a problem with the conversion. Please try again later.")
        quit()

def main():
    """Main function to execute the currency conversion program."""
    init_currency = get_currency_input("Enter an initial currency: ")
    target_currency = get_currency_input("Enter a target currency: ")
    amount = get_valid_amount()

    api_key = 'wFHczokIaD7aE6PNFGf6pss5euJp76lA'

    converted_amount = perform_currency_conversion(init_currency, target_currency, amount, api_key)

    print(f"{amount} {init_currency} = {converted_amount} {target_currency}")

if __name__ == "__main__":
    main()

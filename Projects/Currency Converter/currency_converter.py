import requests

init_currency = input("Enter an initial currency: ")
target_currency = input("Enter an target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be a numeric value!")
        continue

    if amount == 0:
        print("The amount must be greater than 0")
        continue
    else:
        break

url = ("https://api.apilayer.com/fixer/convert?to="
        + target_currency + "&from=" + init_currency
        + "&amount=" + str(amount))
headers = {
    'apikey': 'wFHczokIaD7aE6PNFGf6pss5euJp76lA',
}

response = requests.get(url, headers=headers)
result = response.json()

# Get the converted amount
converted_amount = result['result']

print(f"{amount} {init_currency} = {converted_amount} {target_currency}")

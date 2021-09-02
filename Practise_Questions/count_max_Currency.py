amount = int(input("Enter amount: "))
# list of currencies in descending order
currency = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
output = {}
max_currency = 0
while amount>0:
    for i in range(len(currency)):
        if amount == currency[i]:
            output.update({amount: 1})
            amount = 0
        elif amount < currency[i]:
            pass
        elif amount > currency[i]:
            max_currency = currency[i]
            count = amount//max_currency

            output.update({max_currency: count})
            amount = amount-(max_currency*count)
            break

print(output)



stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 320
}

total = 0

print("Welcome to Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock] * quantity
        total = total + investment

        print("Investment Value =", investment)
    else:
        print("Stock not found! Please enter a valid stock name.")

print("\nTotal Investment Value =", total)
print("Thank you for using Stock Portfolio Tracker.")
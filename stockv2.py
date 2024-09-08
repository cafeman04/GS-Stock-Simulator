import requests

stocks = []

stock_input = input("Which stock do you want to see?: ")
stocks.append(stock_input)
while True:
    repeater = input("Any other stocks or 'CONTINUE'?: ")
    if repeater.upper() == 'CONTINUE':
        break
    else:
        stocks.append(repeater)

buy_date = '2023-05-04'
# input(f"What date do you want to buy them? (YYYY-MM-DD): ")
sell_date = '2023-06-05'
# input(f"What date do you want to sell them? (YYYY-MM-DD): ")
shares = 5
# input("How many stocks do you want to buy?: ")


def find_close(stock, date):
    response = requests.get(f'https://api.polygon.io/v1/open-close/{stock}/{date}?adjusted=true&apiKey={API-key}').json()
    return response['close']

class Company():
    def __init__(self, ticker):
        self.ticker = ticker
        self.profit = round((find_close(ticker, sell_date) * shares - find_close(ticker, buy_date) * shares), 2)

for company in stocks:
    apple = Company(company)

print(apple.profit)




        








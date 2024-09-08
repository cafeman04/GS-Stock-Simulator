import gspread
import requests
import time
from oauth2client.service_account import ServiceAccountCredentials


#Google API Credentials
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json',scope)
client = gspread.authorize(creds)
sheet = client.open('StockSheet').sheet1
# Enter API Key
API-key = None 
API-token = None

#Creating companies with tickers and cell locations
class Company():
    def __init__(self, ticker,week0, week1, week2, week3, week4):
        self.ticker = ticker
        self.week0 = week0
        self.week1 = week1
        self.week2 = week2
        self.week3 = week3
        self.week4 = week4

apple = Company('AAPL', [7,5], [7,8], [7,9], [7,10], [7,11])
microsoft = Company('MSFT',[8,5], [8,8], [8,9], [8,10], [8,11])
nvidia = Company('NVDA',[9,5],[9,8], [9,9], [9,10], [9,11])
airbnb = Company('ABNB',[10,5],[10,8], [10,9], [10,10], [10,11])
intuit = Company('INTU', [11,5],[11,8], [11,9], [11,10], [11,11])
    
dates = ["2024-02-26", "2024-03-01", "2024-03-08", "2024-03-15", "2024-03-21"]
companies = [apple,microsoft,nvidia,airbnb,intuit]

#Close Price Function - uses 2 APIs because first one doesn't work sometimes
def find_close(stock, date):
    response = requests.get(f'https://api.polygon.io/v1/open-close/{stock}/{date}?adjusted=true&apiKey={API-key}').json()
    if response['status'] == "NOT_FOUND":
        response = requests.get(f'https://api.stockdata.org/v1/data/eod?symbols={stock}&date={date}&sort=True&api_token={API-token}').json()
        return str(response['data'][0]['close'])
    else:
        return str(response['close'])

        
#Loops through each company and each date for each cell
tick = 0
for company in companies:
    for date in dates:
        week = "week" + str(tick)
        sheet.update_cell(getattr(company, week)[0], getattr(company, week)[1], find_close(company.ticker, date))
        time.sleep(13)
        tick += 1
    tick = 0



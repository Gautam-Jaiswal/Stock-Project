import requests

Stock_API_Key = 'Your API Key'


#Search for stocks having a particular keyword
def FindParticularStock(search_stock):
    url = 'https://www.alphavantage.co/query?'
    parameters = {
        'function': 'SYMBOL_SEARCH',
        'keywords': search_stock,
        'apikey': Stock_API_Key
    }
    r = requests.get(url=url, params=parameters)
    r.raise_for_status()
    data = r.json()['bestMatches']
    return data


#Returns yesterdays and day before yesterday data of a particular stock
def StockSearch(symbol):
    url = 'https://www.alphavantage.co/query?'
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': Stock_API_Key
    }
    r = requests.get(url=url, params=parameters)
    data = list(r.json()['Time Series (Daily)'].items())
    return data
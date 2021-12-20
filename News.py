import requests
import datetime

News_API_Key = 'Your API Key'

today = datetime.datetime.today()
before = datetime.datetime.today()-datetime.timedelta(days=5)

def getNews(stock_name):
    url = 'https://newsapi.org/v2/everything?'
    parameters = {
        'from': before,
        'to': today,
        'qInTitle': stock_name,
        'sortBy': 'popularity',
        'language': 'en',
        'apiKey': News_API_Key
    }
    r = requests.get(url=url, params=parameters)
    r.raise_for_status()
    data = r.json()['articles'][:5]
    return data

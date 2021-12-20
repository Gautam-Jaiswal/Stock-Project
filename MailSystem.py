import smtplib
import json
import Stock
import News
import time

Email = 'Your Mail'
Password = 'Your Password'

def sendMail():
    with open('data.json', 'r') as file:
        data_json = json.load(file)
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=Email,password=Password)
    for data in data_json:
        d = Stock.StockSearch(data)
        news = News.getNews(data)
        yesterday = d[0]
        day_before = d[1]
        connection.sendmail(from_addr=Email,
                            to_addrs='Receiving Address',
                            msg=f'Subject:{data} {yesterday[0]} Stock Details\n\n'
                                f'Opening: {yesterday[1]["1. open"]}\n'
                                f'Closing: {yesterday[1]["2. high"]}\n'
                                f'Low: {yesterday[1]["3. low"]}\n'
                                f'Close: {yesterday[1]["4. close"]}')
        time.sleep(3)
        connection.sendmail(from_addr=Email,
                            to_addrs='Receiving Address',
                            msg=f'Subject:{data} {day_before[0]} Stock Details\n\n'
                                f'Opening: {day_before[1]["1. open"]}\n'
                                f'Closing: {day_before[1]["2. high"]}\n'
                                f'Low: {day_before[1]["3. low"]}\n'
                                f'Close: {day_before[1]["4. close"]}')
        time.sleep(3)
        for new in news:
            connection.sendmail(from_addr=Email,
                                to_addrs='Receiving Address',
                                msg=f'Subject:{new["title"]}\n\n'
                                    f'{new["description"]}\n'
                                    f'{new["url"]}'.encode("utf-8"))
            time.sleep(3)
    connection.close()
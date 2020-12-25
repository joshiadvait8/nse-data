from bs4 import BeautifulSoup
import requests

headers = {
    'Host': 'www1.nseindia.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'
}

def getprice(symbol):
    url = 'https://www.nse-india.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?&symbol='+symbol+'&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17'
    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html,'lxml')
    l=soup.select('div#container >div.content_big>div#wrapper_btm>table span b')
    price = l[0].text.split()
    print(l[0].text)
    # Actual price of equity derivative
    print(price[1])
    # print(l[0].text)
    # print(l[1].text)

def get_values_from_option_chain(symbol):

    # Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=" + expdate
    Base_url = f'https://www.nse-india.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?&symbol={symbol}&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17'
    page = requests.get(Base_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    table_cls_2 = soup.find(id="octable")
    req_row = table_cls_2.find_all('tr')

    strike_price_list = []
    OI_calls_list = []
    OI_puts_list =[]

    for row_number, tr_nos in enumerate(req_row):
        # print(row_number)
        # print(tr_nos)
        # This ensures that we use only the rows with values
        if row_number <= 1 or row_number == len(req_row) - 1:
            continue

        td_columns = tr_nos.find_all('td')
        # print(BeautifulSoup(str(td_columns[11]),'html.parser').get_text())

        #append strike price
        strike_price = int(float(BeautifulSoup(str(td_columns[11]), 'html.parser').get_text()))
        strike_price_list.append(strike_price)
        #append oi calls
        OI_calls = BeautifulSoup(str(td_columns[1]), 'html.parser').get_text()
        OI_calls_list.append(OI_calls)
        #append oi puts
        OI_puts = BeautifulSoup(str(td_columns[21]), 'html.parser').get_text()
        OI_puts_list.append(OI_puts)
        
    # print()
    # print("-------------strike_price-------------")
    # print (strike_price_list)
    # print("*****OI Calls******")
    # print(OI_calls_list)
    # print("*****OI puts******")
    # print(OI_puts_list)
    return strike_price_list

get_values_from_option_chain('INFY')
getprice('INFY')


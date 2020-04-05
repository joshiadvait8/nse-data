import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
import xlwt 
from xlwt import Workbook 


def get_strike_price_from_option_chain(symbol, expdate):
# Workbook is created 
    wb = Workbook() 
    sheet1 = wb.add_sheet('Sheet 1')
    Base_url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=" + expdate
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
          "X-Requested-With": "XMLHttpRequest"}

    page = requests.get(Base_url,headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    table_cls_2 = soup.find(id="octable")
    req_row = table_cls_2.find_all('tr')

    strike_price_list = []
    calls_OI_list = []
    calls_OI_change_list = []
    puts_OI_list = []
    puts_OI_change_list = []
    

    for row_number, tr_nos in enumerate(req_row):

        # This ensures that we use only the rows with values
        if row_number <= 1 or row_number == len(req_row) - 1:
            continue

        td_columns = tr_nos.find_all('td')
        
        strike_price = int(float(BeautifulSoup(str(td_columns[11]), 'html.parser').get_text()))
        strike_price_list.append(strike_price)
        
        calls_OI = (BeautifulSoup(str(td_columns[1]), 'html.parser').get_text())
        if calls_OI=='-':
            calls_OI=0
        calls_OI_list.append(calls_OI)
        calls_OI_change = (BeautifulSoup(str(td_columns[2]), 'html.parser').get_text())
        calls_OI_change_list.append(calls_OI_change)
        
        puts_OI = (BeautifulSoup(str(td_columns[21]), 'html.parser').get_text())
        puts_OI_list.append(puts_OI)
        puts_OI_change = (BeautifulSoup(str(td_columns[20]), 'html.parser').get_text())
        puts_OI_change_list.append(puts_OI_change)
#         #print ("Number of items in the list = ",len(calls_OI_list))
#         j = len(calls_OI_list)
# #         print (j)
#         i=len(calls_OI_list)
        
# #     print (i)
    
    
    print ("Strike Price",strike_price_list)
    print ("CALLS OI",calls_OI_list)
#     print ("Change In CALLS OI",calls_OI_change_list)
#     print ("PUTS OI",puts_OI_list)
#     print ("Change In PUTS OI",puts_OI_change_list)    
      
#     for idx in range(len(strike_price_list)):
#         print(strike_price_list[10])
#         sheet1.write(idx, 0, strike_price_list[idx])
#         sheet1.write(idx, 0, idx)

    sheet1.write(0, 0, "calls_OI_list")
    sheet1.write(0, 1, "calls_OI_change_list")
    sheet1.write(0, 2, "strike_price_list")
    sheet1.write(0, 3, "puts_OI_change_list")
    sheet1.write(0, 4, "puts_OI_list")

    for x in range(len(strike_price_list)):
        sheet1.write(x+1, 0, calls_OI_list[x])
        sheet1.write(x+1, 1, calls_OI_change_list[x])
        sheet1.write(x+1, 2, strike_price_list[x])
        sheet1.write(x+1, 3, puts_OI_change_list[x])
        sheet1.write(x+1, 4, puts_OI_list[x])
   
    wb.save(r"C:\Users\Personal\Desktop\FNO\\"+symbol+".xls") 
        
# here end of functionbasically


f = open(r'FNO.csv')
lines = [line.strip() for line in f]
# print(lines[1])
for i in range(1,len(lines)):
    print(lines[i])
    get_strike_price_from_option_chain(lines[i], "30APR2020")
    
    
        
# wait apan pahile fakt 5 script taky karan 144 loopmadhe
#     wb.save(i.xls) 
#     sheet1 = wb.add_sheet(symbol[]) 
        #print(symbol[row])
#     get_strike_price_from_option_chain(symbol[i], "30APR2020")

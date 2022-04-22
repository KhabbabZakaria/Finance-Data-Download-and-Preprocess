import pandas as pd
import csv
import requests
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

current_dir = os.getcwd()

symbol = 'DOW'
years = [1,2]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
for year in years:
    for month in months:
        #CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey=E6XK1RI9FGCFWII9&datatype=csv'
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=' + symbol + '&interval=1min&slice=year' + str(year) + 'month' + str(month) + '&apikey=E6XK1RI9FGCFWII9&datatype=csv'
        output_dir = os.path.join(current_dir, symbol)
        output_file = os.path.join(current_dir, symbol, symbol + 'year' + str(year) + 'month' + str(month) + '.csv')
        print(output_file)
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            header = my_list[0]
            my_list.pop(0)
            df = pd.DataFrame(my_list, columns=header)
            df.to_csv(output_file, index=False)
        time.sleep(15)


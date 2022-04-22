import pandas as pd
import yfinance as yf


data = yf.download('AAPL', start="2020-03-23", end="2022-03-10", interval = "1m")

print(data)
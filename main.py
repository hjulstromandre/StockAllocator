import yfinance as yf
import pandas as pd
import plotly.express as px


ticker_symbols = ['AAPL', 'MSFT', 'IBM', 'GE', 'T', 'XOM', 'CSCO', 'PG', 'KO', 'JNJ']


historical_data = yf.download(ticker_symbols, start="2004-01-01", end="2024-01-01")


close_prices = historical_data['Close']


fig = px.line(close_prices, title='Historical Closing Prices of Large-Cap Stocks')
fig.update_layout(xaxis_title='Date', yaxis_title='Price (USD)', legend_title='Ticker Symbols')
fig.show()

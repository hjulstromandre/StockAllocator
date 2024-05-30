import yfinance as yf
import pandas as pd
import plotly.express as px


ticker_symbols = ['AAPL', 'MSFT', 'IBM', 'GE', 'T', 'XOM', 'CSCO', 'PG', 'KO', 'JNJ']


historical_data = yf.download(ticker_symbols, start="2004-01-01", end="2024-01-01")


close_prices = historical_data['Close']

num_stocks = len(ticker_symbols)
equal_weight = 1 / num_stocks
portfolio_value = close_prices.apply(lambda x: x * equal_weight, axis=1).sum(axis=1)
msft_prices = close_prices['MSFT']

fig = px.line()
fig.add_scatter(x=portfolio_value.index, y=portfolio_value, name='Equally-Weighted Portfolio')
fig.add_scatter(x=msft_prices.index, y=msft_prices, name='MSFT Stock')
fig.update_layout(title='Comparison of Equally-Weighted Portfolio and MSFT Stock',
                  xaxis_title='Date', yaxis_title='Price (USD)')
fig.show()

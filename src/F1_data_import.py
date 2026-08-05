import yfinance as yf
import matplotlib.pyplot as plt

def get_data(ticker, start_date, end_date):
    #import the raw data from Yahoo Finance
    rawdata = yf.download(ticker, start=start_date, end=end_date, multi_level_index = False)
    return rawdata

if __name__ == '__main__':
    ticker = 'GOOG'
    start_date = '2025-01-01'
    end_date = '2026-01-01'
    df = get_data(ticker, start_date, end_date)

    print(df.tail())
    df.plot(y='Close', 
                   title=f'{ticker} Closing Prices from {start_date} to {end_date}', 
                   xlabel='Date', 
                   ylabel='Closing Price (USD)')
    plt.show()


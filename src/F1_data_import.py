import yfinance as yf

def get_data(ticker, start_date, end_date):
    #import the raw data from Yahoo Finance
    rawdata = yf.download(ticker, start=start_date, end=end_date, multi_level_index = False)
    # save the raw data to a CSV file
    with open('data/RAW.csv', 'w') as f:
        rawdata.to_csv(f)
    return rawdata


if __name__ == '__main__':
    ticker = 'GOOG'
    start_date = '2023-01-01'
    end_date = '2026-01-01'

    df = get_data(ticker, start_date, end_date)
    print(f'RAW DATA SAVED TO CSV, {len(df)} rows')

    '''import matplotlib.pyplot as plt
    df.plot(y='Close', 
                   title=f'{ticker} Closing Prices from {start_date} to {end_date}', 
                   xlabel='Date', 
                   ylabel='Closing Price (USD)')
    plt.show()'''

import pandas as pd

def add_data():
    df = pd.read_csv(f'data/RAW_{ticker}_{start_date}_{end_date}.csv', index_col=0, parse_dates=True)

    #for the below calculations closing data is used as it is more indicative of the market
    #calculate 5-day, 10-day, and 20-day moving averages
    df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['MA20'] = df['Close'].rolling(window=20).mean()

    #calculate the simple volatility (20-day rolling standard deviation)
    df['Volatility'] = df['Close'].rolling(window=20).std()

    #calculate the volume rate of change (20-day fractional change in volume)
    df['VolumeROC'] = df['Volume'].pct_change(periods=20)

    #calculate 1 day, 5 day and 10 day momentum 
    df['Momentum-1'] = df['Close'].diff(periods=1)
    df['Momentum-5'] = df['Close'].diff(periods=5)
    df['Momentum-10'] = df['Close'].diff(periods=10)

    #save the processed data to a CSV file
    with open(f'data/PROCESSED_{ticker}_{start_date}_{end_date}.csv', 'w') as f:
        df.to_csv(f)
    return df

if __name__ == '__main__':
    ticker = 'GOOG'
    start_date = '2025-01-01'
    end_date = '2026-01-01'
    df = add_data()

    print('PROCESSED DATA SAVED TO CSV')
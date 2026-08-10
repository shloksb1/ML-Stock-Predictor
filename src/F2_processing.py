import pandas as pd

def add_data():
    # load the raw data from CSV
    df = pd.read_csv(f'data/RAW.csv', index_col=0, parse_dates=True)

    #for the below calculations closing data is used as it is more indicative of the market

    #calculate 5-day, 20-day and 50-day moving averages
    MA5 = df['Close'].rolling(window=5).mean()
    MA20 = df['Close'].rolling(window=20).mean()
    MA50 = df['Close'].rolling(window=50).mean()

    df['MA50_Distance'] = (df['Close'] - MA50) / df['Close']  # distance from 50-day MA as a fraction
    df['MA5-20_Crossover'] = (MA5 - MA20)/MA20  # difference between 5-day and 20-day moving averages as a fraction
    #calculate the simple volatility (20-day & 50-day rolling standard deviation)
    df['Volatility20'] = df['Close'].rolling(window=20).std()
    df['Volatility50'] = df['Close'].rolling(window=50).std()

    #calculate the volume rate of change (20-day & 50-day fractional change in volume)
    df['VolumeRO20'] = df['Volume'].pct_change(periods=20)
    df['VolumeRO50'] = df['Volume'].pct_change(periods=50)

    #calculate 5, 10, 20 and 50 day momentum (difference between prices) 
    df['Momentum-5'] = df['Close'].diff(periods=5)
    df['Momentum-10'] = df['Close'].diff(periods=10)
    df['Momentum-20'] = df['Close'].diff(periods=20)
    df['Momentum-50'] = df['Close'].diff(periods=50)



    # drop the open, high, close and low values as these do not greatly contribute to the 20 day prediction 
    # and these values are highly correlated with each other and other things like moving averages and momentum, 
    # so they can be removed to improve model performance.
    # having percentage indicators instead of absolute values is more useful and prevents high correlation with other data.
    df.drop(['Open', 'High', 'Low'], axis=1, inplace=True)

    #save the processed data to a CSV file
    with open('data/PROCESSED.csv', 'w') as f:
        df.to_csv(f)
    return df

if __name__ == '__main__':
    df = add_data()
    print(f'\033[96mPROCESSED DATA SAVED TO CSV, {len(df)} rows\033[0m')

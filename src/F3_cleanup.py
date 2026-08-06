import pandas as pd

def cleanup(delete):
    # load the processed data from CSV 
    df = pd.read_csv(f'data/PROCESSED.csv', index_col=0, parse_dates=True)

    #drop any rows with null values (so at least the first 20 if not more)
    df.dropna(inplace=True)

    #save the data to a new file
    with open('data/CLEANED.csv', 'w') as f:
        df.to_csv(f)
    
    #if specified, delete the raw and processed data as they wont be used
    if delete:
        import os
        os.remove('data/RAW.csv')
        os.remove('data/PROCESSED.csv')
    return df

if __name__ == '__main__':
    df = cleanup(delete=True)
    print(f'CLEANED DATA SAVED TO CSV, {len(df)} rows')
    
import pandas as pd
from joblib import load
from sklearn.model_selection import train_test_split

def test_model():
    #load the data from CSV 
    df = pd.read_csv(f'data/CLEANED.csv', index_col=0, parse_dates=True)

    #load the model from joblib file
    model = load('model/model.joblib')

    X = df.drop('Close', axis=1)
    Y = (df['Close'].shift(-20) > df['Close']).astype(int)

    #split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=False)
    
    
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None) 

    # this tests the input data on correlation with itself
    # this highlights large overlaps than should be removed to improve model performance
    corr_matrix = X_train.corr()
    #print(f"Correlation Matrix:\n{corr_matrix}")

    threshold = 0.85
    corr_pairs = corr_matrix.unstack()
    corr_pairs = corr_pairs[corr_pairs < 1]  # Exclude self-correlation
    high_corr =  corr_pairs[corr_pairs > threshold]
    print(f"Highly Correlated Pairs: \n{high_corr}\n")

    #this tests how much/ the importance of each data input to the model. this can also higlight data that needs to be removed.
    importances = pd.Series(model.feature_importances_, index=X_train.columns)
    importances.sort_values(ascending=False, axis=0, inplace=True)
    print(f"Feature Importances:\n{importances}\n")


if __name__ == '__main__':
    test_model()
    print(f'\033[96mMODEL TESTED\033[0m')
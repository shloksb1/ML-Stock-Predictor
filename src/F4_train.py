import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt 
from joblib import dump

def train_model():
    #load the data from CSV 
    df = pd.read_csv(f'data/CLEANED.csv', index_col=0, parse_dates=True)

    #separate the data into the input features and the expected output (target)
    X = df.drop('Close', axis=1)  # drop the 'Close' column
    Y = (df['Close'].shift(-20) > df['Close']).astype(int) # sets target to  1 if the 20 day price is higher than today & 0 otherwise

    #split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=False)

    #the next two lines assign the model to a variable and then train it using the training data
    #the model is an XGBoost model which is using binary cross entopy as the loss function 
    model = XGBClassifier(n_estimators=1000,
                          learning_rate=0.05,
                          max_depth=4,
                          early_stopping_rounds=10,
                          eval_metric='logloss',) 
    model.fit(X_train, Y_train,
              verbose=False,
              eval_set=[(X_test, Y_test)])

    predictions = model.predict_proba(X_test)[:, 1]

    #calculate the log loss between the predicted and actual values
    logloss = log_loss(Y_test, predictions)
    
    print(f"\033[42mLog Loss: {logloss:.4f}\033[0m")

    #plot the actual vs predicted values
    '''plt.plot(Y_test.values, label='Actual')
    plt.plot(predictions, label='Predicted')
    plt.title('Actual vs Predicted')
    plt.xlabel('Index')
    plt.ylabel('Close Price')
    plt.legend(loc='lower right')
    plt.show()'''
    
    return model

if __name__ == '__main__':
    model = train_model()
    dump(model, 'model/model.joblib')
    print(f'\033[96mMODEL TRAINED & SAVED TO JOBLIB\033[0m')

    

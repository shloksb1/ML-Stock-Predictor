import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt 

def train_model():
    #load the data from CSV 
    df = pd.read_csv(f'data/CLEANED.csv', index_col=0, parse_dates=True)

    #separate the data into the input features and the expected output (target)
    X = df
    #this line sets the target to be 1 if the next day's price is higher than today's price, and 0 otherwise
    Y = (df['Close'].shift(-1) > df['Close']).astype(int) 

    #split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=False)

    #the next two lines assign the model to a variable and then train it using the training data
    #the model is an XGBoost model which is using squared error as the loss function 
    #it will train 100 iterations to fit the data
    model = XGBRegressor(objective='binary:logistic', n_estimators=100) 
    model.fit(X_train, Y_train)

    predictions = model.predict(X_test)

    #convert the predictions to binary values (1 if predicted value > 0.5, else 0)
    #predictions = (predictions > 0.5).astype(int)

    #calculate the log loss between the predicted and actual values
    logloss = log_loss(Y_test, predictions)
    
    print(f"Log Loss: {logloss:.4f}")

    #plot the actual vs predicted values
    plt.plot(Y_test.values, label='Actual')
    plt.plot(predictions, label='Predicted')
    plt.title('Actual vs Predicted')
    plt.xlabel('Index')
    plt.ylabel('Close Price')
    plt.legend(loc='lower right')
    plt.show()
    
    return model

if __name__ == '__main__':
    model = train_model()
    print(f'MODEL TRAINED')

    

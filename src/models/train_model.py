from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pickle
from sklearn.preprocessing import MinMaxScaler


# Function to train the model
def train_neural_network(X, y):
    # Splitting the data into training and testing sets
    xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=123, stratify=y)

    # Scale the data using MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(xtrain)
    xtrain_scaled = scaler.transform(xtrain)
    xtest_scaled = scaler.transform(xtest)
    
    # fit/train the model
    MLP = MLPClassifier(hidden_layer_sizes=(2,2), batch_size=50, max_iter=200)
    MLP.fit(xtrain_scaled, ytrain)
    
    # Save the trained model
    with open('models/NNmodel.pkl', 'wb') as f:
        pickle.dump(MLP, f)

    return MLP, xtest_scaled, ytest

# Import accuracy score
from sklearn.metrics import confusion_matrix, accuracy_score

# # Function to predict and evaluate
def evaluate_model(model, xtest_scaled, ytest):
    # make predictions on train
    y_pred = model.predict(xtest_scaled)

    # Calculate the accuracy score
    accuracy = accuracy_score(ytest, y_pred)

    # Calculate the confusion matrix
    confusion_mat = confusion_matrix(ytest, y_pred)

    # return accuracy and confusion_mat
    return accuracy, confusion_mat
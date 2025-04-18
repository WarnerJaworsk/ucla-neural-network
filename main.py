# from setuptools import find_packages, setup


# setup(
#     name='src',
#     packages=find_packages(),
#     version='0.1.0',
#     description='Credit Risk Model code structuring',
#     author='Swapnil Kangralkar',
#     license='',
# )

from src.data.make_dataset import load_data
from src.visualization.visualize import plot_correlation_GRE_TOEFL, plot_confusion_matrix, plot_loss_curve
from src.features.build_features import create_dummy_vars
from src.models.train_model import train_neural_network
from src.models.predict_model import evaluate_model

if __name__ == "__main__":
    # Load and preprocess the data
    data_path = "data/raw/Admission.csv"
    df = load_data(data_path)

    # Create dummy variables and separate features and target
    X, y = create_dummy_vars(df)

    # Train the Neural Network model
    MLP, xtest, ytest = train_neural_network(X, y)

    # Evaluate the model
    accuracy, confusion_mat = evaluate_model(MLP, xtest, ytest)
    
    # Print evaluation results
    print(f"Accuracy: {accuracy}")
    print(f"Confusion Matrix:\n{confusion_mat}")
    
    # plot confusion matrix & loss curve
    plot_loss_curve(MLP)
    plot_confusion_matrix(ytest, MLP.predict(xtest), classes=['Class 0', 'Class 1'])
    plot_correlation_GRE_TOEFL(df)
    

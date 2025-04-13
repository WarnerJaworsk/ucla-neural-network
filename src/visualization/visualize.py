
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import numpy as np

def plot_correlation_GRE_TOEFL(data):
    plt.figure(figsize=(15,8))
    sns.scatterplot(data=data, x='GRE_Score', y='TOEFL_Score', hue='Admit_Chance')
    plt.savefig("relationship.png")

# Function to plot confusion matrix
def plot_confusion_matrix(y_test, y_pred, classes):
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, xticklabels=classes, yticklabels=classes)
    plt.xlabel('Predicted', fontsize=12)
    plt.ylabel('Actual', fontsize=12)
    plt.title('Confusion Matrix', fontsize=16)
    plt.savefig('confusion_matrix.png')
    
# Function to plot loss curve
def plot_loss_curve(MLP):
    loss_values = MLP.loss_curve_
    
    plt.figure(figsize=(10, 6))
    plt.plot(loss_values, label='Loss', color='blue')
    plt.title('Loss Curve')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig('loss_curve.png')
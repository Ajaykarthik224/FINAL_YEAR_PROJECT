from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import model_selection, neighbors
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class prepare_data:

    def __init__(self, path):
        super().__init__()
        self.path_of_file = path

    def prepare(self):
        # Read the csv file with the rainfall data
        data = pd.read_csv(self.path_of_file)

        # Remove rows with missing data
        data = data.dropna(how="any", axis=0)
        data.cov()
        data.corr()

        # Classify annual rainfall of more than 3000mm as flood = True else False
        data['FLOOD'] = data.apply(
            lambda row: True if row['annual'] > 3000 else False, axis=1)

        # Convert the [True False] values to [1,0] for easy processing
        data['FLOOD'].replace([True, False], [1, 0], inplace=True)

        # Separate the concept values and the target values and return it
        x = data.iloc[:, 1:19]
        y = data.iloc[:, -1]
        # print(x)
        # print(y)

        return [x, y]

import requests
import json
import config
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import model_selection, neighbors
from sklearn import preprocessing
from get_prediction_and_accuracy import get_prediction_and_accuracy
from sklearn.linear_model import LogisticRegression


def write_json(data, filename='output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def clear_output_file():
    with open("output.json") as json_file:
        data = json.load(json_file)

        data['scores'] = []
    write_json(data)


clear_output_file()
# datarequest.py
api_key = config.api_key
url = f'https://api.data.gov.in/resource/8e0bd482-4aba-4d99-9cb9-ff124f6f1c2f?api-key={api_key}&format=json&offset=0&limit=10000000'

data = requests.get(url).json()

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# csv_converter.py
with open('data.json') as json_file:
    data = json.load(json_file)

rainfall_data = data['records']

data_file = open('data_in_csv.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for rainfall in rainfall_data:
    if count == 0:

        header = rainfall.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(rainfall.values())

data_file.close()

# prepare_data.py
data = pd.read_csv('data_in_csv.csv')

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
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

# Plotting the data in the graph

c = data[['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']].mean().plot.line()
# c.hist()
plt.xlabel('Month', fontsize=20)
plt.ylabel('Mean Rainfall in mm', fontsize=20)
plt.show()

# time.sleep(5)
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
ax = data[['jan', 'feb', 'mar', 'apr', 'may', 'jun',
           'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'jf', 'mam', 'jjas', 'ond']].mean().plot.bar(width=0.5, edgecolor='k', align='center', linewidth=2)
plt.xlabel('Month', fontsize=30)
plt.ylabel('Monthly Rainfall', fontsize=20)
plt.title('Rainfall in India for all Months', fontsize=25)
ax.tick_params(labelsize=20)
plt.grid()
plt.ioff()
plt.show()

# prepare_model.py
minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
# print(minmax.fit(x).transform(x))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# print("Training Data:\n", x_train)
# print("Testing Data:\n", x_test)
y_train = y_train.astype('int')
y_test = y_test.astype('int')

# knn_algorithm.py
clf = neighbors.KNeighborsClassifier()
clf.fit(x_train, y_train)

# print("Predicted Values for the Floods:")
y_predict = clf.predict(x_test)
# print(y_predict)

x_train_std = minmax.fit_transform(x_train)
x_test_std = minmax.fit_transform(x_test)
knn_acc = cross_val_score(clf, x_train_std, y_train,
                          cv=3, scoring='accuracy', n_jobs=-1)
knn_proba = cross_val_predict(
    clf, x_train_std, y_train, cv=3, method='predict_proba')

# print(knn_acc)
# print("\nAccuracy Score:%f" %
#       (accuracy_score(y_test, y_predict)*100))

# print("Recall Score:%f" %
#       (recall_score(y_test, y_predict)*100))
# print("ROC score:%f" % (roc_auc_score(y_test, y_predict)*100))
# print(confusion_matrix(y_test, y_predict))
accuracy_score = accuracy_score(y_test, y_predict)*100

# print_to_file.py


def print_output_file(algorithm, prediction, accuracy):
    with open("output.json") as json_file:
        data = json.load(json_file)

        scores_to_be_written = {
            "algorithm": algorithm,
            "prediction": prediction,
            "accuracy": accuracy
        }

        data['scores'].append(scores_to_be_written)
    write_json(data)


def knn_algorithm(state_selected, month_selected):
    [prediction, accuracy] = get_prediction_and_accuracy(
        y_predict, accuracy_score, state_selected, month_selected).display_result()
    print(
        f"KNN Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")
    print_output_file("K Nearest Neighbor", prediction, accuracy)


# logistic_regression.py
minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
x_train_std = minmax.fit_transform(x_train)
y_train_std = minmax.transform(x_test)

lr = LogisticRegression()
lr.fit(x_train, y_train)
lr_acc = cross_val_score(lr, x_train_std, y_train,
                         cv=3, scoring='accuracy', n_jobs=-1)
lr_proba = cross_val_predict(
    lr, x_train_std, y_train, cv=3, method='predict_proba')
y_pred = lr.predict(x_test)

# print("\nAccuracy Score:%f" %
#       (accuracy_score(y_test, y_predict)*100))

# print("Recall Score:%f" %
#       (recall_score(y_test, y_predict)*100))
# print("ROC score:%f" % (roc_auc_score(y_test, y_predict)*100))
# print(confusion_matrix(y_test, y_predict))
accuracy_score = accuracy_score(y_test, y_pred))*100


def logistic_regression(state_selected, month_selected):
    [prediction, accuracy]=get_prediction_and_accuracy(
        y_predict, accuracy_score, state_selected, month_selected).display_result()
    print(
        f"Logistic Regression Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")
    print_output_file("Logistic Regression", prediction, accuracy)


def support_vector_algorithm(state_selected, month_selected):
    [prediction, accuracy]=get_prediction_and_accuracy(
        y_predict, accuracy_score, state_selected, month_selected).display_result()
    print(
        f"Support Vector Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")
    print_output_file("Support Vector", prediction, accuracy)


def decision_tree(state_selected, month_selected):
    [prediction, accuracy]=get_prediction_and_accuracy(
        y_predict, accuracy_score, state_selected, month_selected).display_result()
    print(
        f"Decision Tree Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")
    print_output_file("Decision Tree", prediction, accuracy)


knn_algorithm('Bihar', 'mar')
logistic_regression('Bihar', 'mar')
support_vector_algorithm('Bihar', 'mar')
decision_tree('Bihar', 'mar')

from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import model_selection, neighbors
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the csv file with the rainfall data
data = pd.read_csv('data/data_in_csv.csv')

# Remove rows with missing data
data = data.dropna(how="any", axis=0)
data.cov()
data.corr()

# Classify annual rainfall of more than 3000mm as flood = True else False
data['FLOOD'] = data.apply(
    lambda row: True if row['annual'] > 3000 else False, axis=1)

# Convert the [True False] values to [1,0] for easy processing
data['FLOOD'].replace([True, False], [1, 0], inplace=True)

# Separate the concept values and the target values
x = data.iloc[:, 1:19]
y = data.iloc[:, -1]
print(x)
print(y)


# Plotting the data in the graph

# c = data[['jan', 'feb', 'mar', 'apr', 'may', 'jun',
#           'jul', 'aug', 'sep', 'oct', 'nov', 'dec']]
# c.hist()
# plt.show()


# ax = data[['jan', 'feb', 'mar', 'apr', 'may', 'jun',
#            'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'jf', 'mam', 'jjas', 'ond']].mean().plot.bar(width=0.5, edgecolor='k', align='center', linewidth=2, figsize=(14, 6))
# plt.xlabel('Month', fontsize=30)
# plt.ylabel('Monthly Rainfall', fontsize=20)
# plt.title('Rainfall in India for all Months', fontsize=25)
# ax.tick_params(labelsize=20)
# plt.grid()
# plt.ioff()
# plt.show()

# Using SKLearn to prepare the model

minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
print(minmax.fit(x).transform(x))


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print("Training Data:\n", x_train.head())
print("Testing Data:\n", x_test.head())
y_train = y_train.astype('int')
y_test = y_test.astype('int')


# Using K Neighbors Algorithm to predict
clf = neighbors.KNeighborsClassifier()
clf.fit(x_train, y_train)

print("Predicted Values for the Floods:")
y_predict = clf.predict(x_test)
print(y_predict)

print("Actual Values for the Floods:")
print(y_test)


print("List of the Predicted Values:")
print(y_predict)

x_train_std = minmax.fit_transform(x_train)
x_test_std = minmax.fit_transform(x_test)
knn_acc = cross_val_score(clf, x_train_std, y_train,
                          cv=3, scoring='accuracy', n_jobs=-1)
knn_proba = cross_val_predict(
    clf, x_train_std, y_train, cv=3, method='predict_proba')
print(knn_acc)


print("\nAccuracy Score:%f" % (accuracy_score(y_test, y_predict)*100))
print("Recall Score:%f" % (recall_score(y_test, y_predict)*100))
print("ROC score:%f" % (roc_auc_score(y_test, y_predict)*100))
print(confusion_matrix(y_test, y_predict))

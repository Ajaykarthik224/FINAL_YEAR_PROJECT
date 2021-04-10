from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import model_selection, neighbors
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
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

data_in_json = open('data/data.json', 'r')
data_in_json = json.load(data_in_json)
state_names_list = list()
state_names_set = set()

for values in data_in_json['records']:
    state_names_set.add(values['subdivision'])

for i in state_names_set:
    state_names_list.append(i)

state_names_list.sort()

predicted_values_array = [y_predict[i:i + 17]
                          for i in range(0, len(y_predict), 17)]
predicted_values_array = predicted_values_array[:36]
print("Each state values:", len(predicted_values_array))
print("State list length:", len(state_names_list))

all_states_predicted = []

for state_name, predicted_value_for_each_state in enumerate(predicted_values_array):
    predicted_state_values = {"subdivision": state_names_list[state_name], "jan": predicted_value_for_each_state[0],
                              "feb": predicted_value_for_each_state[1],
                              "mar": predicted_value_for_each_state[2],
                              "apr": predicted_value_for_each_state[3],
                              "may": predicted_value_for_each_state[4],
                              "jun": predicted_value_for_each_state[5],
                              "jul": predicted_value_for_each_state[6],
                              "aug": predicted_value_for_each_state[7],
                              "sep": predicted_value_for_each_state[8],
                              "oct": predicted_value_for_each_state[9],
                              "nov": predicted_value_for_each_state[10],
                              "dec": predicted_value_for_each_state[11],
                              "annual": predicted_value_for_each_state[12],
                              "jf": predicted_value_for_each_state[13],
                              "mam": predicted_value_for_each_state[14],
                              "jjas": predicted_value_for_each_state[15],
                              "ond": predicted_value_for_each_state[16], }

    all_states_predicted.append(predicted_state_values)

# all_states_predicted_dict = {"records": []}
# for predicted_state_value_objects in all_states_predicted:
#     all_states_predicted_dict['records'].append(predicted_state_value_objects)

print(all_states_predicted[1])

state_selected = 'Andaman & Nicobar Islands'
month_selected = 'feb'

print()

print("Actual Values for the Floods:")
print(y_test)


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
# print(confusion_matrix(y_test, y_predict))

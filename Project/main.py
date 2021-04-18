from prepare_data import prepare_data
from prepare_model import prepare_model
from knn_algorithm import knn_algorithm
from frontend_gui import frontend_gui
from get_prediction_and_accuracy import get_prediction_and_accuracy
from logistic_regression import logistic_regression
from support_vector_algorithm import support_vector_algorithm
from decision_tree import decision_tree
from print_to_file import print_to_file
import os

os.remove("OutputFile.txt")
# Initalizing the prepare data by passing the CSV data file and getting the x and y values by calling the function.
[x, y] = prepare_data('data/data_in_csv.csv').prepare()

# Initalizing the model by passing the x and y values and getting the model by calling the prepare model function
[x_train, x_test, y_train, y_test] = prepare_model(
    x, y).prepare_training_and_testing_data()

# Getting the state and month from the user
[state_selected, month_selected] = frontend_gui().state_and_month_selection()

# Initializing the KNN Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
[y_predict, accuracy_score] = knn_algorithm(
    x_train, x_test, y_train, y_test).knn_predict()

[prediction, accuracy] = get_prediction_and_accuracy(
    y_predict, accuracy_score, state_selected, month_selected).display_result()
print(
    f"KNN Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")
print_to_file("K Nearest Neighbor", prediction, accuracy).print_output_file()

# Initializing the Logistic Regression Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
[y_predict, accuracy_score] = logistic_regression(
    x_train, x_test, y_train, y_test).lr_predict()
[prediction, accuracy] = get_prediction_and_accuracy(
    y_predict, accuracy_score, state_selected, month_selected).display_result()
print(
    f"Logistic Regression Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")
print_to_file("Logistic Regression", prediction, accuracy).print_output_file()

# Initializing the Support Vector Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
[y_predict, accuracy_score] = support_vector_algorithm(
    x_train, x_test, y_train, y_test).sv_predict()

[prediction, accuracy] = get_prediction_and_accuracy(
    y_predict, accuracy_score, state_selected, month_selected).display_result()
print(
    f"Support Vector Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")
print_to_file("Support Vector", prediction, accuracy).print_output_file()

# Initializing the Decision Tree Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
[y_predict, accuracy_score] = decision_tree(
    x_train, x_test, y_train, y_test).dt_predict()

[prediction, accuracy] = get_prediction_and_accuracy(
    y_predict, accuracy_score, state_selected, month_selected).display_result()
print(
    f"Decision Tree Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")
print_to_file("Decision Tree", prediction, accuracy).print_output_file()

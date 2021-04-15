from prepare_data import prepare_data
from prepare_model import prepare_model
from knn_algorithm import knn_algorithm
from frontend_gui import frontend_gui
from get_prediction_and_accuracy import get_prediction_and_accuracy
from logistic_regression import logistic_regression
from support_vector_algorithm import support_vector_algorithm
from decision_tree import decision_tree

# Initalizing the prepare data by passing the CSV data file and getting the x and y values by calling the function.
prepare_object = prepare_data('data/data_in_csv.csv')
[x, y] = prepare_object.prepare()

# Initalizing the model by passing the x and y values and getting the model by calling the prepare model function
model_object = prepare_model(x, y)
[x_train, x_test, y_train, y_test] = model_object.prepare_training_and_testing_data()

# Getting the state and month from the user
input_object = frontend_gui()
[state_selected, month_selected] = input_object.state_and_month_selection()


# Initializing the KNN Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
knn_object = knn_algorithm(x_train, x_test, y_train, y_test)
[y_predict, accuracy_score] = knn_object.knn_predict()

# Getting the prediction and accuracy by passing the y_predict value and getting the result
get_prediction_and_accuracy_object = get_prediction_and_accuracy(
    y_predict, accuracy_score, state_selected, month_selected)
[prediction, accuracy] = get_prediction_and_accuracy_object.display_result()
print(
    f"KNN Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")


# Initializing the Logistic Regression Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
lr_object = logistic_regression(x_train, x_test, y_train, y_test)
[y_predict, accuracy_score] = lr_object.lr_predict()

get_prediction_and_accuracy_object = get_prediction_and_accuracy(
    y_predict, accuracy_score, state_selected, month_selected)
[prediction, accuracy] = get_prediction_and_accuracy_object.display_result()
print(
    f"Logistic Regression Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")


# Initializing the Support Vector Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
support_vector_object = support_vector_algorithm(
    x_train, x_test, y_train, y_test)
[y_predict, accuracy_score] = support_vector_object.sv_predict()

get_prediction_and_accuracy_object = get_prediction_and_accuracy(
    y_predict, accuracy_score, state_selected, month_selected)
[prediction, accuracy] = get_prediction_and_accuracy_object.display_result()
print(
    f"Support Vector Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")


# Initializing the Decision Tree Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
decision_tree_object = decision_tree(x_train, x_test, y_train, y_test)
[y_predict, accuracy_score] = decision_tree_object.dt_predict()

get_prediction_and_accuracy_object = get_prediction_and_accuracy(
    y_predict, accuracy_score, state_selected, month_selected)
[prediction, accuracy] = get_prediction_and_accuracy_object.display_result()
print(
    f"Decision Algorithm: Prediction '{prediction}' with Accuracy of {accuracy}%")

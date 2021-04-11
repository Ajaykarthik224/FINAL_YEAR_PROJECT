from prepare_data import prepare_data
from prepare_model import prepare_model
from knn_algorithm import knn_algorithm

# Initalizing the prepare data by passing the CSV data file and getting the x and y values by calling the function.
prepare_object = prepare_data('data/data_in_csv.csv')
[x, y] = prepare_object.prepare()

# Initalizing the model by passing the x and y values and getting the model by calling the prepare model function
model_object = prepare_model(x, y)
[x_train, x_test, y_train, y_test] = model_object.prepare_training_and_testing_data()

# Initializing the KNN Algorithm by providing x_train, x_test, y_train, y_test and getting the predicted values.
knn_object = knn_algorithm(x_train, x_test, y_train, y_test)
print(knn_object.knn_predict())

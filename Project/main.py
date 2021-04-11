from prepare_data import prepare_data
from prepare_model import prepare_model


prepare_object = prepare_data('data/data_in_csv.csv')

[x, y] = prepare_object.prepare()

model_object = prepare_model(x, y)
model_object.prepare_training_and_testing_data()

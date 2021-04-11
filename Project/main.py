from prepare_data import prepare_data


data_handler.get_data_using_api()

prepare_object = prepare_data('data/data_in_csv.csv')

[x, y] = prepare_object.prepare()

print(x)

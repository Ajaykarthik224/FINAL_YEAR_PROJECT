from sklearn.model_selection import train_test_split
from sklearn import preprocessing


class prepare_model:

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def prepare_training_and_testing_data(self):
        minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
        # print(minmax.fit(x).transform(x))

        x_train, x_test, y_train, y_test = train_test_split(
            self.x, self.y, test_size=0.2)
        print("Training Data:\n", x_train)
        print("Testing Data:\n", x_test)
        y_train = y_train.astype('int')
        y_test = y_test.astype('int')

        return [x_train, x_test, y_train, y_test]

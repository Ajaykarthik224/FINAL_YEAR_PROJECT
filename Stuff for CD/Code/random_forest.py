from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import preprocessing


class random_forest:
    def __init__(self, x_train, x_test, y_train, y_test):
        super().__init__()
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def random_forest_predict(self):
        minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
        x_train_std = minmax.fit_transform(self.x_train)
        x_test_std = minmax.fit_transform(self.x_test)

        rmf = RandomForestClassifier(max_depth=3, random_state=0)
        rmf_clf = rmf.fit(self.x_train, self.y_train)
        rmf_clf_acc = cross_val_score(
            rmf_clf, x_train_std, self.y_train, cv=3, scoring="accuracy", n_jobs=-1)
        rmf_proba = cross_val_predict(
            rmf_clf, x_train_std, self.y_train, cv=3, method='predict_proba')

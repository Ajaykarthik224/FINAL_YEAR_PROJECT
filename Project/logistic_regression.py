from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, confusion_matrix
from sklearn import preprocessing


class logistic_regression:
    def __init__(self, x_train, x_test, y_train, y_test):
        super().__init__()
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def lr_predict(self):
        minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
        x_train_std = minmax.fit_transform(self.x_train)
        y_train_std = minmax.transform(self.x_test)

        lr = LogisticRegression()
        lr.fit(self.x_train, self.y_train)
        lr_acc = cross_val_score(lr, x_train_std, self.y_train,
                                 cv=3, scoring='accuracy', n_jobs=-1)
        lr_proba = cross_val_predict(
            lr, x_train_std, self.y_train, cv=3, method='predict_proba')
        y_pred = lr.predict(self.x_test)
        # print("Predicated value:", y_pred)

        # print("\nAccuracy score:%f" %
        #       (accuracy_score(self.y_test, y_pred)*100))
        # print("recall score:%f" % (recall_score(y_test, y_pred)*100))
        # print("roc score:%f" % (roc_auc_score(y_test, y_pred)*100))
        # print(confusion_matrix(y_test, y_pred))

        return [y_pred, accuracy_score(self.y_test, y_pred)*100]

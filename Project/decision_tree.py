from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import preprocessing


class decision_tree:
    def __init__(self, x_train, x_test, y_train, y_test):
        super().__init__()
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def dt_predict(self):
        minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
        x_train_std = minmax.fit_transform(self.x_train)
        x_test_std = minmax.fit_transform(self.x_test)

        dtc_clf = DecisionTreeClassifier()
        dtc_clf.fit(self.x_train, self.y_train)
        dtc_clf_acc = cross_val_score(
            dtc_clf, x_train_std, self.y_train, cv=3, scoring="accuracy", n_jobs=-1)

        # print("Predicted Values:")
        y_predict = dtc_clf.predict(self.x_test)

        # print("Actual Values:")
        # print(y_test.values)
        # print("\nAccuracy Score:%f" %
        #       (accuracy_score(self.y_test, y_predict)*100))
        # print("Recall Score:%f" %
        #       (recall_score(self.y_test, y_predict)*100))
        # print("ROC score:%f" % (roc_auc_score(self.y_test, y_predict)*100))
        # print(confusion_matrix(self.y_test, y_predict))

        return [y_predict, accuracy_score(self.y_test, y_predict)*100]

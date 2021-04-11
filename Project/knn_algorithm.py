from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import model_selection, neighbors
from sklearn import preprocessing


class knn_algorithm:

    def __init__(self, x_train, x_test, y_train, y_test):
        super().__init__()
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    # Using K Neighbors Algorithm to predict
    def knn_predict(self):
        minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
        clf = neighbors.KNeighborsClassifier()
        clf.fit(self.x_train, self.y_train)

        # print("Predicted Values for the Floods:")
        y_predict = clf.predict(self.x_test)
        # print(y_predict)

        x_train_std = minmax.fit_transform(self.x_train)
        x_test_std = minmax.fit_transform(self.x_test)
        knn_acc = cross_val_score(clf, x_train_std, self.y_train,
                                  cv=3, scoring='accuracy', n_jobs=-1)
        knn_proba = cross_val_predict(
            clf, x_train_std, self.y_train, cv=3, method='predict_proba')

        # print(knn_acc)
        # print("\nAccuracy Score:%f" %
        #       (accuracy_score(self.y_test, y_predict)*100))
        # print("Recall Score:%f" %
        #       (recall_score(self.y_test, y_predict)*100))
        # print("ROC score:%f" % (roc_auc_score(self.y_test, y_predict)*100))
        # print(confusion_matrix(self.y_test, self.y_predict))

        return [y_predict, accuracy_score(self.y_test, y_predict)*100]

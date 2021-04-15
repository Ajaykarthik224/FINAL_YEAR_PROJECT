from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, confusion_matrix


class support_vector_algorithm:

    def __init__(self, x_train, x_test, y_train, y_test):
        super().__init__()
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def sv_predict(self):
        minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
        x_train_std = minmax.fit_transform(self.x_train)
        y_train_std = minmax.transform(self.x_test)

        svc = SVC(kernel='rbf', probability=True)
        svc_classifier = svc.fit(self.x_train, self.y_train)
        svc_acc = cross_val_score(svc_classifier, x_train_std,
                                  self.y_train, cv=3, scoring="accuracy", n_jobs=-1)
        svc_proba = cross_val_predict(
            svc_classifier, x_train_std, self.y_train, cv=3, method='predict_proba')
        svc_scores = svc_proba[:, 1]
        y_predict = svc_classifier.predict(self.x_test)
        # print("Actual Flood Values:")
        # print(self.y_test.values)
        # print("Predicted Flood Values:")
        # print(y_pred)

        return [y_predict, accuracy_score(self.y_test, y_predict)*100]

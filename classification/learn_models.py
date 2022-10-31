import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

pd.options.mode.chained_assignment = None


def learn(clf, filename):
    train_data = pd.read_csv('../train.csv')

    x_train = train_data['name_1'].astype(str) + ' ' + train_data['name_2']
    y_train = train_data['is_duplicate']
    vectorizer = TfidfVectorizer(encoding='utf-8')

    x_train = vectorizer.fit_transform(x_train)

    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2)

    clf = clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    result1 = classification_report(y_test, y_pred)
    print("Полученные результаты классификации:", )
    print(result1)
    result2 = accuracy_score(y_test, y_pred)
    print("accuracy score:", )
    print(result2)

    with open(filename, 'wb') as f:
        pickle.dump(clf, f)


if __name__ == '__main__':
    print('Logic Regression results:')
    learn(LogisticRegression(), 'logic_regression')

    print('Decision Tree results:')
    learn(DecisionTreeClassifier(), 'decision_tree')

    print('Random Forest results:')
    learn(RandomForestClassifier(), 'random_forest')

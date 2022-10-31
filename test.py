import pickle
import itertools


if __name__ == '__main__':
    with open('./classification/learned models/random_forest', 'rb') as f:
        clf = pickle.load(f)

    with open('./classification/vectorizer.pk', 'rb') as f:
        vectorizer = pickle.load(f)

    with open('demo_names.txt', 'r') as f:
        companies = f.read().splitlines()
    print(companies)

    pairs = list(itertools.combinations(companies, 2))

    preds = []
    for pair in pairs:
       item = vectorizer.fit_transform([pair[0] + ' ' + pair[1]])
       prediction = clf.predict(item)

       preds.append([pair[0], pair[1], prediction])

    print(preds)

import re

import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from pymorphy2 import MorphAnalyzer
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV

# nltk.download('popular')

df_claster = pd.read_csv('../../Users/konon/Downloads/CompClust-master/CompClust-master/train.csv')
df_train = df_claster.loc[df_claster['is_duplicate'] == 0]
df_test = df_claster.loc[df_claster['is_duplicate'] > 0]

bad_words = "[0-9!#$%&'()*+,./:;<=>?@[\]^_{|}~\"\-]+"
morph = MorphAnalyzer()


def token_only(text):
    text = re.sub(bad_words, ' ', text)
    tokens = [word.lower() for sent in sent_tokenize(text) for word in word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        token = token.strip()
        token = morph.normal_forms(token)[0]
        filtered_tokens.append(token)
    return filtered_tokens


df_name1 = df_train['name_1']
df_name2 = df_train['name_2']

df_name1_test = df_test['name_1']
df_name2_test = df_test['name_2']

tfidf_vectorizer = TfidfVectorizer(smooth_idf=True, max_df=0.6, min_df=0.01, max_features=100000,
                                   use_idf=True, tokenizer=token_only, ngram_range=(1, 3))
tfidf_matrix_1 = tfidf_vectorizer.fit_transform(df_name1)
tfidf_matrix_2 = tfidf_vectorizer.transform(df_name2)

mbk = MiniBatchKMeans()
parameters = {'init': ('k-means++', 'random'), 'n_clusters': [2, 3, 4], 'max_iter': [50, 100, 200, 300]}
clf = GridSearchCV(mbk, parameters)
clf.fit(tfidf_matrix_1)

# предикт для обучения
y_kmeansMBK = clf.predict(tfidf_matrix_1)
num_1 = [int(pt) for pt in y_kmeansMBK]
df_train['num_cluster_1'] = num_1

y_kmeansMBK = clf.predict(tfidf_matrix_2)
num_2 = [int(pt) for pt in y_kmeansMBK]
df_train['num_cluster_2'] = num_2

df_train.to_csv('claster.csv', index=False)

# предикт для теста
tfidf_matrix_3 = tfidf_vectorizer.transform(df_name1_test)
tfidf_matrix_4 = tfidf_vectorizer.transform(df_name2_test)

y_kmeansMBK = clf.predict(tfidf_matrix_3)
num_1 = [int(pt) for pt in y_kmeansMBK]
df_test['num_cluster_1'] = num_1
y_kmeansMBK = clf.predict(tfidf_matrix_4)
num_2 = [int(pt) for pt in y_kmeansMBK]
df_test['num_cluster_2'] = num_2

df_test.to_csv('claster_test.csv', index=False)

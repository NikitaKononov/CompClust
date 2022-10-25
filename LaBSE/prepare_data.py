import pandas as pd
from scipy.spatial.distance import cosine, euclidean
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

if __name__ == '__main__':
    data = pd.read_csv('../train.csv', index_col='pair_id')
    data_numpy = data.to_numpy()

    model = SentenceTransformer('sentence-transformers/LaBSE')

    data_arr = []
    for item in tqdm(data_numpy):
        embeddings = model.encode([item[0], item[1]])
        data_arr.append([item[0], item[1], embeddings[0], embeddings[1], cosine(embeddings[0], embeddings[1]),
                         euclidean(embeddings[0], embeddings[1]), item[2]])

    result = pd.DataFrame(data=data_arr,
                          columns=['name_1', 'name_2', 'labse_1', 'labse_2', 'cosine', 'euclidean', 'is_duplicate'])

    result.to_csv('full_labse.csv')

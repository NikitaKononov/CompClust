import pandas as pd

df = pd.read_csv('claster_test.csv')

print(df.shape)
df['is_duplicate_pred'] = 0 * df['pair_id'].shape[0]

for first, second, index in zip(df['num_cluster_1'], df['num_cluster_2'], range(df['pair_id'].shape[0])):
    if first == second:
        df['is_duplicate_pred'][index] = 1

df.to_csv('ans.csv', index=False)

print('Точность ---->  ', sum(df['is_duplicate_pred']) / (df['is_duplicate_pred']).shape[0])

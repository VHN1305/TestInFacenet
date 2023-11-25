import pandas as pd

data = pd.read_csv('data\pizza_error_list_with_label.csv')

# Split data

full_train = data.sample(frac=0.8, random_state=42)
full_test = data.drop(full_train.index)

full_train.to_csv('data\pizza_train.csv', index=False)
full_test.to_csv('data\pizza_test.csv', index=False)


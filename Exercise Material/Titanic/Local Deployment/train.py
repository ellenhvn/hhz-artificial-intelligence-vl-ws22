"""
Quick model training for Titanic for the local deployment example

Loosely based on https://github.com/amirziai/sklearnflask

"""

import os
import time

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rf

# inputs
training_data = str(os.getcwd()) + '/data/titanic.csv'
include = ['Age', 'Sex', 'Embarked', 'Survived']
dependent_variable = include[-1]

model_directory = str(os.getcwd()) + '/model'
model_file_name = '%s/model.pkl' % model_directory
model_columns_file_name = '%s/model_columns.pkl' % model_directory



def train():
    df = pd.read_csv(training_data)
    df_ = df[include]

    categoricals = [] 

    for col, col_type in df_.dtypes.items():
        if col_type == 'O':
            categoricals.append(col)
        else:
            df_[col].fillna(df[col].mean(), inplace=True)  # fill NA's with mean imputation

    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    y = df_ohe[dependent_variable]

    model_columns = list(x.columns)
    joblib.dump(model_columns, model_columns_file_name)

    clf = rf()
    start = time.time()
    clf.fit(x, y)

    joblib.dump(clf, model_file_name)

    message1 = 'Trained in %.5f seconds' % (time.time() - start)
    message2 = 'Model training score: %s' % clf.score(x, y)
    print('Success. \n{0}. \n{1}.'.format(message1, message2))


if __name__ == '__main__':
    train()

import pandas as pd
import torch
import numpy as np

def open_and_prepare_df(ds):

    path = 'datasets/'
    if ds == 'eval':
        df = pd.read_excel(io=f'{path}NLP_PILOT.xlsx')

    elif ds == 'main':
        df = pd.read_excel(io=f'{path}NLP_CLEAN.xlsx')
        df = df[df['time'] > 300]
        df = df[df['label'] != 1]

    elif ds == 'features':
        df = pd.read_excel(io=f'{path}NLP_FEATURES.xlsx')

    for item in [f'nlp_{i}' for i in range(2, 6)]:
        df = df[df[item].apply(lambda x: len(x) > 10)]

    return df

def set_device():
    print(f'Cuda available: {torch.cuda.is_available()}')
    return "cuda:0" if torch.cuda.is_available() else "cpu"
    

def X_y_split(df, X_string):
    
    X = []
    X_raw = df[X_string].values
    for item in X_raw:
        X.append(eval(item))

    X = np.asarray(X)
    y = df['label'].values

    return X, y

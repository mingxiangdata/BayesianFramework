import pandas as pd
import bayesframe

def load_data():
    path = '/'.join(bayesframe.__path__[0].split('/')[:-1]) + '/data/data.csv'
    return pd.read_csv(path)

def load_test_data():
    path = '/'.join(bayesframe.__path__[0].split('/')[:-1]) + '/data/data_test.csv'
    return pd.read_csv(path)


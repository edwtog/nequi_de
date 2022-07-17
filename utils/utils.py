import logging
import pandas as pd

def describe_all(df):
    a = df.describe(include='all').T
    a_null = pd.DataFrame(df.isnull().sum())
    a_null.columns = ['missing']
    types_df = pd.DataFrame(df.dtypes)
    types_df.columns = ['DataType']
    summary_df = a.join(a_null).join(types_df)
    return summary_df
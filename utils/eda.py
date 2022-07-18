import os
import pandas as pd
from pandas_profiling import ProfileReport

from utils.definitions import ROOT_DIR

def describe_all(df):
    a = df.describe(include='all').T
    a_null = pd.DataFrame(df.isnull().sum())
    a_null.columns = ['missing']
    types_df = pd.DataFrame(df.dtypes)
    types_df.columns = ['DataType']
    summary_df = a.join(a_null).join(types_df)
    return summary_df

def profiling_df(df, name, report_html=False):
    rel_path = "profiling_reports/{}.{}".format(name, 'csv')
    summary = describe_all(df)
    summary.to_csv(os.path.join(ROOT_DIR, rel_path))
    if report_html:
        profile = ProfileReport(df.sample(round(len(df)/100)),
                                title="Pandas Profiling Report", html={'style':{'full_width':True}})
        profile.to_file(os.path.join(ROOT_DIR, rel_path))

import os
import logging
import pandas as pd

from utils.definitions import ROOT_DIR
from utils.eda import profiling_df
from src.load_datasets_S3 import upload_parquet

def trf_csv(data_source, file_name):
    try:
        rel_path = "data/raw/{}/{}".format(data_source, file_name)
        abs_file_path = os.path.join(ROOT_DIR, rel_path)
        loan_df = pd.read_csv(abs_file_path)
        profiling_df(loan_df, name='credit-risk raw loan')

        loan_reduce_df = loan_df[["id", "loan_amnt", "term", "int_rate", "grade", "home_ownership", "loan_status", "purpose"]]
        profiling_df(loan_df, name='credit-risk processed loan')

        rel_path_loan = "data/processed/{}/loan_reduce_df.parquet.gzip".format(data_source)
        loan_reduce_df.to_parquet(os.path.join(ROOT_DIR, rel_path_loan),
                             engine='pyarrow', compression='gzip')
        
        upload_parquet(parquet_name='loan_reduce_df.parquet.gzip',
                data_source=data_source,
                zone='processed')

    except:
        logging.info('parquet failed !!!')
        return False
    return True
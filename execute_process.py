import logging
import os
import time
import pandas as pd
import src.infra as infra
from src.load_data import load_datasets
from src.load_datasets_S3 import upload_datasets

from utils.definitions import ROOT_DIR


if __name__ == '__main__':

    file_date = time.strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(filename='logs/'+file_date+'.log', level=logging.INFO)
    
    logging.info('Started infra creation')
    infra.create_infra()
    logging.info('Finished infra creation')

    logging.info('Loading datasets')
    if load_datasets():
        logging.info('datasets loaded')

    logging.info('Uploading datasets to S3')
    if upload_datasets():
        logging.info('datasets loaded to S3')

    rel_path = "data/raw/credit-risk/loan/loan.csv"
    abs_file_path = os.path.join(ROOT_DIR, rel_path)
    data = pd.read_csv(abs_file_path)
    print(data.shape)

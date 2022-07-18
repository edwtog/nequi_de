import logging
import os
import time
import json
import pandas as pd
import src.infra as infra
from src.load_data import load_datasets
from src.load_datasets_S3 import upload_datasets
from src.transform_credit_risk import trf_csv as trf_csv_credit_risk
from src.transform_electric_motor_temperature import trf_csv as trf_csv_electric_motor_temp
from src.transform_json_cite_sum import trf_json

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
    
    # json files
    if trf_json():
        logging.info('cite-sum json to parquet')

    # csv files
    if trf_csv_credit_risk(data_source='credit-risk', file_name='loan/loan.csv'):
        logging.info('credit-risk csv to parquet')

    if trf_csv_electric_motor_temp(data_source='electric-motor-temperature', file_name='measures_v2.csv'):
        logging.info('electric-motor-temperatue csv to parquet')
    
    logging.info('Process finished')
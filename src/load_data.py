import logging
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

def load_datasets():
    try:
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files("wkirgsn/electric-motor-temperature", "data/raw/electric-motor-temperature/", unzip=True)
        api.dataset_download_files("ranadeep/credit-risk-dataset", "data/raw/credit-risk/", unzip=True)
        api.dataset_download_files("nbroad/cite-sum", "data/raw/cite-sum/", unzip=True)
    except:
        logging.info('Datasets cant be loaded')
        return False
    return True






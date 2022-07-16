import logging
from kaggle.api.kaggle_api_extended import KaggleApi

#kaggle datasets download -d wkirgsn/electric-motor-temperature

def load_datsets():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files("wkirgsn/electric-motor-temperature", "data/raw/electric-motor-temperature/", unzip=True)
    api.dataset_download_files("ranadeep/credit-risk-dataset", "data/raw/credit-risk/", unzip=True)
    api.dataset_download_files("nbroad/cite-sum", "data/raw/cite-sum/", unzip=True)
    logging.info('Datsets_loaded')

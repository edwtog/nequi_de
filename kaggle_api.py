import logging
import os
import infra
import time
#os.environ['KAGGLE_USERNAME'] = "<your-kaggle-username>"
#os.environ['KAGGLE_KEY'] = "<your-kaggle-api-key>"
from kaggle.api.kaggle_api_extended import KaggleApi

def main():
    file_date = time.strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(filename='log_files/'+file_date+'.log', level=logging.INFO)
    logging.info('Started infra creation')
    infra.create_infra()
    logging.info('Finished infra creation')

    #kaggle datasets download -d wkirgsn/electric-motor-temperature
    dataset_1 = "wkirgsn/electric-motor-temperature"
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files("wkirgsn/electric-motor-temperature", "data/raw/electric-motor-temperature/", unzip=True)
    api.dataset_download_files("ranadeep/credit-risk-dataset", "data/raw/credit-risk/", unzip=True)
    # kaggle datasets download -d harshithgupta/youtubes-channels-dataset

if __name__ == '__main__':
    main()
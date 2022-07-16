import os
#os.environ['KAGGLE_USERNAME'] = "<your-kaggle-username>"
#os.environ['KAGGLE_KEY'] = "<your-kaggle-api-key>"

from kaggle.api.kaggle_api_extended import KaggleApi

#kaggle datasets download -d wkirgsn/electric-motor-temperature
dataset_1 = "wkirgsn/electric-motor-temperature"
api = KaggleApi()
api.authenticate()
api.dataset_download_files("wkirgsn/electric-motor-temperature", "data/raw/electric-motor-temperature/", unzip=True)
api.dataset_download_files("ranadeep/credit-risk-dataset", "data/raw/credit-risk/", unzip=True)


print("Done !!")
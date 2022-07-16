import os
os.environ['KAGGLE_USERNAME'] = "<your-kaggle-username>"
os.environ['KAGGLE_KEY'] = "<your-kaggle-api-key>"

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

print("Done!!")
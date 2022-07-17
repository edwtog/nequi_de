import logging
import pandas as pd
import boto3
from botocore.exceptions import ClientError
import os
from datetime import datetime
from utils.definitions import ROOT_DIR

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_datasets():

    now = datetime.now() # current date and time

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    try:
        rel_path = "data/raw/credit-risk/loan/loan.csv"
        abs_file_path = os.path.join(ROOT_DIR, rel_path)
        upload_file(abs_file_path, bucket="prueba-nequi",
                    object_name="raw/credit-risk/{}/{}/{}/loan.csv".format(year, month, day))

        rel_path = "data/raw/electric-motor-temperature/measures_v2.csv"
        abs_file_path = os.path.join(ROOT_DIR, rel_path)
        upload_file(abs_file_path, bucket="prueba-nequi",
                    object_name="raw/electric-motor-temperature/{}/{}/{}/measures_v2.csv".format(year, month, day))

        rel_path = "data/raw/cite-sum/train.json"
        abs_file_path = os.path.join(ROOT_DIR, rel_path)
        upload_file(abs_file_path, bucket="prueba-nequi",
                    object_name="raw/cite-sim/{}/{}/{}/data.json".format(year, month, day))                   
    except:
        logging.INFO('Datasets cant be uploaded to S3')
        return False
    return True

if __name__ == '__main__':

    #upload_datasets()
    rel_path = "data/raw/credit-risk/loan/loan.csv"
    abs_file_path = os.path.join(os.path.dirname(__file__), rel_path)
    data = pd.read_csv(abs_file_path)

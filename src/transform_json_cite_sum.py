import os
import json
import logging
import pandas as pd

from utils.definitions import ROOT_DIR
from utils.eda import profiling_df
from src.load_datasets_S3 import upload_parquet

def trf_json():
    try:
        rel_path = "data/raw/cite-sum/train.json"
        abs_file_path = os.path.join(ROOT_DIR, rel_path)

        data_info = [json.loads(x) for x in open(abs_file_path)]
        discipline_info = []
        papers_info = []

        for item in data_info:
            if item is not None:
                if item['discipline'] is not None:
                    discipline = item['discipline']
                else:
                    discipline = {'venue':'not specified', 'journal':'not specified',
                                  'mag_field_of_study':['not specified']}
                discipline['paper_id'] = item['paper_id']
                discipline_info.append(discipline)
                item.pop('discipline')
                papers_info.append(item)
            
        papers_df = pd.DataFrame(papers_info)
        discipline_df = pd.DataFrame(discipline_info)
        profiling_df(papers_df, name='cite-sum papers')
        profiling_df(discipline_df, name='cite-sum discipline')

        rel_path_papers = "data/processed/cite-sum/papers_df.parquet.gzip"
        rel_path_discipline = "data/processed/cite-sum/discipline_df.parquet.gzip"
        papers_df.to_parquet(os.path.join(ROOT_DIR, rel_path_papers),
                             engine='pyarrow', compression='gzip')
        discipline_df.to_parquet(os.path.join(ROOT_DIR, rel_path_discipline),
                             engine='pyarrow', compression='gzip')

        upload_parquet(parquet_name='papers_df.parquet.gzip',
                       data_source='cite-sum',
                       zone='processed')

        upload_parquet(parquet_name='discipline_df.parquet.gzip',
                       data_source='cite-sum',
                       zone='processed')

    except:
        logging.info('parquet failed !!!')
        return False
    return True
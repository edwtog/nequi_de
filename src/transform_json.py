import os
import json
import logging

from utils.definitions import ROOT_DIR


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
                    discipline = {'venue':'not specified', 'journal':'not specified', 'mag_field_of_study':'not specified'}
                discipline['paper_id'] = item['paper_id']
                discipline_info.append(discipline)
                item.pop('discipline')
                papers_info.append(item)
            
        print(len(discipline_info))
        print(len(papers_info))
    except:
        logging.INFO('Failed !!!')
        return False
    return True
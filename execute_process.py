import logging
import os
import infra
import time
import src.load_data as load_data
#os.environ['KAGGLE_USERNAME'] = "<your-kaggle-username>"
#os.environ['KAGGLE_KEY'] = "<your-kaggle-api-key>"


def main():
    file_date = time.strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(filename='logs/'+file_date+'.log', level=logging.INFO)
    logging.info('Started infra creation')
    infra.create_infra()
    logging.info('Finished infra creation')

    load_data.load_datsets()

if __name__ == '__main__':
    main()
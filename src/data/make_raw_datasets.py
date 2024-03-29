# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from joinning_raw_datasets import MakeRawDataset
import os

@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    datasets = MakeRawDataset()
    df_train = datasets.create_dataframe()
    df_test = datasets.create_dataframe(mode='test')

    df_train.to_csv(os.path.join(output_filepath,'train_data.csv'),index=False)
    df_test.to_csv(os.path.join(output_filepath,'test_data.csv'),index=False)

    print('Raw datasets created with success')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables

    main()

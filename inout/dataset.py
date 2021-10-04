import logging
from configparser import ConfigParser
from os import listdir
from os.path import isfile, join

class DatasetIO:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.config = ConfigParser()
        self.config.read('conf/app.conf')

    def read_input(self):
        self.logger.info("Start read dataset")
        dataset_path = self.config.get('DATASET','dataset_path')

        onlyfiles = [f for f in listdir(dataset_path) if isfile(join(dataset_path, f))]

        self.logger.info(onlyfiles)



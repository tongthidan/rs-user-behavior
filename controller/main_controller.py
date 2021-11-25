import logging

from inout.dataset import DatasetIO
from training.trainingdata import Trainner


class MainController:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.run()

    def run(self):
        # read data set
        dataset_io = DatasetIO()
        dataset_io.read_input()
        # train = Trainner()
        # train.convert_rating_to_user_item()


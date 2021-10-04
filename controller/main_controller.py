import logging

from inout.dataset import DatasetIO


class MainController:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.run()

    def run(self):
        # read data set
        dataset_io = DatasetIO()
        dataset_io.read_input()

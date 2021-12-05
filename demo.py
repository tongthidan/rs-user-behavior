import logging
import logging.config
import os

from common.constants import Constants
from controller.main_controller import MainController
from training.Spliter import Spliter
from training.trainingdata import Trainner


def conf_log():
    log_filename = "logs/rs.log"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)

    logging.config.fileConfig('conf/logging.conf')
    logging.root.setLevel(logging.NOTSET)


if __name__ == '__main__':
    conf_log()
    # split dataset
    split = Spliter()
    # split.get_data_train_test()
    split.split_data_context()
    # train = Trainner()
    # manh1
    # train.spilit_data_rating(Constants.DATASET_MANH1, 282, 218, Constants.DATASET_MATRIX_TRAIN_manh1)

    # train.convert_rating_to_user_item(Constants.DATASET_MANH1, Constants.DATASET_MATRIX_TRAIN_manh1)
    # # train.fill_zero()
    # train.calculate_similar_user_user(Constants.DATASET_MATRIX_TRAIN_manh1,Constants.DATASET_USER_SIMILAR_manh1)
    # train.calculate_similar_item_item(Constants.DATASET_MATRIX_TRAIN_manh1,Constants.DATASET_ITEM_SIMILAR_manh1)

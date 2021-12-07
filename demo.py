import logging
import logging.config
import os

from common.constants import Constants
from controller.main_controller import MainController
from training.Spliter import Spliter
from training.Training import Trainner


def conf_log():
    log_filename = "logs/rs.log"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    logging.config.fileConfig('conf/logging.conf')
    logging.root.setLevel(logging.NOTSET)


if __name__ == '__main__':
    conf_log()
    # split dataset
    # split = Spliter()
    # split.get_data_train_test()
    # split.split_data_context()
    train = Trainner()
    train.convert_rating_to_user_item("train_dataset_0_0_0.csv")
    # for filename in os.listdir(Constants.TRAINING_SUB_DATASETS_DIRECTORY):
    #     logging.info("Convert file name " + filename)
    #     train.convert_rating_to_user_item(filename)
    # print("Calculate done  !!! ")
    # for filename in os.listdir(Constants.USER_ITEM_DATASETS_DIRECTORY):
    #     logging.info("Calculate item-item-similar  with file " + filename)
    #     # train.calculate_similar_item_item(filename)
    #     train.calculate_similar_user_user(filename)
    # print("Calculate all done  !!! ")

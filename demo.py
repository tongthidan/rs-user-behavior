import logging
import logging.config
import os

from common.constants import Constants
from controller.main_controller import MainController
from training.Recommender import Recommender
from training.Spliter import Spliter
from training.Testing import Testing
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
    # train = Trainner()
    # convert to matrix
    # for filename in os.listdir(Constants.TRAINING_SUB_DATASETS_DIRECTORY):
    #     logging.info("Convert file name " + filename)
    #     train.convert_rating_to_user_item(filename)
    # print("Calculate done  !!! ")

    # calculate similar
    # for filename in os.listdir(Constants.USER_ITEM_DATASETS_DIRECTORY):
    #     logging.info("Calculate item-item-similar  with file " + filename)
    #     train.calculate_similar_item_item(filename)
    #     train.calculate_similar_user_user(filename)
    # print("Calculate all done  !!! ")

    # predict- recomendation
    # recommender = Recommender()
    # recommender.result_context_predict("_0_0_0")
    # recommender.result_context_predict("_0_0_1")
    # recommender.result_context_predict("_0_1_0")
    # recommender.result_context_predict("_0_1_1")
    # recommender.result_context_predict("_1_0_0")
    # recommender.result_context_predict("_1_0_1")
    # recommender.result_context_predict("_1_1_0")
    # recommender.result_context_predict("_1_1_1")
    # print("Calculate result predict done !!! ")

    # testing
    test = Testing()
    test.test_pre_filtering("_1_1_1")

from enum import Enum


class Constants:
    PRODUCT_DATASETS_DIRECTORY = "data\\data_product\\"
    TRAINING_DATASETS_DIRECTORY = "data\\data_train\\"
    DATASET_RATING = PRODUCT_DATASETS_DIRECTORY + "behavior-rating.csv"
    TRAINING_SUB_DATASETS_DIRECTORY = "data\\sub_data\\training\\"
    TESTING_SUB_DATASETS_DIRECTORY = "data\\sub_data\\testing\\"
    USER_ITEM_DATASETS_DIRECTORY = "data\\data_cf\\cosin\\"
    USER_ITEM_DATASETS_NORMAL_DIRECTORY = "data\\data_cf\\normal\\"
    USER_SIMILAR_DATASETS_DIRECTORY = "data\\data_similar\\user_similar\\"
    ITEM_SIMILAR_DATASETS_DIRECTORY = "data\\data_similar\\item_similar\\"


class ValueContext:
    name = str()
    value = str()


class Measure(Enum):
    COSINE = 1
    PEARSON = 2


class Filter(Enum):
    USER_BASE = 1
    ITEM_BASE = 2

    # DATASETS_DIRECTORY_OUT_TRAIN = "data\\OUT_TRAIN\\"
    # raw
    # DATASET_USER = DATASETS_DIRECTORY_INPUT + "tbluser.csv"
    # DATASET_HOTEL = DATASETS_DIRECTORY_INPUT + "tblhotel.csv"
    # DATASET_RATING = DATASETS_DIRECTORY_INPUT + "tblrate.csv"
    # DATASET_MANH1 = DATASETS_DIRECTORY_INPUT + "manh1.csv"
    # DATASET_MANH2 = DATASETS_DIRECTORY_INPUT + "manh2.csv"
    # DATASET_MANH3 = DATASETS_DIRECTORY_INPUT + "manh3.csv"
    # DATASET_MANH4 = DATASETS_DIRECTORY_INPUT + "manh4.csv"
    # DATASET_MANH5 = DATASETS_DIRECTORY_INPUT + "manh5.csv"
    # DATASET_MANH6 = DATASETS_DIRECTORY_INPUT + "manh6.csv"
    # DATASET_MANH7 = DATASETS_DIRECTORY_INPUT + "manh7.csv"
    # DATASET_MANH8 = DATASETS_DIRECTORY_INPUT + "manh8.csv"
    # # slipit
    # DATASET_TRAIN_MANH1 = DATASETS_DIRECTORY_IN_TRAIN + "manh1.csv"
    # DATASET_TRAIN_MANH2 = DATASETS_DIRECTORY_IN_TRAIN + "manh2.csv"
    # DATASET_TRAIN_MANH3 = DATASETS_DIRECTORY_IN_TRAIN + "manh3.csv"
    # DATASET_TRAIN_MANH4 = DATASETS_DIRECTORY_IN_TRAIN + "manh4.csv"
    # DATASET_TRAIN_MANH5 = DATASETS_DIRECTORY_IN_TRAIN + "manh5.csv"
    # DATASET_TRAIN_MANH6 = DATASETS_DIRECTORY_IN_TRAIN + "manh6.csv"
    # DATASET_TRAIN_MANH7 = DATASETS_DIRECTORY_IN_TRAIN + "manh7.csv"
    # DATASET_TRAIN_MANH8 = DATASETS_DIRECTORY_IN_TRAIN + "manh8.csv"
    # # parse ma tran
    # DATASET_MATRIX_TRAIN_manh1 = DATASETS_DIRECTORY_IN_TRAIN + "user-hotel-manh1.csv"
    # DATASET_MATRIX_TRAIN_manh2 = DATASETS_DIRECTORY_IN_TRAIN + "user-hotel-manh2.csv"
    # DATASET_MATRIX_TRAIN_manh3 = DATASETS_DIRECTORY_IN_TRAIN + "user-hotel-manh3.csv"
    # DATASET_MATRIX_TRAIN_manh4 = DATASETS_DIRECTORY_IN_TRAIN + "user-hotel-manh4.csv"
    # DATASET_MATRIX_TRAIN_manh5 = DATASETS_DIRECTORY_IN_TRAIN + "user-hotel-manh5.csv"
    # DATASET_MATRIX_TRAIN_manh6 = DATASETS_DIRECTORY_IN_TRAIN + "user-hotel-manh6.csv"
    # DATASET_MATRIX_TRAIN_manh7 = DATASETS_DIRECTORY_IN_TRAIN + "user-hotel-manh7.csv"
    # DATASET_MATRIX_TRAIN_manh8 = DATASETS_DIRECTORY_IN_TRAIN + "user-hotel-manh8.csv"
    # # item-similar
    # DATASET_ITEM_SIMILAR_manh1 = DATASETS_DIRECTORY_OUT_TRAIN + "item-item-similar-manh1.csv"
    # DATASET_ITEM_SIMILAR_manh2 = DATASETS_DIRECTORY_OUT_TRAIN + "item-item-similar-manh2.csv"
    # DATASET_ITEM_SIMILAR_manh3 = DATASETS_DIRECTORY_OUT_TRAIN + "item-item-similar-manh3.csv"
    # DATASET_ITEM_SIMILAR_manh4 = DATASETS_DIRECTORY_OUT_TRAIN + "item-item-similar-manh4.csv"
    # DATASET_ITEM_SIMILAR_manh5 = DATASETS_DIRECTORY_OUT_TRAIN + "item-item-similar-manh5.csv"
    # DATASET_ITEM_SIMILAR_manh6 = DATASETS_DIRECTORY_OUT_TRAIN + "item-item-similar-manh6.csv"
    # DATASET_ITEM_SIMILAR_manh7 = DATASETS_DIRECTORY_OUT_TRAIN + "item-item-similar-manh7.csv"
    # DATASET_ITEM_SIMILAR_manh8 = DATASETS_DIRECTORY_OUT_TRAIN + "item-item-similar-manh8.csv"
    # # user-similar
    # DATASET_USER_SIMILAR_manh1 = DATASETS_DIRECTORY_OUT_TRAIN + "user-user-similar-manh1.csv"
    # DATASET_USER_SIMILAR_manh2 = DATASETS_DIRECTORY_OUT_TRAIN + "user-user-similar-manh2.csv"
    # DATASET_USER_SIMILAR_manh3 = DATASETS_DIRECTORY_OUT_TRAIN + "user-user-similar-manh3.csv"
    # DATASET_USER_SIMILAR_manh4 = DATASETS_DIRECTORY_OUT_TRAIN + "user-user-similar-manh4.csv"
    # DATASET_USER_SIMILAR_manh5 = DATASETS_DIRECTORY_OUT_TRAIN + "user-user-similar-manh5.csv"
    # DATASET_USER_SIMILAR_manh6 = DATASETS_DIRECTORY_OUT_TRAIN + "user-user-similar-manh6.csv"
    # DATASET_USER_SIMILAR_manh7 = DATASETS_DIRECTORY_OUT_TRAIN + "user-user-similar-manh7.csv"
    # DATASET_USER_SIMILAR_manh8 = DATASETS_DIRECTORY_OUT_TRAIN + "user-user-similar-manh8.csv"

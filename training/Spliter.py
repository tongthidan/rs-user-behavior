import logging
from builtins import print

import pandas as pd
from numpy.distutils.command.install_data import install_data

from common.constants import Constants


class Spliter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_data_train_test(self):
        path = Constants.DATASET_RATING
        data = pd.read_csv(path)

        data_train = pd.DataFrame(columns=data.columns)
        data_test = pd.DataFrame(columns=data.columns)

        userIds = data.user_id.unique()

        for i in range(0, len(userIds)):
            rating_by_user = data.loc[data['user_id'] == int(userIds[i])]

            num_collect = int(len(rating_by_user) * 80 / 100) + 1

            if num_collect == len(rating_by_user):
                num_collect -= 1

            train_records = rating_by_user.loc[rating_by_user['user_id'] == userIds[i]].iloc[:num_collect, :]
            test_records = rating_by_user.loc[rating_by_user['user_id'] == userIds[i]].iloc[num_collect:, :]

            data_train = data_train.append(train_records)
            data_test = data_test.append(test_records)

            print("Progress " + str((i + 1) * 100 / len(userIds)))

        data_train.to_csv(Constants.TRAINING_DATASETS_DIRECTORY + "behavior_rating_official_training.csv", index=False)
        data_test.to_csv(Constants.TRAINING_DATASETS_DIRECTORY + "behavior_rating_official_testing.csv", index=False)

        # print(data_train)

    def split_data_context(self):
        # data = pd.read_csv(Constants.TRAINING_DATASETS_DIRECTORY + "behavior_rating_official_testing.csv")
        data = pd.read_csv(Constants.TRAINING_DATASETS_DIRECTORY + "behavior_rating_official_training.csv")

        like = [0, 1]
        comment = [0, 1]
        post = [0, 1]
        a = len(like)
        b = len(comment)
        c = len(post)
        for i in like:
            for j in comment:
                for k in post:
                    in1 = like[i]
                    in2 = comment[j]
                    in3 = post[k]

                    filename = "dataset_" + str(in1) + "_" + str(in2) + "_" + str(in3)
                    print("CHECK" + str(in1) + "_" + str(in2) + "_" + str(in3))
                    data_filter = data.loc[(data['is_like'] == in1)
                                           & (data['is_comment'] == in2) & (data['is_post'] == in3)]

                    print(data_filter)
                    data_filter.to_csv(Constants.TRAINING_SUB_DATASETS_DIRECTORY + "train_" + filename + ".csv",
                                       index=False)
                    # data_filter.to_csv(Constants.TESTING_SUB_DATASETS_DIRECTORY + "test_" + filename + ".csv",
                    #                    index=False)

        print("Complete !!")

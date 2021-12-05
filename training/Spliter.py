import logging

import pandas as pd

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
        data = pd.read_csv(Constants.TRAINING_DATASETS_DIRECTORY + "behavior_rating_official_testing.csv")
        # data = pd.read_csv(Constants.TRAINING_DATASETS_DIRECTORY + "behavior_rating_official_training.csv")

        like = ['0', '1', '']
        comment = ['0', '1', '']
        post = ['0', '1', '']

        for i in range(0, len(like)):
            for j in range(0, len(comment)):
                for k in range(0, len(post)):
                    filename = "dataset_"
                    drop_columns = []

                    if like[i] != '':
                        filename += like[i].lower() + "_"
                        condition_like = data['is_like'] == like[i]
                        drop_columns.append('is_like')
                    else:
                        condition_like = True

                    if comment[j] != '':
                        filename += comment[j].lower() + "_"
                        condition_comment = data['is_comment'] == comment[j]
                        drop_columns.append('is_comment')
                    else:
                        condition_comment = True

                    if post[k] != '':
                        filename += post[k].lower() + "_"
                        condition_post = data['is_post'] == post[k]
                        drop_columns.append('is_post')
                    else:
                        condition_post = True

                    if filename[len(filename) - 1] == '_':
                        filename = filename[:len(filename) - 1]

                    full_condition = condition_like & condition_comment & condition_post

                    if (condition_like is True) & (condition_comment is True) & (condition_post is True):
                        data_filtered = data
                    else:
                        data_filtered = data[full_condition]

                    data_filtered = data_filtered.drop(drop_columns, 1)
                    # data_filtered.to_csv(Constants.TRAINING_SUB_DATASETS_DIRECTORY + "train_" + filename + ".csv",
                    #                      index=False)

                    data_filtered.to_csv(Constants.TESTING_SUB_DATASETS_DIRECTORY + "test_" + filename + ".csv",
                                         index=False)

        print("Complete !!")

import logging
import math

import numpy as np
import pandas as pd

from common.constants import Constants

from sklearn.metrics.pairwise import cosine_similarity


class Trainner:
    def __init__(self):
        self

    def spilit_data_rating(self, path_file_in, user_count, hotel_count, path_file_out):
        print(path_file_in)
        ratings = pd.read_csv(path_file_in)

        users = ratings.loc[0:, 'user_id'].unique()
        items = ratings.loc[0:, 'hotel_id'].unique()

        small_ratings = ratings.loc[
            (ratings['user_id'] < users[user_count]) & (ratings['hotel_id'] < items[hotel_count])]

        print(small_ratings)

        small_ratings.to_csv(path_file_out, sep=',', index=False)

    def calculate_sdv_matrix_rating(self, matrix_rating, items, users):
        matrix_A_T = np.transpose(matrix_rating)
        matrix_M1 = matrix_rating.dot(matrix_A_T)
        w, v = np.linalg.eig(matrix_M1)
        matrix_S = np.sqrt(v)
        matrix_A_xap_xi = pd.DataFrame(index=users, columns=items)
        u, s, vh = np.linalg.svd(matrix_rating,full_matrices=False)
        smat = np.diag(s)
        matrix_A_xap_xi = u.dot(smat).dot(vh)
        matrix_A_xap_xi.to_csv(Constants.DATASET_MATRIX_TRAIN_manh1)

    def convert_rating_to_user_item(self, path_file_in, path_file_train):
        try:
            print(Constants.DATASET_TRAIN_MANH1)
            ratings = pd.read_csv(path_file_in, delimiter=',')

            users = ratings.loc[0:, 'user_id'].unique()
            hotels = ratings.loc[0:, 'hotel_id'].unique()

            matrix_rating = pd.DataFrame(index=users, columns=hotels, dtype='float64')
            # matrix_rating_xapxi = pd.DataFrame(index=users, columns=hotels, dtype='float64')

            total_row = len(ratings)
            for i in range(0, total_row):
                try:
                    userId = ratings.loc[i, 'user_id']
                    hotelId = ratings.loc[i, 'hotel_id']
                    score = ratings.loc[i, 'rate_star']

                    matrix_rating.loc[userId, hotelId] = score

                    print(str(i + 1) + "/" + str(total_row))
                except Exception as e2:
                    print(e2)

            for i in range(0, len(users)):
                for j in range(0, len(hotels)):
                    userId = users[i]
                    hotelId = hotels[j]

                    score = matrix_rating.loc[userId, hotelId]
                    if math.isnan(score):
                        matrix_rating.loc[userId, hotelId] = 0
            matrix_rating.to_csv(path_file_train, sep=',')
            # tinh svd
            self.calculate_sdv_matrix_rating(matrix_rating, hotels, users)
        except Exception as e1:
            print(e1)

    def calculate_similar_item_item(self, path_file_item_train, path_file_item_similar):

        user_item_rating = pd.read_csv(path_file_item_train, index_col=0)
        items = user_item_rating.columns.tolist()

        item_base = pd.DataFrame(index=items, columns=items)
        num_item = len(items)

        for i in range(0, num_item):
            for j in range(i, num_item):
                try:
                    # The usual creation of arrays produces wrong format (as cosine_similarity works on matrices)
                    x = np.array(user_item_rating.iloc[:, i].tolist())
                    y = np.array(user_item_rating.iloc[:, j].tolist())

                    # Need to reshape these
                    x = x.reshape(1, -1)
                    y = y.reshape(1, -1)

                    # calculate similar between two items
                    if not i == j:
                        item_base.iloc[i, j] = cosine_similarity(x, y)[0][0]
                        item_base.iloc[j, i] = cosine_similarity(x, y)[0][0]
                    else:
                        item_base.iloc[i, j] = 1

                except Exception as e:
                    print(e)

                print(str(i) + "/" + str(num_item))

        item_base.to_csv(path_file_item_similar)
        print("Complete item-item-similar!")

    def calculate_similar_user_user(self, path_file_user_train, path_file_user_similar):
        print("Start read path "+ path_file_user_train)
        print("Handle done -> to_csv  path "+ path_file_user_similar)
        user_item_rating = pd.read_csv(path_file_user_train, index_col=0)

        users = user_item_rating.index.tolist()

        users_items_userbase = pd.DataFrame(index=users, columns=users)

        num_users = len(users)

        for i in range(0, num_users):
            for j in range(i, num_users):
                try:
                    # The usual creation of arrays produces wrong format (as cosine_similarity works on matrices)
                    x = np.array(user_item_rating.iloc[i, :].tolist())
                    y = np.array(user_item_rating.iloc[j, :].tolist())

                    # Need to reshape these
                    x = x.reshape(1, -1)
                    y = y.reshape(1, -1)

                    # calculate similar between two items
                    if not i == j:
                        users_items_userbase.iloc[i, j] = cosine_similarity(x, y)[0][0]
                        users_items_userbase.iloc[j, i] = cosine_similarity(x, y)[0][0]
                    else:
                        users_items_userbase.iloc[i, j] = 1

                except Exception as e:
                    print(e)
        print("Tinh xong ")
        users_items_userbase.to_csv(path_file_user_similar, sep=',')
        print("Caclutor Complete !")


train = Trainner()
# manh1
# train.spilit_data_rating(Constants.DATASET_MANH1, 282, 218, Constants.DATASET_MATRIX_TRAIN_manh1)

# train.convert_rating_to_user_item(Constants.DATASET_MANH1, Constants.DATASET_MATRIX_TRAIN_manh1)
# # train.fill_zero()
# train.calculate_similar_user_user(Constants.DATASET_MATRIX_TRAIN_manh1,Constants.DATASET_USER_SIMILAR_manh1)
train.calculate_similar_item_item(Constants.DATASET_MATRIX_TRAIN_manh1,Constants.DATASET_ITEM_SIMILAR_manh1)

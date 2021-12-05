import logging
import math

import numpy as np
import pandas as pd
from numpy import savetxt

from common.constants import Constants

from sklearn.metrics.pairwise import cosine_similarity


class Trainner:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def calculate_sdv_matrix_rating(self, matrix_rating, items, users):
        matrix_A_xap_xi = pd.DataFrame(index=users, columns=items)
        u, s, vh = np.linalg.svd(matrix_rating, full_matrices=False)
        smat = np.diag(s)
        matrix_A_xap_xi = u.dot(smat).dot(vh)
        savetxt(Constants.DATASET_MATRIX_TRAIN_manh1, matrix_A_xap_xi, delimiter=',')

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

                    self.logger.info(str(i + 1) + "/" + str(total_row))
                except Exception as e2:
                    self.logger.error(e2)

            for i in range(0, len(users)):
                for j in range(0, len(hotels)):
                    userId = users[i]
                    hotelId = hotels[j]

                    score = matrix_rating.loc[userId, hotelId]
                    if math.isnan(score):
                        matrix_rating.loc[userId, hotelId] = 0
            # matrix_rating.to_csv(path_file_train, sep=',')
            # tinh svd
            self.logger.info("Start calculate sdv")
            self.calculate_sdv_matrix_rating(matrix_rating, hotels, users)
        except Exception as e1:
            self.logger.exception(e1)

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
                    self.logger.exception(e)

                self.logger.info(str(i) + "/" + str(num_item))

        item_base.to_csv(path_file_item_similar)
        print("Complete item-item-similar!")

    def calculate_similar_user_user(self, path_file_user_train, path_file_user_similar):
        self.logger.info("Start read path " + path_file_user_train)
        self.logger.info("Handle done -> to_csv  path " + path_file_user_similar)
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
                    self.logger.error(e)
        self.logger.info("Tinh xong ")
        users_items_userbase.to_csv(path_file_user_similar, sep=',')
        self.logger.info("Caclutor Complete !")

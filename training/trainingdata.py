import math

import numpy as np
import pandas as pd

from common.constants import Constants

from sklearn.metrics.pairwise import cosine_similarity


class Trainner:

    def convert_rating_to_user_item(self):
        try:
            print(Constants.DATASET_MANH1)
            ratings = pd.read_csv(Constants.DATASET_MANH1, delimiter=',')

            users = ratings.loc[0:, 'user_id'].unique()
            hotels = ratings.loc[0:, 'hotel_id'].unique()

            matrix_rating = pd.DataFrame(index=users, columns=hotels, dtype='float64')

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

            matrix_rating.to_csv(Constants.DATASETS_DIRECTORY_OUT + "user-hotel-manh1.csv", sep=',')
            U, S, V = np.linalg.svd(matrix_rating)
            V_transpose = V.transpose()
            print("Thực hiện transpose thành công")
            matrix_A= U.dot(S).dot(V_transpose)
            print("Tính ma trận A thành công ",matrix_A)
            # matrix_A.to_csv(Constants.DATASETS_DIRECTORY_OUT + "sdv-user-hotel-manh1.csv", sep=',')
            print("Complete !")

        except Exception as e1:
            print(e1)


def fill_zero(self):
    user_item_rating = pd.read_csv(Constants.DATASETS_DIRECTORY_OUT + "user-hotel-manh8.csv", sep=',')

    users = user_item_rating.index.tolist()[1:]
    hotels = user_item_rating.columns.tolist()[1:]

    print(users)
    print(hotels)

    for i in range(0, len(users)):
        for j in range(0, len(hotels)):
            try:
                userId = users[i]
                hotelId = str(hotels[j])

                score = int(user_item_rating.loc[userId, hotelId])
            except Exception:
                score = 0
                user_item_rating.loc[users[i], hotels[j]] = score

            print(score)

    user_item_rating.to_csv(Constants.DATASETS_DIRECTORY_OUT + "user-item.csv", sep=',')
    return


def calculate_similar_item_item(self):
    user_item_rating = pd.read_csv(Constants.DATASETS_DIRECTORY_OUT + "user-hotel-manh1.csv", index_col=0)
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

    item_base.to_csv(Constants.DATASETS_DIRECTORY_OUT + "item-item-similar-manh1.csv")
    print("Complete item-item-similar!")


def calculate_similar_user_user(self):
    user_item_rating = pd.read_csv(Constants.DATASETS_DIRECTORY_OUT + "user-hotel-manh1.csv", index_col=0)
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

    users_items_userbase.to_csv(Constants.DATASETS_DIRECTORY_OUT + "user-user-similar-manh1.csv")
    print("Caclutor Complete !")


def calculate_svd(matrix_rate):
    A = np.array(matrix_rate);


train = Trainner()
train.convert_rating_to_user_item()
# # train.fill_zero()
# train.calculate_similar_user_user()
# train.calculate_similar_item_item()

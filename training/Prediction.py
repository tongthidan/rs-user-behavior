import pandas as pd

from common.constants import Constants


class Prediction:
    # context_exg = "0_0_0"
    @staticmethod
    def prediction_contextual(userid, itemid, context):
        data_train = pd.read_csv(Constants.TRAINING_SUB_DATASETS_DIRECTORY + "train_dataset" + context + ".csv")

        similar = pd.read_csv(Constants.USER_ITEM_DATASETS_DIRECTORY + "user_hotel_train_dataset" + context + ".csv")
        similar_user = similar.loc[similar['Unnamed: 0'] == int(userid)]

        numerator = 0
        denominator = 0

        # lay ra cac ban ghi cua user da danh gia item do
        user_rated = data_train.loc[data_train['hotel_id'] == itemid]

        # lay cac user
        userids = user_rated['user_id'].unique()

        for i in range(0, len(userids)):
            userid = userids[i]
            similar_value = similar_user[str(userid)]
            similar_value = float(similar_value)
            other_user_rated = user_rated.loc[(user_rated['user_id'] == userid)]

            for j in range(0, len(other_user_rated)):
                rating_value = other_user_rated.iloc[j, :]['rate_star']
                numerator += rating_value * similar_value
                denominator += similar_value

        try:
            if float(denominator) == 0:
                return 0
            else:
                return numerator / denominator
        except Exception as e:
            # print(mau)
            return 0

    # @staticmethod
    # def prediction_items_splitting(userid, itemid):
    #     data_train = pd.read_csv(Constants.DATASETS_ITEM_SPLITTING_DIRECTORY + "data-rating.csv")
    #
    #     similar = pd.read_csv(Constants.DATASETS_ITEM_SPLITTING_DIRECTORY + "users-users.csv")
    #     similar_user = similar.loc[similar['Unnamed: 0'] == int(userid)]
    #
    #     numerator = 0
    #     denominator = 0
    #
    #     # lay ra cac ban ghi cua user da danh gia item do
    #     user_rated = data_train.loc[data_train['itemid'] == itemid]
    #
    #     # lay cac user
    #     userids = user_rated['userid'].unique()
    #
    #     for i in range(0, len(userids)):
    #         userid = userids[i]
    #         similar_value = similar_user[str(userid)]
    #         similar_value = float(similar_value)
    #         other_user_rated = user_rated.loc[(user_rated['userid'] == userid)]
    #
    #         for j in range(0, len(other_user_rated)):
    #             rating_value = other_user_rated.iloc[j, :]['rating']
    #             numerator += rating_value * similar_value
    #             denominator += similar_value
    #
    #     try:
    #         if float(denominator) == 0:
    #             return 0
    #         else:
    #             return numerator / denominator
    #     except Exception as e:
    #         # print(mau)
    #         return 0

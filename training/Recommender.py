import json
import logging
from cmath import nan

import pandas as pd

from common.constants import Constants
from entity.Hotel import Hotel


class Recommender:
    def __init__(self):
        pass

    def read_config(self, context):
        self.item_item = pd.read_csv(
            Constants.ITEM_SIMILAR_DATASETS_DIRECTORY + "item_item_similar_user_hotel_train_dataset" + context + ".csv",
            index_col=0)
        self.user_hotel = pd.read_csv(
            Constants.USER_ITEM_DATASETS_NORMAL_DIRECTORY + "user_hotel_train_dataset" + context + ".csv",
            index_col=0)
        # self.user_user = pd.read_csv(
        #     Constants.USER_SIMILAR_DATASETS_DIRECTORY + "user_user_similar_user_hotel_train_dataset" + context + ".csv",
        #     index_col=0)
        self.items = pd.read_csv(Constants.PRODUCT_DATASETS_DIRECTORY + "tblhotel.csv")

    def get_top_ten_predict_for_user(self, userId, context):
        self.read_config(context)
        rating_by_user = self.user_hotel.loc[(self.user_hotel.index == userId)]
        not_rating = []
        items = self.user_hotel.columns.tolist()

        for i in range(0, len(items)):
            if rating_by_user.loc[userId, str(items[i])] == 0:
                not_rating.append(items[i])

        score_not_rating = []

        for i in range(0, len(not_rating)):
            itemId = int(not_rating[i])
            name = self.get_name_hotel(itemId)
            score = self.get_score_user_item(userId, itemId)

            item = Hotel()
            item.id = itemId
            item.name = name
            item.score = score
            score_not_rating.append(item)

        list_sorted = sorted(score_not_rating, key=lambda x: x.score, reverse=True)[:10]

        list_hotel_json = []
        for hotel in list_sorted:
            list_hotel_json.append(json.dumps(hotel.__dict__))
        return list_hotel_json

    def calculate_similar(self, rating, itemsimilarity):
        result = 0
        count = 0

        for i in range(0, len(rating)):
            result += rating[i] * itemsimilarity[i]
            if (rating[i] > 0):
                count += 1
        return result / count

    def get_score_user_item(self, userId, itemId):
        # print(self.user_item)
        try:
            ratings_item = self.user_hotel.loc[userId, :].tolist()
            similar_item = self.item_item.loc[itemId, :].tolist()
            value = self.calculate_similar(ratings_item, similar_item)
            return value
        except Exception as e1:
            print(e1.__cause__)
            return 0

    def get_name_hotel(self, itemId):
        hotel_matrix = pd.DataFrame(self.items)
        hotel = hotel_matrix.loc[self.items.hotel_id == itemId]
        json = hotel.name
        return str(json)

    def result_context_predict(self, context):
        print("Start handle context " + context)
        self.read_config(context)
        userIds = self.user_hotel.index
        result = pd.DataFrame(index=userIds, columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        for i in range(0, len(userIds)):
            userid = userIds[i]
            logging.info("Start calculate predict top 10")
            top10 = self.get_top_ten_predict_for_user(userid, context)
            value = []
            for h in top10:
                y = json.loads(h)
                itemIdRe = y["id"]
                value.append(itemIdRe)
            value_get_size = 10 - len(value)
            if (len(value) < 10):
                for t in range(10 - value_get_size, 10):
                    value.insert(t, nan)
            else:
                value = value
            result.loc[userid] = value

        result_name = "result_predict" + context + ".csv"
        path_out = Constants.RESULT_PREDICT_DATASETS_DIRECTORY + result_name
        result.to_csv(path_out, sep=',')

    def get_score_predict(self, userId, hotelId, context):
        self.read_config(context)
        score = self.get_score_user_item(userId, hotelId)
        return score

    def get_score_user_item_user_similar(self, userId, itemId, context):
        # print(self.user_item)
        self.read_config(context)
        ratings_item = self.user_hotel.loc[userId, :].tolist()
        similar_user = self.user_user.loc[userId, :].tolist()
        value = self.calculate_similar(ratings_item, similar_user)
        return value

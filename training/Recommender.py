import pandas as pd

from common.constants import Constants
from entity.Hotel import Hotel


class Recommender:
    def __init__(self, context):

        self.item_item = pd.read_csv(
            Constants.ITEM_SIMILAR_DATASETS_DIRECTORY + "item_item_similar_user_hotel_train_dataset" + context + ".csv",
            index_col=0)
        self.user_hotel = pd.read_csv(
            Constants.USER_ITEM_DATASETS_NORMAL_DIRECTORY + "user_hotel_train_dataset" + context + ".csv",
            index_col=0)
        self.user_user = pd.read_csv(
            Constants.USER_SIMILAR_DATASETS_DIRECTORY + "user_user_similar_user_hotel_train_dataset" + context + ".csv",
            index_col=0)
        self.items = pd.read_csv(Constants.PRODUCT_DATASETS_DIRECTORY + "tblhotel.csv")

    def recommend_top_ten_by_user(self, userId):
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
        return list_sorted[0:10]

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
        ratings_item = self.user_hotel.loc[userId, :].tolist()
        similar_item = self.item_item.loc[itemId, :].tolist()
        value = self.calculate_similar(ratings_item, similar_item)
        return value

    def get_name_hotel(self, itemId):
        hotel_matrix = pd.DataFrame(self.items)
        hotel = hotel_matrix.loc[self.items.hotel_id == itemId]
        return str(hotel)

import pandas as pd

from common.constants import Constants
from entity.Hotel import Hotel


class Recommender:
    def __init__(self):
        self
        self.item_item = pd.read_csv(Constants.DATASETS_DIRECTORY_OUT + "item-item-similar-manh1.csv", index_col=0)
        self.user_item = pd.read_csv(Constants.DATASETS_DIRECTORY_OUT + "user-hotel-manh1.csv", index_col=0)
        self.user_user = pd.read_csv(Constants.DATASETS_DIRECTORY_OUT + "item-item-similar-manh1.csv", index_col=0)
        self.items = pd.read_csv(Constants.DATASETS_DIRECTORY_INPUT + "tblhotel.csv", sep=',')

    def recommend_top_ten_by_user(self, userId):
        rating_by_user = self.user_item.loc[(self.user_item.index == userId)]
        not_rating = []
        items = self.user_item.columns.tolist()

        for i in range(0, len(items)):
            if rating_by_user.loc[userId, str(items[i])] == 0:
                not_rating.append(items[i])

        score_not_rating = []

        for i in range(0, len(not_rating)):
            itemId = int(not_rating[i])
            score = self.get_score_user_item(userId, itemId)

            item = Hotel()
            item.id = itemId
            item.score = score

            score_not_rating.append(item)

        list_sorted = sorted(score_not_rating, key=lambda x: x.score, reverse=True)[:10]
        data_items = []

        for i in range(0, len(list_sorted)):
            try:
                itemId = list_sorted[i].id

                temp = self.items.loc[self.items['hotel_id'] == itemId]
                item = Hotel()

                print(temp.loc[temp['hotel_id'] == itemId, 'name'])
                print(temp.loc[0,'hotel_id'])
                return

                item.convert_data(temp)
                data_items.append(item)
            except Exception as e:
                print(e)

        print(data_items)

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
        ratings_item = self.user_item.loc[userId, :].tolist()
        similar_item = self.user_user.loc[itemId, :].tolist()
        value = self.calculate_similar(ratings_item, similar_item)
        return value

    def get_name_hotel(self, itemId):
        hotel_matrix = pd.DataFrame(self.items)
        return hotel_matrix.loc[2, itemId]


recommender = Recommender()
print("Top 10 recommend cho 100000001838110 la: ")

print(recommender.recommend_top_ten_by_user(100000001838110))

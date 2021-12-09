import logging
import math

import pandas as pd

from common.constants import Constants
from training.Recommender import Recommender


class Testing:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def test_pre_filtering(self, context):
        file_test_name = "test_dataset" + context + ".csv"
        data_test = pd.read_csv(Constants.TESTING_SUB_DATASETS_DIRECTORY + file_test_name)

        numerator_rmse = 0
        recommend = Recommender()
        result = pd.DataFrame(columns=['hotel_id', 'actual', 'predicted'])

        for i in range(0, len(data_test)):
            record = data_test.iloc[i, :]
            userid = record['user_id']
            itemid = record['hotel_id']

            value_prediction = recommend.get_score_predict(userid, itemid, context)
            print("Score predict: ",value_prediction)
            value_expect = record['rate_star']
            print("Score real : ", value_expect)

            numerator_rmse += math.pow(value_expect - value_prediction, 2)

            result.loc[i, 'hotel_id'] = itemid
            result.loc[i, 'actual'] = value_expect
            result.loc[i, 'predicted'] = value_prediction

        numerator_rmse = math.sqrt(numerator_rmse)
        rmse = numerator_rmse / float(len(data_test))

        relevent_items = result.loc[result['actual'] >= 4]
        recommend_items = result.loc[result['predicted'] >= 4]

        relevent_items = relevent_items.sort_values(by='actual', ascending=False).iloc[0:10, :]
        recommend_items = recommend_items.sort_values(by='predicted', ascending=False).iloc[0:10, :]

        intersection_items = recommend_items.merge(relevent_items)

        precision = len(intersection_items) / len(recommend_items)
        recall = len(intersection_items) / len(relevent_items)

        if precision + recall == 0:
            f_score = 0
        else:
            f_score = 2 * precision * recall / (precision + recall)

        print("RMSE = " + str(rmse))

        print("Precision: " + str(precision))
        print("Recall: " + str(recall))
        print("F-Score: " + str(f_score))

    # def test_item_splitting(self):
    #     data_test = pd.read_csv(Constants.DATASETS_ITEM_SPLITTING_DIRECTORY + "data-test.csv")
    #     data_train = pd.read_csv(Constants.DATASETS_ITEM_SPLITTING_DIRECTORY + "data-rating.csv")
    #
    #     result = pd.DataFrame(columns=['itemid', 'actual', 'predicted'])
    #
    #     numerator_rmse = 0
    #
    #     for i in range(0, len(data_test)):
    #         record = data_train.iloc[i, :]
    #
    #         userid = record['userid']
    #         itemid = record['itemid']
    #
    #         value_prediction = Prediction.prediction_items_splitting(userid, itemid)
    #         value_expect = record['rating']
    #
    #         numerator_rmse += math.pow(value_expect - value_prediction, 2)
    #
    #         result.loc[i, 'itemid'] = itemid
    #         result.loc[i, 'actual'] = value_expect
    #         result.loc[i, 'predicted'] = value_prediction
    #
    #         print("- Process: " + str((i + 1) * 100 / len(data_test)) + "%")
    #
    #     print(result)
    #
    #     numerator_rmse = math.sqrt(numerator_rmse)
    #     rmse = numerator_rmse / float(len(data_test))
    #
    #     relevent_items = result.loc[result['actual'] >= 3.5]
    #     recommend_items = result.loc[result['predicted'] >= 3.5]
    #
    #     relevent_items = relevent_items.sort_values(by='actual', ascending=False).iloc[0:30, :]
    #     recommend_items = recommend_items.sort_values(by='predicted', ascending=False).iloc[0:30, :]
    #
    #     print(relevent_items)
    #     print(recommend_items)
    #
    #     intersection_items = recommend_items.merge(relevent_items)
    #
    #     print(intersection_items)
    #
    #     precision = len(intersection_items) / len(recommend_items)
    #     recall = len(intersection_items) / len(relevent_items)
    #
    #     if precision + recall == 0:
    #         f_score = 0
    #     else:
    #         f_score = 2 * precision * recall / (precision + recall)
    #
    #     print("RMSE = " + str(rmse))
    #     print("F-Score: " + str(f_score))

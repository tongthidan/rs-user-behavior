class Rating:
    def __init__(self):
        self

    def convert_data(self, dataframe):
        print(dataframe.loc[0, 'user_id'])

        return

        self.userId = dataframe.loc[0, 'user_id']
        self.hotelId = dataframe.loc[0, 'hotel_id']
        self.rateStar = dataframe.loc[0, 'rate_star']

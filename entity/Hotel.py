class Hotel:
    def __init__(self):
        self

    def convert_data(self, dataframe):
        print(dataframe.loc[0, 'hotel_id'])

        return

        self.id = dataframe.loc[0, 'hotel_id']
        self.name = dataframe.loc[0, 'name']
        self.address = dataframe.loc[0, 'address']
        self.link = dataframe.loc[0, 'link']

class User:
    def __init__(self):
        self

    def convert_data(self, dataframe):
        print(dataframe.loc[0, 'user_id'])

        return
        self.userId = dataframe.loc[0, 'user_id']
        self.name = dataframe.loc[0, 'name']
        self.link = dataframe.loc[0, 'link']

from database import DataBase
import twitter_data

database = DataBase()

database.insert_user(twitter_data.get_user("elonmusk"))
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='MarioMendoza#02',
            db='mys'
        )

        self.cursor = self.connection.cursor()

    def select_user(self, username):
        sql = "SELECT * FROM usuario WHERE screen_name = '{}'".format(username)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            raise

    def select_all_users(self):
        sql= "SELECT * FROM usuario"

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            users_get = []
            for user in users :
                users_get.append(user)
            return users_get
        
        except Exception as e:
            raise

    def insert_user(self, user):
        sql = "INSERT INTO usuario (id, username, screen_name, location, followers_count, friends_count, listed_count, favourites_count, statuses_count, verified) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (user["id_str"], user["name"], user["screen_name"], user["location"], user["followers_count"], user["friends_count"], user["listed_count"], user["favourites_count"], user["statuses_count"], user["verified"])

        try:
            print("hola, estoy funcionando")
            self.cursor.execute(sql, values)
            self.connection.commit()

        except Exception as e:
            raise
        
    def insert_data(self, data):
        sql = "INSERT INTO user_data (username, text, favourite_count, retweet_count) VALUES (%s, %s, %s, %s)"
        values = (data[0], data[1], data[2], data[3])
    

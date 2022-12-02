from database import DataBase

def user_validation(username):
    value = False
    database = DataBase()
    user_list = database.select_all_users()
    for user in user_list:
        if user[2].lower() == username.lower():
            value = True 
            break
    return value
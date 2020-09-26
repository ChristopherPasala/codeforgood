from models.user_info import UserInfo
from models.user import User
from app import db
from random import randrange

def seed_app():
    clear_data()
    user_ids = []
    ethnicity = ['asian', 'hispanic', 'white', 'black', 'native', 'multi']
    gender = ['male', 'female', 'other']
    poop = open("names.txt", "r")
    user_ids += poop.readlines()
    poop.close()

    final_ethnicity = []
    final_gender = []
    ages = []

    for i in range(120):
        final_ethnicity.append(ethnicity[randrange(5)])
        final_gender.append(gender[randrange(3)])
        ages.append(randrange(14,25))

    for i in range(120):
        user = User(email="jank", name=user_ids[i])
        user.hash_password("password")
        db.session.add(user)
        db.session.commit()
        user_info = UserInfo(user_id=i+1, ethnicity=final_ethnicity[i], age=ages[i], gender=final_gender[i])
        db.session.add(user_info)
        db.session.commit()

def clear_data():
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    seed_app()
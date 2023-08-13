"""Seed file to make sample data for users db."""

from models import Users, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Users.query.delete()

# Add Users
user1 = Users(first_name="jordan", last_name= "Noubissi", image_url="https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTs9nnr6Q3KpVEt_FSH-YcbdhjtqC3HGrU4KYZhuvVPC8uNRP1aZsG3eFcR-d8mKMO8rqXHZ0VCz3L2lpggbh8C2VHV20DIabBMoO85-NsFmbMUFD1qOW4J&usqp=CAc")
user2= new_user = Users(first_name="Jack", last_name="yooo", image_url='https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcT7eIxk3gstP1HWmL0mJbZkEqjIbI94hBAn7ABfpMMps8muyOEn_jNkpUXbd6Hrx6eA4HkX8VQ-dNZA88o_nmKBFQp1BvW60s1XIq735rSOq_y5JzY1yeonvA&usqp=CAc')


# Add new objects to session, so they'll persist
db.session.add(user1)
db.session.add(user2)

# Commit--otherwise, this never gets saved!
db.session.commit()

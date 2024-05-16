from app import db
from app.models import *

jimmy = User(id = 1, username = "Jimmy", email = "j@gmail.com", password = "1234")
minh = User(id = 2, username = "Minh", email = "m@gmail.com", password = "5678")
db.session.add_all([jimmy, minh])
db.session.commit()

from main import Session,engine,User
from sqlalchemy import desc


local_session = Session(bind=engine)

#ascending oder

# users=local_session.query(User).order_by(User.username).all()

#descending order 
users=local_session.query(User).order_by(desc(User.username)).all()
for user in users:
    print(f"User  {user.username} ")
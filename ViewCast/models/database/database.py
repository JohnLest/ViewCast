from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mariadb+mariadbconnector://viewcast:V13w-C4st@192.168.0.101:3307/viewcast")
Session = sessionmaker(bind=engine)

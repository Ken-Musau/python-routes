#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Review, Game

fake = Faker()

if __name__ == '__main__':

    engine = create_engine('sqlite:///instance/app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb
    ipdb.set_trace()

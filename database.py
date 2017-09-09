from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Create database
engine = create_engine('postgresql://localhost:5432/sf-python', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


async def init_db():
    from models import Department, Employee, Role, User, Entity
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create Fixture for Users
    user1 = User(name='user1')
    db_session.add(user1)
    user2 = User(name='user2')
    db_session.add(user2)

    # Create Fixture for Profiles
    entity1 = Entity(user=user1, provider="email", data={"email": "user1@svi.io"})
    db_session.add(entity1)
    entity2 = Entity(user=user1, provider="facebook", data={"token": "blablabla"})
    db_session.add(entity2)
    entity3 = Entity(user=user2, provider="email", data={"email": "user2@svi.io"})
    db_session.add(entity3)

    # Insert seed data into database
    db_session.commit()
    print('committed!')

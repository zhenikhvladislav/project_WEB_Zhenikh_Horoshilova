from sqlalchemy import Column, Integer, String, Text, ForeignKey
from data.db_session import SqlAlchemyBase

class Resume(SqlAlchemyBase):
    __tablename__ = 'resumes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    fullname = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    age = Column(String, nullable=True)
    city = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    social = Column(String, nullable=True)
    messenger = Column(String, nullable=True)
    position = Column(String, nullable=True)
    salary = Column(String, nullable=True)
    education = Column(Text, nullable=True)
    experience = Column(Text, nullable=True)
    skills = Column(Text, nullable=True)
    additional = Column(Text, nullable=True)
    qualities = Column(String, nullable=True)
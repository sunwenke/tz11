from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine("mysql+pymysql://root:198813@localhost:3306/shiyanlou?charset=utf8")
Base = declarative_base()

class Github(Base):
    __tablename__ = 'githubs'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)

if __name__ == '__main__':
    Base.metadata.create_all(engine)


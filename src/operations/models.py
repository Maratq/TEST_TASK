import uuid
from sqlalchemy import Column, String, MetaData, Integer, UniqueConstraint
from src.database import Base, engine

metadata = MetaData()


class Entry(Base):
    __tablename__ = "Entry"

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False,default=uuid.uuid4())
    text = Column(String(255), nullable=True)

    __table_args__ = (
        UniqueConstraint('uuid', name='ux_Entry_uuid'),
    )


def create_database():
    Base.metadata.create_all(bind=engine)

import uuid

from sqlalchemy import Column, MetaData, String
from sqlalchemy.dialects.postgresql import UUID

from src.database import Base, engine

metadata = MetaData()


class Entry(Base):
    __tablename__ = "Entry"

    uuid = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                  default=uuid.uuid4)
    text = Column(String(255), nullable=False)


def create_database():
    Base.metadata.create_all(bind=engine)

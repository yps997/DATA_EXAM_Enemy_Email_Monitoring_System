from database.posrtgreSql import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BaseMessage(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)

    location = relationship("BaseLocation", back_populates="message", uselist=False)
    device = relationship("BaseDevice", back_populates="message", uselist=False)
    sentences = relationship("BaseSentence", back_populates="message")

class BaseLocation(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    country = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    message_id = Column(UUID(as_uuid=True))

class BaseDevice(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    browser = Column(String)
    os = Column(String)
    device_id = Column(UUID(as_uuid=True))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    message_id = Column(UUID(as_uuid=True))

class BaseSentence(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    message_id = Column(UUID(as_uuid=True))
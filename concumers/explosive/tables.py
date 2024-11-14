from concumers.pattern import *

class ExplosiveMessage(BaseMessage):
    __tablename__ = 'explosive_messages'

class ExplosiveLocation(BaseLocation):
    __tablename__ = 'explosive_locations'
    message_id = Column(UUID(as_uuid=True), ForeignKey('explosive_messages.id'))
    message = relationship("ExplosiveMessage", back_populates="location")

class ExplosiveDevice(BaseDevice):
    __tablename__ = 'explosive_devices'
    message_id = Column(UUID(as_uuid=True), ForeignKey('explosive_messages.id'))
    message = relationship("ExplosiveMessage", back_populates="device")

class ExplosiveSentence(BaseSentence):
    __tablename__ = 'explosive_sentences'
    message_id = Column(UUID(as_uuid=True), ForeignKey('explosive_messages.id'))
    message = relationship("ExplosiveMessage", back_populates="sentences")
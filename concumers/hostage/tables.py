from concumers.pattern import *

class HostageMessage(BaseMessage):
    __tablename__ = 'hostage_messages'

class HostageLocation(BaseLocation):
    __tablename__ = 'hostage_locations'
    message_id = Column(UUID(as_uuid=True), ForeignKey('hostage_messages.id'))
    message = relationship("HostageMessage", back_populates="location")

class HostageDevice(BaseDevice):
    __tablename__ = 'hostage_devices'
    message_id = Column(UUID(as_uuid=True), ForeignKey('hostage_messages.id'))
    message = relationship("HostageMessage", back_populates="device")

class HostageSentence(BaseSentence):
    __tablename__ = 'hostage_sentences'
    message_id = Column(UUID(as_uuid=True), ForeignKey('hostage_messages.id'))
    message = relationship("HostageMessage", back_populates="sentences")
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, TIMESTAMP
from config.db import meta, engine
import uuid
import datetime


messages = Table(
  'messages', meta,
  Column('uuid', String(255), primary_key=True, default=uuid.uuid4()),
  Column('senderPhone', String(255)),
  Column('receiverPhone', String(255)),
  Column('messageText', String(255)),
  Column('timestamp', TIMESTAMP(timezone=False), nullable=False, default=datetime.datetime.now())
)

meta.create_all(engine)
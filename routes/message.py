from fastapi import APIRouter
from config.db import conn
from models.message import messages
from schemas.message import Message
from typing import Optional
from sqlalchemy import and_, or_

message = APIRouter()

@message.get('/messages')
async def get_messages():
  return conn.execute(messages.select()).fetchall()

@message.get("/channel")
async def channel_messages(sender: str, receiver: str):
  return conn.execute(messages.select().where(
    or_(
      and_(messages.c.senderPhone == sender, messages.c.receiverPhone == receiver),
      and_(messages.c.senderPhone == receiver, messages.c.receiverPhone == sender)
    )
    ).order_by(messages.c.timestamp.asc())).fetchall()

@message.get("/channels")
async def get_channels(sender: str):
  result = conn.execute(messages.select()
  .where(or_(messages.c.senderPhone == sender, messages.c.receiverPhone == sender))
  .order_by(messages.c.timestamp.desc()))
  receivers = list()
  for x in result:
    if not x.senderPhone == sender:
      receivers.append(x.senderPhone)
    if not x.receiverPhone == sender:
      receivers.append(x.receiverPhone)
  return set(receivers)

@message.post("/message")
async def write_message(message: Message):
  conn.execute(messages.insert().values(
    senderPhone= message.senderPhone,
    receiverPhone= message.receiverPhone,
    messageText= message.messageText,
  ))
  return conn.execute(messages.select()).fetchall()

@message.delete('/message/{uuid}')
async def delete_message(uuid: str):
  conn.execute(messages.delete().where(messages.c.uuid == uuid))
  return {}
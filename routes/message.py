from fastapi import APIRouter
from config.db import conn
from models.message import messages
from schemas.message import Message
from typing import Optional

message = APIRouter()

@message.get("/messages")
async def read_messages():
  return conn.execute(messages.select()).fetchall()

@message.post("/messages")
async def write_messages(message: Message):
  conn.execute(messages.insert().values(
    senderPhone= message.senderPhone,
    receiverPhone= message.senderPhone,
    messageText= message.messageText,
  ))
  return conn.execute(messages.select()).fetchall()
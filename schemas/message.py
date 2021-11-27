from pydantic import BaseModel

class Message(BaseModel):
  senderPhone: str
  receiverPhone: str
  messageText: str
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3306/sms-message")
# engine = create_engine('sqlite:///users.db', echo = True)
meta = MetaData()
conn = engine.connect()

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import *

from configuration import *

engine = create_engine(
    f"iomete://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?account_number={ACCOUNT_NUMBER}&lakehouse={LAKEHOUSE}")

session = sessionmaker(bind=engine)()
records = session.query(Table(TABLE, MetaData(bind=engine), autoload=True)) \
    .limit(10) \
    .all()
print(records)

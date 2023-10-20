from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import *

from configuration import *


# Possible dialects (hive and iomete are both operate identically):
# hive+http
# hive+https
# iomete+http
# iomete+https

dialect = "iomete+https"
if SCHEME == "http":
    dialect = "iomete+http"

engine = create_engine(
    f"{dialect}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?lakehouse={LAKEHOUSE}")


def query_table():
    session = sessionmaker(bind=engine)()
    records = session.query(Table(TABLE, MetaData(bind=engine), autoload=True)) \
        .limit(10) \
        .all()
    print(records)


def get_table_names():
    from sqlalchemy import inspect
    inspector = inspect(engine)
    print(inspector.get_table_names())


if __name__ == '__main__':
    query_table()

    get_table_names()

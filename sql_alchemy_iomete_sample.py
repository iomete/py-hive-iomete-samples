from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import *

from configuration import *

engine = create_engine(
    f"iomete://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?workspace_id={WORKSPACE_ID}&lakehouse={LAKEHOUSE}")


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

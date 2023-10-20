from pyhive import hive
from configuration import *

connection = hive.connect(
    host=HOST,
    port=PORT,
    scheme=SCHEME,
    lakehouse=LAKEHOUSE,
    database=DATABASE,
    username=USERNAME,
    password=PASSWORD
)

cursor = connection.cursor()
cursor.execute(f"select * from {TABLE} limit 10")

print(cursor.fetchone())
print(cursor.fetchall())

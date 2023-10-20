from pyhive import hive
from TCLIService.ttypes import TOperationState
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
cursor.execute(f"SELECT * FROM {TABLE} LIMIT 10", async_=True)

status = cursor.poll().operationState

while status in (TOperationState.INITIALIZED_STATE, TOperationState.RUNNING_STATE):
    logs = cursor.fetch_logs()
    for message in logs:
        print(message)

    # If needed, an asynchronous query can be cancelled at any time with:
    # cursor.cancel()

    status = cursor.poll().operationState

print(cursor.fetchall())

# Sample codes for py-hive-iomete

This is a samples repository to show how to use [py-hive-iomete](https://github.com/iomete/py-hive-iomete)

## Prepare environment

### Create a virtual env

```shell
virtualenv .env
source .env/bin/activate
```

### Install py-hive-iomete package

```shell
pip install --upgrade py-hive-iomete

# or, the following which additionally install SQLAlchemy  
pip install --upgrade "py-hive-iomete[sqlalchemy]"
```

## Run samples

First, go to `configuration.py` and set the correct values to the options 

```shell
# DB-API Samples
python db_api_sample.py
python db_api_asynchronous_sample.py

# SQLAlchemy Samples
python sql_alchemy_iomete_sample.py
```

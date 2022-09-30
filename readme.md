# Sample codes for py-hive-iomete

## Prepare environment

### Create a virtual env

```shell
virtualenv .env
source .env/bin/activate
```

### Install py-hive-iomete package

```shell
pip install py-hive-iomete

# or, the following which additionally install SQLAlchemy  
pip install "py-hive-iomete[sqlalchemy]"
```

## Run samples

First, go to `configuration.py` and set the correct values to the options 

```shell
# DB-API Samples
python db_api_sample.py
python db_api_asynchronous_sample.py

# SQLAlchemy Samples
python sql_alchemy_iomete_sample.py
python sql_alchemy_hive_sample.py
```

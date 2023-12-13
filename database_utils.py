import yaml
import pandas as pd
import sqlalchemy

class DatabaseConnector:
    def __init__(self):
        self.db_config = self.read_db_creds()

    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as file:
            return yaml.safe_load(file)

    def init_db_engine(self):
        # Extract the necessary credentials
        database_type = 'postgresql'
        host = self.db_config['RDS_HOST']
        username = self.db_config['RDS_USER']
        password = self.db_config['RDS_PASSWORD']
        database = self.db_config['RDS_DATABASE']
        port = self.db_config['RDS_PORT']

        # Construct the database connection URL
        db_conn_url = f"{database_type}://{username}:{password}@{host}:{port}/{database}"

        # Create and return the SQLAlchemy engine
        engine = sqlalchemy.create_engine(db_conn_url)
        return engine

    def list_db_tables(self):
        engine = self.init_db_engine()
        with engine.connect() as connection:
            # Get the metadata of the database
            metadata = sqlalchemy.MetaData()
            metadata.reflect(bind=connection)

            # Get the table names from the metadata
            table_names = metadata.tables.keys()

            return table_names

    def upload_to_db(self, df, table_name):
        engine = self.init_db_engine()
        df.to_sql(table_name, engine, if_exists='replace')

if __name__ == '__main__':
    print('Tables in Database:', DatabaseConnector().list_db_tables())
   
    from data_cleaning import DataCleaning
    DatabaseConnector().upload_to_db(DataCleaning().clean_user_data(pd.DataFrame()), 'dim_users')

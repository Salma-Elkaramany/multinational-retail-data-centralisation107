# main.py
from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
from data_extraction import DataExtractor

def initialize_components():
    data_extractor = DataExtractor()
    db_conn = DatabaseConnector()
    data_cleaner = DataCleaning()
    engine = db_conn.init_db_engine()
    return data_extractor, db_conn, data_cleaner, engine

def list_all_tables(db_conn):
    all_tables = db_conn.list_db_tables()
    print(f"All tables: {all_tables}")

def extract_and_clean_store_data(data_extractor, data_cleaner, db_conn):
    raw_data = data_extractor.retrieve_stores_data()
    cleaned_data = data_cleaner.clean_store_data(raw_data)
    if cleaned_data is not None:
        db_conn.upload_to_db(cleaned_data, 'dim_store_details')
        print("Uploaded cleaned data to dim_store_details table.")

def process_orders_data(data_extractor, data_cleaner, db_conn):
    orders_data = data_extractor.read_rds_table(db_conn, 'orders_table')
    cleaned_orders_data = data_cleaner.clean_orders_data(orders_data)
    db_conn.upload_to_db(cleaned_orders_data, 'orders_table')
    print("Uploaded cleaned orders data to orders_table.")

def main():
    data_extractor, db_conn, data_cleaner, engine = initialize_components()

    # List all tables
    list_all_tables(db_conn)

    # Extract and clean store data
    extract_and_clean_store_data(data_extractor, data_cleaner, db_conn)

    # Process orders data
    process_orders_data(data_extractor, data_cleaner, db_conn)

if __name__ == "__main__":
    main()

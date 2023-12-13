import pandas as pd
import requests
import tabula
import boto3
from database_utils import DatabaseConnector

class DataExtractor:
    def __init__(self):
        self.db = DatabaseConnector()
        self.rds_database = self.db.init_db_engine()
        self.api_key = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        self.num_stores_api_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        self.bucket_name = 'data-handling-public'

    def read_rds_table(self, table_name):
        return pd.read_sql_table(table_name, self.rds_database)

    def retrieve_pdf_data(self, pdf_link):
        pdf_dataframes = tabula.read_pdf(pdf_link, pages="all", multiple_tables=True)
        return pd.concat(pdf_dataframes, ignore_index=True)

    def list_number_of_store(self):
        stores = requests.get(self.num_stores_api_endpoint, headers=self.api_key)
        number_of_stores = stores.json()
        return number_of_stores["number_stores"]

    def retrieve_stores_data(self):
        number_of_stores = self.list_number_of_store()
        stores_list = []

        for store_number in range(1, number_of_stores + 1):
            api_url = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
            response = requests.get(api_url, headers=self.api_key)

            if response.status_code == 200:
                stores_list.append(pd.json_normalize(response.json()))
            else:
                print(f"Failed to get data for store {store_number}")

        return pd.concat(stores_list)

    def extract_from_s3(self, object_name):
        file_path = f'./{object_name}'
        s3 = boto3.client('s3')
        s3.download_file(self.bucket_name, object_name, file_path)
        return pd.read_csv(file_path)

    def extract_from_s3_json(self, object_name):
        file_path = f'./{object_name}'
        s3 = boto3.client('s3')
        s3.download_file(self.bucket_name, object_name, file_path)
        return pd.read_json(file_path)

if __name__ == "__main__":
    data_extractor = DataExtractor()
    # Example usage (you can add more as needed)
    pdf_data = data_extractor.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
    store_data = data_extractor.retrieve_stores_data()
    s3_table = data_extractor.extract_from_s3('products.csv')
    s3_json_table = data_extractor.extract_from_s3_json('date_details.json')

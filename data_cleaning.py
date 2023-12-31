import pandas as pd
import numpy as np
from data_extraction import DataExtractor

class DataCleaning:
    @staticmethod
    def remove_char_from_string(value):
        return ''.join(char for char in value if char.isdigit())

    @staticmethod
    def clean_invalid_date(df, column):
        df[column] = pd.to_datetime(df[column], errors='coerce')
        return df

    @staticmethod
    def convert_weight(weight_str):
        weight_str = weight_str.lower()
        if 'kg' in weight_str:
            return float(weight_str.replace('kg', '').strip())
        elif 'g' in weight_str:
            return float(weight_str.replace('g', '').strip()) / 1000
        elif 'ml' in weight_str:
            return float(weight_str.replace('ml', '').strip()) / 1000
        return 0.0

    @staticmethod
    def clean_common_data(df, drop_columns=None, dropna_columns=None):
        if drop_columns:
            df.drop(columns=drop_columns, inplace=True)
        if dropna_columns:
            df.dropna(subset=dropna_columns, how='any', inplace=True)
        return df

    def clean_user_data(self, df):
        df = self.clean_common_data(df, dropna_columns=['date_of_birth', 'join_date'])
        return df

    def clean_card_data(self, df):
        df = self.clean_common_data(df, dropna_columns=['card_number', 'date_payment_confirmed'])
        df['card_number'] = df['card_number'].astype(str).str.replace('\W', '', regex=True)
        df['card_number'] = df['card_number'].apply(lambda x: np.nan if x == 'NULL' else x)
        return df

    def clean_store_data(self, df):
        df = self.clean_common_data(df, drop_columns=['lat'], dropna_columns=['opening_date', 'store_type'])
        df['continent'] = df['continent'].replace({'eeEurope': 'Europe', 'eeAmerica': 'America'})
        df['store_type'] = df['store_type'].astype(str).apply(lambda x: np.nan if x == 'NULL' else x)
        df['staff_numbers'] = pd.to_numeric(df['staff_numbers'].apply(self.remove_char_from_string),
                                            errors='coerce', downcast="integer")
        return df

    def convert_product_weights(self, df):
        df['Weight'] = df['Weight'].apply(self.convert_weight)
        return df

    def clean_products_data(self, df):
        df = self.clean_common_data(df, dropna_columns=['uuid', 'product_code'])
        df['date_added'] = pd.to_datetime(df['date_added'], format='%Y-%m-%d', errors='coerce')
        drop_prod_list = ['S1YB74MLMJ', 'C3NCA2CL35', 'WVPMHZP59U']
        df.drop(df[df['category'].isin(drop_prod_list)].index, inplace=True)
        return df

    def clean_orders_data(self, df):
        df = self.clean_common_data(df, drop_columns=['1', 'first_name', 'last_name', 'level_0'])
        return df

    def clean_date_times(self, df):
        df['day'] = pd.to_numeric(df['day'], errors='coerce')
        df = self.clean_common_data(df, dropna_columns=['day', 'year', 'month'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%H:%M:%S', errors='coerce')
        return df


if __name__ == "__main__":
    data_cleaner = DataCleaning()

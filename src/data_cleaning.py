import pandas as pd
import shutil
import random

df = pd.read_csv('/home/mogra/Desktop/Projetos python/Data_Science/Projetos-Portifolio/ecommerce_dataset/data/realistic_e_commerce_sales_data.csv',
                 low_memory=False, parse_dates=True)
pd.set_option('display.max_columns', None)

def data_cleaning():
      global df
      # replace duplicated values
      df.duplicated(keep='first')
      # remove outliers
      if df['Age'].max() > 100:
            df.drop(df['Age'] > 100, axis=1, inplace=True)
      
def data_processing():
      global df
      # avarage age
      avarage_age = df['Age'].mean()
      # switch na to the avarage age
      df['Age'] = df['Age'].fillna(avarage_age)
      df['Age'] = df['Age'].replace([float('inf'), -float('inf')], 0).fillna(0).astype(int)

      region = ['South', 'North', 'West', 'East']
      df['Region'] = df['Region'].fillna(random.choice(region))

def data_posprocessing():
    global df
    clean_file_path = 'clean_database.csv'
    __move_location = '/home/mogra/Desktop/Projetos python/Data_Science/Projetos-Portifolio/ecommerce_dataset/data'
    # data converting
    df.to_csv(clean_file_path, index=False)
    # move file to data directory
    shutil.move(clean_file_path, __move_location)

data_cleaning()
data_processing()
data_posprocessing()
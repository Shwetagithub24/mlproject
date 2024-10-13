import os
import sys
#from pathlib import Path
#sys.path.append(str(Path(__file__).parent.parent))
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts','train.csv')   # all the outputs will be saved in artifacts folder
    test_data_path : str=os.path.join('artifacts','test.csv') 
    raw_data_path : str=os.path.join('artifacts','data.csv') 

class DataIngestion:
     def __init__(self):
          self.ingestion_config=DataIngestionConfig()

     def initiate_data_ingestion(self):
          logging.info("Enter the Data Ingestion method or component")
          try:
            # 1. Read dataset
               df=pd.read_csv('notebook\data\stud.csv')
               logging.info('Read the Dataset in the Dataframe.')

            # 2. Save it locally in Artifacts folder
               os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
               df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            # 3. Train Test Split
               logging.info("Train Test Split Initiated")
               train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
                
            # 4. Save Train test split in artifacts folder
               train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
               test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

               logging.info("Data Ingestion Completed.")

            # return for Data Transformation
               return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path,
               )

          except Exception as e:
               raise CustomException(e,sys)
          

if __name__ == "__main__":
    obj = DataIngestion()  # Properly create an instance of the DataIngestion class
    train_data,test_data=obj.initiate_data_ingestion()  # Call the method using the instance


data_transformation=DataTransformation()
data_transformation.initiate_data_transformation(train_data,test_data)
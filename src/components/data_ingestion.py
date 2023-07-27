from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os,sys

@dataclass
class Data_ingestion_config:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')
class Data_ingestion:
    def __init__(self):
        self.ingestion_config=Data_ingestion_config()
    def inititae_data_ingestion(self):
        try:
            logging.info("Data ingestion has been initiated")
            ## data has been read from the server
            data=pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/credit_card_pw_hindi/main/creditCardFraud_28011964_120214.csv")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.train_data_path)
            logging.info("the data is been splitted into train and test data")

            train_data,test_data=train_test_split(data,test_size=0.30,random_state=30)

        
            train_data.to_csv(self.ingestion_config.train_data_path)
            test_data.to_csv(self.ingestion_config.test_data_path)

            logging.info("Data ingestion has been completed")

            return (self.ingestion_config.train_data_path, 
                    self.ingestion_config.test_data_path)

        except Exception as e:
            logging.info("Error occured at Dataingestion Process")

 
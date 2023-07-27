from src.logger import logging
from src.components.data_ingestion import Data_ingestion
import os,sys
import pandas as pd
import numpy as np
from src.exception import CustomException


if __name__=='__main__':
    obj=Data_ingestion()
    train_data_path,test_data_path=obj.inititae_data_ingestion()
    print(train_data_path,test_data_path)
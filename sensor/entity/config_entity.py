import os
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime
import sys
FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test_csv"

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M_%S')}")
        except Exception  as e:
            raise SensorException(e,sys) 


class DataInjestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="aps"
            self.collection_name="sensor"
            self.data_injestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_injestion")
            self.feature_store_dir= os.path.join(self.data_injestion_dir,"feature")
            self.train_file_path=os.path.join(self.data_injestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_injestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size=0.02
        except Exception as e:
            raise SensorException(e,sys)

    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)




class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...
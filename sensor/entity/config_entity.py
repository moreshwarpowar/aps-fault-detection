import os

class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M_%S')}")


class DataInjestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name="aps"
        self.collection_name="sensor"
        self.data_injestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_injestion")
        self.feature_store_dir= os.path.join(self.data_injestion_dir,"feature")



class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...
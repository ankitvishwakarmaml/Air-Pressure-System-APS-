from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import MyException
import os , sys
from src.logger import logging
#from src.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from src.pipeline.training_pipeline import TrainPipeline
#from src.utilsmongoDB import dump_csv_file_to_mongodb_collection

# def test_exception():
#     try:
#         logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
#         a=1/0
#     except Exception as e:
#        raise SensorException(e,sys) 



if __name__ == "__main__":

    #file_path="aps_failure_training_set1.csv"
    #database_name="MyDatabase"
    #collection_name ="sensor"
    #dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import MyException
from src.logger import logging
import sys
from src.pipeline.training_pipeline import TrainPipeline

if __name__=="__main__":

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
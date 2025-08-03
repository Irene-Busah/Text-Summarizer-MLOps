"""
data_ingestion_pipeline.py
=============================


Implements the data ingestion pipeline to use the component
"""


# Libraries
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.logging import logger


STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"--------------------- {STAGE_NAME} Started Successfully ---------------------")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()

        logger.info(f"--------------------- {STAGE_NAME} Completed Successfully ---------------------")

    except Exception as e:
        logger.exception(e)
        raise e



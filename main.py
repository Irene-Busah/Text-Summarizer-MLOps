"""
main.py
=========

The main project entry point to run the entire ML pipeline
"""


# libraries
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline

logger.info("Welcome to the Text Summarizer Project")


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f"------------ {STAGE_NAME} Started Successfully ------------")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()

    logger.info(f"----------- {STAGE_NAME} Completed Successfully -----------")

except Exception as e:
    logger.exception(e)
    raise e



# ========================= Transformation ============================

STAGE_NAME = 'Data Transformation Stage'

try:
    logger.info(f"---------- {STAGE_NAME} Started Successfully ----------")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()

    logger.info(f"--------- {STAGE_NAME} Completed Successfully ---------")

except Exception as e:
    logger.exception(e)
    raise e

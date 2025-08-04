"""
data_transformation_pipeline.py
=================================


Implements the data transformation pipeline
"""


# libraries
from src.textSummarizer.logging import logger
from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation Stage"


class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        config = ConfigurationManager()

        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()


if __name__ == '__main__':
    try:
        logger.info(f"--------------------- {STAGE_NAME} Started Successfully ---------------------")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()

        logger.info(f"--------------------- {STAGE_NAME} Completed Successfully ---------------------")

    except Exception as e:
        logger.exception(e)
        raise e


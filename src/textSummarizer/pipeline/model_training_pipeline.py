"""
model_training_pipeline.py
============================

Implements the model training pipeline to use the component
"""


# libraries
from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_training import ModelTraining


STAGE_NAME = "Data Transformation Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = ConfigurationManager()

        model_training_config = config.get_model_training_config()
        model_training_config = ModelTraining(config=model_training_config)

        model_training_config.train()


if __name__ == '__main__':
    try:
        logger.info(f"--------------------- {STAGE_NAME} Started Successfully ---------------------")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()

        logger.info(f"--------------------- {STAGE_NAME} Completed Successfully ---------------------")

    except Exception as e:
        logger.exception(e)
        raise e


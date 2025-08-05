"""
model_evaluation_pipeline.py
============================

Implements the model evaluation pipeline to use the component
"""


# libraries
from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_evaluation import ModelEvaluation


STAGE_NAME = "Data Transformation Stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()

        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)

        model_evaluation_config.evaluate_model()


if __name__ == '__main__':
    try:
        logger.info(f"--------------------- {STAGE_NAME} Started Successfully ---------------------")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_training()

        logger.info(f"--------------------- {STAGE_NAME} Completed Successfully ---------------------")

    except Exception as e:
        logger.exception(e)
        raise e


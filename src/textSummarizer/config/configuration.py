"""
configuration.py
=================

Implement the configuration manager for the pipeline
"""


# libraries
from src.textSummarizer.entity.entity import DataIngestionConfig, DataTransformationConfig
from src.textSummarizer.logging import logger
from src.textSummarizer.utils.common import create_directories, read_yaml

from src.textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH


class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)


        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    # data transformation configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_filepath=config.data_filepath,
            tokenizer_name=config.tokenizer_name
        )

        return data_transformation_config

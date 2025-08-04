"""
data_transformation.py
========================


Implements the data transformation component for the pipeline
"""


# libraries
import os
from src.textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk

from src.textSummarizer.entity.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    

    # method to get features
    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)
        
        target_encodings = self.tokenizer(
            text_target=example_batch['summary'], 
            max_length=128, 
            truncation=True
        )
        
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    # method to apply to the dataset
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_filepath)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)

        # saving the converted data to disk
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))

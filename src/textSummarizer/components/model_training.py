"""
model_training.py
===================

Implements the model training pipeline
"""


# libraries
from src.textSummarizer.logging import logger
from src.textSummarizer.entity.entity import ModelTrainerConfig
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
import torch
import os
from datasets import load_from_disk


class ModelTraining:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    # method to train the model
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        #loading the data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16,
            report_to="none",
            dataloader_pin_memory=False
        ) 
        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  processing_class=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["train"],
                  eval_dataset=dataset_samsum_pt["validation"])
        
        trainer.train()

        ## Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))

        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))



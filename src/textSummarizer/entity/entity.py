"""
entity.py
===================

Implements the entities for the various pipelines
"""


# libraries
from dataclasses import dataclass
from pathlib import Path
import os


# Data Ingestion Entity
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path


import os
from os import path
from box.exceptions import BoxValueError
import yaml
from mySummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (str): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For other errors during file reading or YAML parsing.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"The YAML file at {path_to_yaml} is empty.")
            logger.info(f"Successfully read YAML file: {path_to_yaml}")
            return ConfigBox(content)
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create directories from the given paths.

    Args:
        path_to_directories (list): List of paths to the directories.
        verbose (bool, optional): Whether to log creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size in KB.

    Args:
        path (Path): The path to the file or directory.

    Returns:
        str: The size of the file or directory in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"
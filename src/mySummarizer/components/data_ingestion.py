import os
import urllib.request as request
import zipfile
from mySummarizer.entity import DataIngestionConfig
from mySummarizer.logging import logger
from mySummarizer.utils.common import get_size
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename} with the following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(zipfile.Path(self.config.local_data_file))}")



    def extract_file(self):
        """
        Unzip the downloaded file.
        Extracts the zip file to the specified directory.
        Functions returns None.

        """

        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
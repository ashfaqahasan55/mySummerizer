from mySummarizer.config.configuration import ConfiguartionManager
from mySummarizer.components.data_transformation import DataTransformation 
from mySummarizer.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguartionManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
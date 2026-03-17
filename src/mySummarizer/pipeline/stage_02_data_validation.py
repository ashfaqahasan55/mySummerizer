from mySummarizer.config.configuration import ConfiguartionManager
from mySummarizer.components.data_validation import DataValidation
from mySummarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguartionManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_required_files()
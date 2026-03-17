import os
from mySummarizer.entity import DataValidationConfig
from mySummarizer.logging import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_required_files(self) -> bool:
        try:
            validation_status = None

            all_required_files = os.listdir(os.path.join("artifacts", "data_ingestion","samsum_dataset"))

            for file in all_required_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Required file: {file} is not present in the directory. validation_status = False")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"All required files are present in the directory. validation_status = True")
                        
                return validation_status
        
        
        except Exception as e:
            raise e

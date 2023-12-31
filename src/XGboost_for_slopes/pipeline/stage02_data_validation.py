from XGboost_for_slopes.config.configuration import ConfigurationManager
from XGboost_for_slopes.components.data_validation import DataValidation
from XGboost_for_slopes import logger
import sys
from XGboost_for_slopes.exception.exception import CustomException

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_all_columns_dtypes()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)

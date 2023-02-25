from extract import PostingsExtractor
from transform import PostingsTransformer
from load import PostingsLoader
from config.config import SOURCE_URL, CONNECTION_STRING
from datetime import datetime
import os
import logging

def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter(
        "%(asctime)s %(filename)-20s %(lineno)-5d %(levelname)-10s %(message)s"
    )
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


current_date = datetime.now().strftime(r"%d%m%Y_%H%M%S")

logger = setup_logger(
    __name__,
    log_file=f"{os.environ['PYTHONPATH']}/logs/{current_date}.log",
    level=logging.DEBUG,
)

class ETLJob:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run_etl(self):
        try:
            data = self.extractor.extract()
            df = self.transformer.transform(data)
            self.loader.load(df)
        except Exception as e:
            print(f"Exception occured. Details: {e}")
            raise

def main():

    extractor = PostingsExtractor(SOURCE_URL)
    transformer = PostingsTransformer()
    loader = PostingsLoader(CONNECTION_STRING)

    etl = ETLJob(
        extractor=extractor,
        transformer=transformer,
        loader=loader
    )

    logger.info("Starting ETL job")

    etl.run_etl()

    logger.info("Job finished successfully")

if __name__ == "__main__":
    main()
from extract import PostingsExtractor
from transform import PostingsTransformer
from load import PostingsLoader
from config.config import SOURCE_URL, CONNECTION_STRING

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

    etl.run_etl()

if __name__ == "__main__":
    main()
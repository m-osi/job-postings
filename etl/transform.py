from config.config import SOURCE_URL, QUERY_PARAMS
from etl.extract import PostingsExtractor
import pandas as pd
import json

Extractor = PostingsExtractor(SOURCE_URL)
data = Extractor.extract()

class PostingsTransformer:
    def __init__(self, params):
        self.params = params

    def transform(self, content):

        data = self.parse_to_json(content)

        df = pd.DataFrame(data)
        df = df[df.set_index(list(self.params.keys()))
                .index.isin(zip(*list(self.params.values())))]
        
        return df
    
    @staticmethod
    def parse_to_json(content):
        return (json.loads(content))




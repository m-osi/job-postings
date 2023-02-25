import pandas as pd
import json
import logging

logger = logging.getLogger("__main__")

class PostingsTransformer:

    def transform(self, content):

        data = self.parse_to_json(content)
        df = pd.DataFrame(data)
        df = self.expand_columns(df, ['employment_types', 'skills'])
        df.drop(columns=['id', 'company_logo_url',
                'salary', 'multilocation'], inplace=True)
        df.rename({'salary.to': 'salary_to',
                   'salary.from': 'salary_from',
                   'salary.currency': 'salary_currency'}, axis=1, inplace=True)
        df.drop_duplicates(inplace=True)
        logger.info("Data transformed successfully")
        # df = df[df.set_index(list(self.params.keys()))
        #         .index.isin(zip(*list(self.params.values())))]

        return df

    @staticmethod
    def parse_to_json(content):
        return (json.loads(content))

    @staticmethod
    def expand_columns(df, columns):
        for column in columns:
            df = df.explode(column).reset_index()
        df.drop(columns=['level_0', 'index'], inplace=True)
        for column in columns:
            df = pd.concat([df, pd.json_normalize(df[column])], axis=1)
            df.drop(columns=column, inplace=True)
        return df

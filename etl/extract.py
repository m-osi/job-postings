from contextlib import closing
from requests import get
from requests.exceptions import (
    ConnectionError,
    HTTPError
)


class PostingsExtractor:
    def __init__(self, url):
        self.url = url

    def extract(self):

        try:
            with closing(get(self.url)) as res:
                if self.validate_response(res):
                    return res.content
                else:
                    return None

        except (ConnectionError, HTTPError) as e:
            print(f"Error occurred. Details: {e}")

    @staticmethod
    def validate_response(res):
        return (res.status_code == 200
                & len(res.content) > 0)

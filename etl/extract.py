from contextlib import closing
import logging
from requests import get
from requests.exceptions import (
    ConnectionError,
    HTTPError
)

logger = logging.getLogger("__main__")


class PostingsExtractor:
    def __init__(self, url):
        self.url = url

    def extract(self):

        try:
            with closing(get(self.url)) as res:
                if self.validate_response(res):
                    logger.debug(
                        f"Data extracted successfully from: {self.url}")
                    return res.content
                else:
                    return None

        except (ConnectionError, HTTPError) as e:
            logger.error(f"Error while extracting data. Details: {e}")
            raise Exception

    @staticmethod
    def validate_response(res):
        return ((res.status_code == 200) & (len(res.content) > 0))

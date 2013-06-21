import logging
import requests
from requests.exceptions import RequestException
from moxie_webcams.providers import WebcamProviderException

logger = logging.getLogger(__name__)


class StillImageProvider(object):

    def __init__(self, timeout=1):
        self.timeout = timeout

    def get_image(self, url):
        try:
            response = requests.get(url, timeout=self.timeout)
            return response.content
        except RequestException as re:
            logger.warn("Couldn't fetch image", exc_info=True, extra={
                'data': {
                    'url': url
                }
            })
            raise WebcamProviderException(re.message)

from moxie.core.service import Service

from .domain import Webcam
from .providers.still_image import StillImageProvider


class WebcamsService(Service):

    def __init__(self, webcams_list):
        self.webcams = webcams_list

    def get_all_webcams(self):
        return [Webcam.from_yaml(k, v) for k, v in self.webcams.iteritems()]

    def get_still_image(self, webcam_slug):
        """Get an image for the given webcam
        :param webcam_slug: unique identifier of the webcam
        :return: tbd
        """
        provider = StillImageProvider()
        webcam = self.webcams.get(webcam_slug)
        if webcam:
            return provider.get_image(webcam['url'])
        else:
            return None
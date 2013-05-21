import yaml

from moxie.core.service import Service

from .domain import Webcam


class WebcamsService(Service):

    def __init__(self, webcams_list):
        self.webcams = yaml.safe_load(open(webcams_list))

    def get_all_webcams(self):
        return [Webcam.from_yaml(k, v) for k, v in self.webcams.iteritems()]

    def get_still_image(self, webcam_slug):
        """Get an image for the given webcam
        :param webcam_slug: unique identifier of the webcam
        :return: tbd
        """
        pass

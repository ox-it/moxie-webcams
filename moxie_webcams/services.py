import yaml

from moxie.core.service import Service


class WebcamsService(Service):

    def __init__(self, webcams_list):
        self.webcams = yaml.safe_load(open(webcams_list))

    def get_all_webcams(self):
        return self.webcams

    def get_still_image(self, webcam_slug):
        """Get an image for the given webcam
        :param webcam_slug: unique identifier of the webcam
        :return: tbd
        """
        pass

from moxie.core.views import ServiceView
from moxie_webcams.services import WebcamsService


class Webcams(ServiceView):
    """Get a list of webcams available
    """

    def handle_request(self):
        service = WebcamsService.from_context()
        return service.get_all_webcams()


class StillImage(ServiceView):
    """Get an image for the given webcam
    """

    def handle_request(self, slug):
        """Get an image for the given webcam
        :param slug: unique identifier of the webcam
        :return: image (tbd)
        """
        service = WebcamsService.from_context()
        return service.get_still_image(slug)

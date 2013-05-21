from flask import request

from moxie.core.views import ServiceView, accepts
from moxie.core.exceptions import abort
from moxie.core.representations import HAL_JSON, JSON
from moxie_webcams.providers import WebcamProviderException

from moxie_webcams.services import WebcamsService
from moxie_webcams.representations import HALWebcamsRepresentation


class Webcams(ServiceView):
    """Get a list of webcams available
    """

    def handle_request(self):
        service = WebcamsService.from_context()
        return service.get_all_webcams()

    @accepts(HAL_JSON, JSON)
    def as_hal_json(self, webcams):
        return HALWebcamsRepresentation(webcams, request.url_rule.endpoint).as_json()


class StillImage(ServiceView):
    """Get an image for the given webcam
    """

    def handle_request(self, slug):
        """Get an image for the given webcam
        :param slug: unique identifier of the webcam
        :return: image (tbd)
        """
        service = WebcamsService.from_context()
        try:
            return service.get_still_image(slug)
        except WebcamProviderException:
            # TODO return appropriate header to try again soon
            return abort(503, body="An error has occured")

    @accepts('image/jpeg')
    def as_image(self, image):
        return image
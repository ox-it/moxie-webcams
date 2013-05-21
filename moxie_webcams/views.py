from moxie.core.views import ServiceView


class Webcams(ServiceView):
    """Get a list of webcams available
    """

    def handle_request(self):
        pass


class StillImage(ServiceView):
    """Get an image for the given webcam
    """

    def handle_request(self, slug):
        pass

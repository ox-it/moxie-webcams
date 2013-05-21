from flask import url_for, jsonify

from moxie.core.representations import Representation, HALRepresentation


class WebcamRepresentation(Representation):

    def __init__(self, webcam):
        self.webcam = webcam

    def as_json(self):
        return jsonify(self.as_dict())

    def as_dict(self):
        return {
            'slug': self.webcam.slug,
            'title': self.webcam.title,
            'description': self.webcam.description,
            'credit': self.webcam.credit,
        }


class HALWebcamRepresentation(WebcamRepresentation):

    def __init__(self, webcam, endpoint):
        """HAL+JSON representation of a webcam
        """
        super(HALWebcamRepresentation, self).__init__(webcam)
        self.endpoint = endpoint

    def as_json(self):
        return jsonify(self.as_dict())

    def as_dict(self):
        base = super(HALWebcamRepresentation, self).as_dict()
        representation = HALRepresentation(base)
        representation.add_link('self', url_for(self.endpoint, slug=self.webcam.slug))
        if self.webcam.poi:
            # TODO remove hardcoded endpoint for places
            representation.add_link('poi', url_for('places.poidetail', ident=self.webcam.poi))
        return representation.as_dict()


class HALWebcamsRepresentation(object):

    def __init__(self, webcams, endpoint):
        self.webcams = webcams
        self.endpoint = endpoint

    def as_json(self):
        return jsonify(self.as_dict())

    def as_dict(self):
        representation = HALRepresentation({})
        representation.add_embed('webcams', [HALWebcamRepresentation(w, 'webcams.webcam').as_dict()
                                             for w in self.webcams])
        representation.add_link('self', url_for('webcams.webcams'))
        return representation.as_dict()

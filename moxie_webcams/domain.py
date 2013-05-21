class Webcam(object):

    def __init__(self, slug, title, description, credit, url, poi=None):
        self.slug = slug
        self.title = title
        self.description = description
        self.credit = credit
        self.url = url
        self.poi = poi

    @staticmethod
    def from_yaml(slug, properties):
        return Webcam(slug, properties.get('title'),
                      properties.get('description'),
                      properties.get('credit'),
                      properties.get('url'),
                      properties.get('poi', None))
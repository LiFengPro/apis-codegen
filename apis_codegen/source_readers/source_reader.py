import json


class SourceReader(object):
    def __init__(self):
        self.source = None

    def read_from_json(self, filename, tag='swagger1.2'):
        pass



    def _read_from_swagger_1_2(self, source):
        """
        Args:
            source (dict)
        """

        for key, value in source.items():
            if key == 'models':
                pass



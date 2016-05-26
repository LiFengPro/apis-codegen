from apis_codegen.models.model import Property, Model
from apis_codegen.exceptions import ApisCodegenException


class Swagger12(object):

    TYPE_MAPPING = {
        'string': 'str',
        'integer': 'int',
        'long': 'int',
        'float': 'float',
        'double': 'float',
        'array': 'list',
        'map': 'dict',
        'boolean': 'bool',
        'date': 'date',
        'DateTime': 'datetime',
        'object': 'object',
        'file': 'file',
        'binary': 'str',
        'ByteArray': 'str',
        'UUID': 'str'
    }

    def read_models(self, models_dict):
        models = []
        for model_name, model_dict in models_dict.items():
            models.append(self._create_model(model_name, model_dict))
        models.sort()
        return models

    def _create_model(self, model_name, model_dict):
        if 'properties' not in model_dict:
            raise ApisCodegenException("Model {} doesn't have any properties".format(model_name))

        properties = []
        for property_name, property_dict in model_dict['properties'].items():
            properties.append(self._create_property(property_name, property_dict))
        properties.sort()

        model_kwargs = {}
        model_kwargs['name'] = model_name
        model_kwargs['properties'] = properties
        model_kwargs['extends'] = model_dict.get('extends', None)
        model_kwargs['description'] = model_dict.get('description', None)
        model_kwargs['id'] = model_dict.get('id', None)

        return Model(**model_kwargs)

    def _create_property(self, property_name, property_dict):
        property_kwargs = {}
        property_kwargs['name'] = property_name
        property_kwargs['type'] = self._convert_type(property_dict.get('type', None))
        property_kwargs['ref'] = property_dict.get('$ref', None)
        property_kwargs['description'] = property_dict.get('description', None)

        if property_kwargs['type'] == 'list':
            property_kwargs['items'] = {
                'type': self._convert_type(property_dict['items'].get('type', None)),
                'ref': property_dict['items'].get('$ref', None)
            }


        return Property(**property_kwargs)

    def _convert_type(self, original_type):
        if original_type:
            return Swagger12.TYPE_MAPPING[original_type]
        else:
            return None

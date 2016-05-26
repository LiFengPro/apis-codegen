from apis_codegen.source_readers.swagger_1_2 import Swagger12

class TestSwagger12(object):


    def test_read_models(self):
        reader = Swagger12()

        models_dict = {
        "A": {
            "id": "id_a",
            "description": "des_a",
            "properties": {
                "response": {
                    "type": "integer"
                },
                "version": {
                    "type": "string"
                }
            },
            "extends": ""
        },
        "B": {
            "id": "id_b",
            "description": "des_b",
            "properties": {
                "response": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "version": {
                    "type": "array",
                    "items": {
                        "$ref": "Version"
                    }
                }
            },
            "extends": "A"
        }}

        models = reader.read_models(models_dict)
        a = models[0]
        assert a.name == 'A'
        assert a.id == 'id_a'
        assert a.description == 'des_a'
        assert a.extends is None
        assert a.properties[0].name == 'response'
        assert a.properties[0].type == 'int'
        assert a.properties[1].name == 'version'
        assert a.properties[1].type == 'str'

        b = models[1]
        assert b.name == 'B'
        assert b.id == 'id_b'
        assert b.description == 'des_b'
        assert b.extends == 'A'
        assert b.properties[0].name == 'response'
        assert b.properties[0].type == 'list'
        assert b.properties[0].items['type'] == 'str'
        assert b.properties[1].name == 'version'
        assert b.properties[1].type == 'list'
        assert b.properties[1].items['ref'] == 'Version'

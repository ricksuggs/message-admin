from __future__ import unicode_literals

from tests import test_settings
from api.models import Base
from eve_sqlalchemy.tests import TestMinimal

SETTINGS = vars(test_settings)


class TestApi(TestMinimal):
    def setUp(self, url_converters=None):
        super(TestApi, self).setUp(SETTINGS, url_converters, Base)

    def bulk_insert(self):
        self.app.data.insert(
            "source",
            [
                {"name": "test_1"},
                {"name": "test_2"},
                {"name": "test_3"},
                {"name": "test_4"},
            ],
        )

    def test_get_source(self):
        
        response, status = self.get("source")
        self.assert200(status)
        sources = response["_items"]
        self.assertEqual(len(sources), 4)

        response, status = self.get(f"source/{sources[0]['id']}")
        self.assert200(status)
        name = response["name"]
        self.assertEqual(name, "test_1")


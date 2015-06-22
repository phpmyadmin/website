from django.test import TestCase
from files.models import Release


class ReleaseTest(TestCase):
    def test_version(self):
        self.assertEquals(
            Release.parse_version('1.2.3.1'),
            102030199
        )
        self.assertEquals(
            Release.parse_version('1.2.3'),
            102030099
        )
        self.assertEquals(
            Release.parse_version('1.2.3-rc1'),
            102030051
        )
        self.assertEquals(
            Release.parse_version('1.2.3-beta9'),
            102030019
        )
        self.assertEquals(
            Release.parse_version('1.2.3-alpha2'),
            102030002
        )

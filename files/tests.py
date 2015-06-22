from django.test import TestCase
from files.models import Release


class ReleaseTest(TestCase):
    def test_version(self):
        self.assertEquals(
            Release(version='1.2.3.1').parse_version(),
            102030199
        )
        self.assertEquals(
            Release(version='1.2.3').parse_version(),
            102030099
        )
        self.assertEquals(
            Release(version='1.2.3-rc1').parse_version(),
            102030051
        )
        self.assertEquals(
            Release(version='1.2.3-beta9').parse_version(),
            102030019
        )
        self.assertEquals(
            Release(version='1.2.3-alpha2').parse_version(),
            102030002
        )

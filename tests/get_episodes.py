import unittest

from AIO import AIO


class EpisodeTests(unittest.TestCase):
    def test_get_radio(self):
        e = AIO.getRadioEpisodes()
        for ep in e:
            assert ep['url'].startswith('https://media.focusonthefamily.com/')
        print(e)

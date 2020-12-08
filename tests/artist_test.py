import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Angel Olsen", 60)

    def test_artist_has_name(self):
        self.assertEqual("Angel Olsen", self.artist.name)
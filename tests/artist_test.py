import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Angel Olsen")

    def test_artist_has_name(self):
        self.assertEqual("Angel Olsen", self.artist.name)

    def test_artist_id_starts_none(self):
        self.assertEqual(None, self.artist.id)
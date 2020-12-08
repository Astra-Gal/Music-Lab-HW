import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album("Burn Your Fire For No Witness", "Indie folk", "Angel Olsen")

    def test_album_has_title(self):
        self.assertEqual("Burn Your Fire For No Witness", self.album.title)
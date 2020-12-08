import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album("Burn Your Fire For No Witness", "Indie folk", "Angel Olsen")

    def test_album_has_title(self):
        self.assertEqual("Burn Your Fire For No Witness", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Indie folk", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Angel Olsen", self.album.artist)

    def test_album_id_starts_as_none(self):
        self.assertEqual(None, self.album.id)
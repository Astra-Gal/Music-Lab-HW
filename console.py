import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_repository.delete_all()
album_repository.delete_all()

artist_1 = Artist ("Angel Olsen")
artist_repository.save(artist_1)

album_1 = Album ("Burn Your Fire For No Witness", "Indie folk", artist_1)
album_repository.save(album_1)

res = album_repository.select_all()
for album in res:
    print(album.__dict__)
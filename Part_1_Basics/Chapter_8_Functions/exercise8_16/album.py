def make_album(artist, album):
    """
    Return a disctionary of a music album.
    """
    music_album = {
        'artist': artist,
        'album': album
        }
    return music_album

def make_album2(artist, album, 
                num_track=None):
    """
    Return a dictionary of a music album.
    """
    music_album2 = {
        'artist': artist,
        'album': album
        }
    if num_track:
        music_album2['num_track'] = num_track
    return music_album2
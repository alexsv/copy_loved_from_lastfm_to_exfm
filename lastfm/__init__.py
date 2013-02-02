# coding=utf-8
"""
Last.fm wrappers.
"""

import pylast
from core import Track, Tracks

class LastFmClient():
    def __init__(self, api_key, api_secret, username):
        self.network = pylast.LastFMNetwork(
            api_key=api_key,
            api_secret=api_secret
        )
        self.user = pylast.User(user_name=username, network=self.network)

    def get_loved_tracks(self, **kwargs):
        return self.user.get_loved_tracks(kwargs)

    def get_library_tracks(self, **kwargs):
        return self.user.get_library().get_tracks(kwargs)


class LastFmTracks(Tracks, LastFmClient):
    """
    Last.fm track collection.
    """
    def __init__(self, options, **kwargs):
        super(LastFmTracks, self).__init__(**kwargs)
        self.collection = self.get_tracks(options)

    def __next__(self):
        raise NotImplementedError

    def get_tracks(self, options):
        """
        Abstract get track list.
        """
        raise NotImplementedError

    def _get_track(self):
        track = next(self)
        return Track(
            title=track.title,
            artist=track.artist.name if isinstance(track.artist, pylast.Artist) else track.artist
        )


class LastFmLovedTracks(LastFmTracks):
    def __init__(self, **kwargs):
        super(LastFmLovedTracks, self).__init__(**kwargs)

    def __next__(self):
        return next(self.collection).track

    def get_tracks(self, options):
        """
        Retrieve all loved tracks.
        """
        print("limit:", options['limit'])
        return self.get_loved_tracks(limit=options['limit'])

class LastFmLibraryTracks(LastFmTracks):
    def __init__(self, **kwargs):
        super(LastFmLibraryTracks, self).__init__(**kwargs)

    def __next__(self):
        return next(self.collection).item

    def get_tracks(self, options):
        """
        Retrieve all loved tracks.
        """
        print("limit:", options['limit'])
        return self.get_library_tracks(limit=options['limit'])
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify API credentials
client_id ='ae6b4bdab0004fdcb4eafab93c63dbf2'
client_secret = '305655ded0c244bfa65c8d6a8a1562fc'

# Authenticate with Spotify using Client Credentials Flow
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager, requests_timeout=10, retries=5)

def get_playlist_feats(playlist_ids):
    # Retrieve the songs, their features, and popularity from users' playlists
    # Initialize lists to store song information
    track_ids = []
    track_names = []
    artist_names = []
    track_popularity = []

    # Iterating over each playlist ID
    for playlist_id in playlist_ids:
        print(playlist_id)
        # Getting the playlist details
        source_playlist = sp.playlist(playlist_id)
        tracks = source_playlist["tracks"]
        songs = tracks["items"]
        # Extracting song information
        for i in range(0, len(songs)):
            song_id = songs[i]['track']['id']
            # Exclude duplicate tracks
            if song_id is not None and song_id not in track_ids:
                song_popularity = sp.track(song_id)['popularity']
                track_ids.append(song_id)
                track_names.append(songs[i]['track']['name'])
                artist_names.append(songs[i]['track']['artists'][0]['name'])
                track_popularity.append(song_popularity)

    # Retrieving audio features for the tracks
    audio_features_list = []
    for i in range(0, len(track_ids), 100):  # Process 100 tracks at a time
        batch = track_ids[i:i + 100]
        audio_features_results = sp.audio_features(batch)
        audio_features_list.extend(audio_features_results)

    # Convert audio features to DataFrame
    audio_features_df = pd.DataFrame(audio_features_list)

    # Preparing data for DataFrame
    data_list = []
    for i in range(len(track_ids)):
        audio_features_dict = {
            'artist_name': artist_names[i],
            'track_id': audio_features_df.loc[i, 'id'],
            'track_name': track_names[i],
            'acousticness': audio_features_df.loc[i, 'acousticness'],
            'danceability': audio_features_df.loc[i, 'danceability'],
            'duration_ms': audio_features_df.loc[i, 'duration_ms'],
            'energy': audio_features_df.loc[i, 'energy'],
            'instrumentalness': audio_features_df.loc[i, 'instrumentalness'],
            'key': audio_features_df.loc[i, 'key'],
            'liveness': audio_features_df.loc[i, 'liveness'],
            'loudness': audio_features_df.loc[i, 'loudness'],
            'mode': audio_features_df.loc[i, 'mode'],
            'speechiness': audio_features_df.loc[i, 'speechiness'],
            'tempo': audio_features_df.loc[i, 'tempo'],
            'time_signature': audio_features_df.loc[i, 'time_signature'],
            'valence': audio_features_df.loc[i, 'valence'],
            'popularity': track_popularity[i]
        }
        data_list.append(audio_features_dict)

    # Create DataFrame from collected data and save to CSV
    data_df = pd.DataFrame(data_list, index=track_ids)
    data_df.to_csv('SpotifyDataset.csv', index=False, header=True)

# Define the array with the playlist IDs
playlist_links = [
    '37i9dQZEVXbNG2KDcFcKOF', #2024A
    '37i9dQZEVXbMDoHDwVN2tF', #2024B
    '37i9dQZF1DX18jTM2l2fJY', #2023
    '56r5qRUv3jSxADdmBkhcz7', #2022
    '37i9dQZF1DWTqOsMG7SsUt', #2021
    '37i9dQZF1DX7Jl5KP2eZaS', #2020
    '37i9dQZF1DWVRSukIED0e9', #2019
    '37i9dQZF1DXe2bobNYDtW8', #2018
    '37i9dQZF1DWTE7dVUebpUW', #2017
    '37i9dQZF1DX8XZ6AUo9R4R', #2016
    '37i9dQZF1DX9ukdrXQLJGZ', #2015
    '37i9dQZF1DX0h0QnLkMBl4', #2014
    '37i9dQZF1DX3Sp0P28SIer', #2013
    '37i9dQZF1DX0yEZaMOXna3', #2012
    '37i9dQZF1DXcagnSNtrGuJ', #2011
    '37i9dQZF1DXc6IFF23C9jj', #2010
    '37i9dQZF1DX4UkKv8ED8jp', #2009
    '37i9dQZF1DWYuGZUE4XQXm', #2008
    '37i9dQZF1DX3j9EYdzv2N9', #2007
    '37i9dQZF1DX1vSJnMeoy3V', #2006
    '37i9dQZF1DWWzQTBs5BHX9', #2005
    '37i9dQZF1DWTWdbR13PQYH', #2004
    '37i9dQZF1DXaW8fzPh9b08', #2003
    '37i9dQZF1DX0P7PzzKwEKl', #2002
    '37i9dQZF1DX9Ol4tZWPH6V', #2001
    '37i9dQZF1DWUZv12GM5cFk', #2000
    '37i9dQZF1DX4PrR66miO50', #1999
    '37i9dQZF1DWWmGB2u14f8m', #1998
    '37i9dQZF1DWWKd15PHZNnl', #1997
    '37i9dQZF1DWZkDl55BkJmo', #1996
    '37i9dQZF1DXayIOFUOVODK', #1995
    '37i9dQZF1DXbKFudfYGcmj', #1994
    '37i9dQZF1DXbUFx5bcjwWK', #1993
    '37i9dQZF1DX9ZZCtVNwklG', #1992
    '37i9dQZF1DX6TtJfRD994c', #1991
    '37i9dQZF1DX4joPVMjBCAo', #1990
    '37i9dQZF1DX4qJrOCfJytN', #1989
    '37i9dQZF1DX3MZ9dVGvZnZ', #1988
    '37i9dQZF1DX38yySwWsFRT', #1987
    '37i9dQZF1DX7b12kdMQTpG', #1986
    '37i9dQZF1DWXZ5eJ1sVtmf', #1985
    '37i9dQZF1DX2O7iyPnNKby', #1984
    '37i9dQZF1DXbE3rNuDfpVj', #1983
    '37i9dQZF1DXas7qFgKz9OV', #1982
    '37i9dQZF1DX3MaR62kDrX7', #1981
    '37i9dQZF1DWXbLOeOIhbc5', #1980
    '37i9dQZF1DWZLO9LcfSmxX', #1979
    '37i9dQZF1DX0fr2A59qlzT', #1978
    '37i9dQZF1DX26cozX10stk', #1977
    '37i9dQZF1DX6rhG68uMHxl', #1976
    '37i9dQZF1DX3TYyWu8Zk7P', #1975
    '37i9dQZF1DWVg6L7Yq13eC'  #1974
]

# Call the function to fetch playlist features
get_playlist_feats(playlist_links)
print("done")
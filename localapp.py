# Sample Python code for user authorization

import os
import csv
from pathlib import Path

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# List of Channels to adds
test_list = ['PLwg4AG1KkgLxZ2RPuELOONAszjFfv5DvT', 'UUkyfHZ6bY2TjqbJhiH8Y2QQ']
discovery_channel = list(set(['UU6107grRI4m0o2-emgoDnAA', 'UUX6b17PVsYBQ0ip5gyeme-Q', 'UUzR-rom72PHN9Zg7RML9EbA', 'UUZYTClx2T1of7BRZ86-8fow', 'UUrMePiHCWG4Vwqv3t7W9EFg', 'UU2C_jShtL725hvbm1arSV9w', 'UUHnyfMqiRRG1u-2MsSQLbXA', 'UUsXVk37bltHxD1rDPwtNM8Q', 'UUUHW94eEFW7hkUMVaZz4eDg', 'UUeiYXex_fwgYDonaTcSIk6w', 'UUtwKon9qMt5YLVgQt1tvJKg', 'UUoxcjq-8xIDTYp3uz647V5A', 'UUtESv1e7ntJaLJYKIO1FoYw', 'UUuPgdqQKpq4T4zeqmTelnFg', 'PLwg4AG1KkgLxZ2RPuELOONAszjFfv5DvT', 'UUkyfHZ6bY2TjqbJhiH8Y2QQ', 'UUmmPgObSUPw1HL2lq6H4ffA', 'UUivA7_KLKWo43tFcCkFvydw', 'UU-3SbfTPJsL8fJAPKiVqBLg', 'UU4K10PNjqgGLKA3lo5V8KdQ', 'UUt_t6FwNsqr3WWoL6dFqG9w', 'UUkxMlA7rt-mnIc1AjbyAsPw', 'UUX6b17PVsYBQ0ip5gyeme-Q', 'UUFqaprvZ2K5JOULCvr18NTQ', 'UUabaQPYxxKepWUsEVQMT4Kw', 'UUwTZ-JLF5FQ3EmQ2nPaS-lg', 'UU1ZBQ-F-yktYD4m5AzM6pww', 'UU9RM-iSvTu1uPJb8X5yp3EQ', 'UUHdluULl5c7bilx1x1TGzJQ', 'UUK09g6gYGMvU-0x1VCF1hgA', 'UUUcyEsEjhPEDf69RRVhRh4A', 'UUlfEht64_NrzHf8Y0slKEjw', 'UU22BdTgxefuvUivrjesETjg', 'UUE1jXbVAGJQEORz9nZqb5bQ', 'UU510QYlOlKNyhy_zdQxnGYw', 'UUvPXiKxH-eH9xq-80vpgmKQ', 'UUR1IuLEqb6UEA_zQ81kwXfg', 'UUlqhvGmHcvWL9w3R48t9QXQ', 'UUMOqf8ab-42UUQIdVoKwjlQ', 'UUQMyhrt92_8XM0KgZH6VnRg', 'UUX34tk-noBVC4WVC9qQGyMw', 'UUnbvPS_rXp4PC21PG2k1UVg', 'PLqq4LnWs3olUpaD8oXCF7IlLikGBY7HFg', 'dncYbSIjJIo&list=UUELt4nocnWDEnYJmov4zqyA']))
comic_channel = list(set(['UU4kjDjhexSVuC8JWk4ZanFw', 'UUmA-0j6DRVQWo4skl8Otkiw', 'UUKxQmKgrkUv4S7P5w0pLayw', 'UU20DNxT_UjT49mYOIocJAww', 'UUPnpVfa6XNHv4P1JxGFSDrQ', 'UUV2J1eTpFClb0-OPz8_QGQQ', 'UUURz5rKDgt7YibUSageNhEw', 'UUDiFRMQWpcp8_KD4vwIVicw', 'UUkDSAQ_5-yx5hmuvUcsJL7A']))
interior = ['https://www.youtube.com/channel/UCXvzpK4eKUJysEZ42zjTUdw','https://www.youtube.com/channel/UCq6H4g9eVY9WxoboCFd0iRA','https://www.youtube.com/user/HGTV']

# CONSTANTS
PLAYLIST_LENGTH = 500
CHANNEL_LIMIT = 150 #number of videos to take from a single channel

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

# csv file url -> listof channel urls
# takes a csv file and returns a list of channel urls
def csv_to_channels_list(csv_name):
    channel_urls = []
    with open(csv_name, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            channel_urls.append(row['URL'])
    return channel_urls

# channel url -> channel uploads playlist id
def get_channel_playlist(channel_url):
    start = channel_url.find('playlist?list=')
    if start > -1:
        start = start + 14
        return channel_url[start:]
    start = channel_url.find('/channel/')
    if start > -1:
        start = start + 9
        channel_info = youtube.channels().list(
        part='snippet,contentDetails',
        id=channel_url[start:]
        ).execute()
        return channel_info['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    start = channel_url.find('/user/')
    if start > -1:
        start = start + 6
        channel_info = youtube.channels().list(
        part='snippet,contentDetails',
        forUsername=channel_url[start:]
        ).execute()
        return channel_info['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# listof channel urls -> list of channel playlist ids
# takes a list of channel urls and returns a list of all the channels uploads playlist ids
def channels_to_playlists(channel_list):
    print('Converting Channel Urls to Playlist IDs. ', end='')
    playlist_ids = []
    for channel in channel_list:
        try:
            playlist_ids.append(get_channel_playlist(channel))
        except:
            print('\nError with channel: {}'.format(channel))
            pass
    print('DONE')
    return list(set(playlist_ids))


# playist id -> list of video_ids
def get_playlist_items(playlist_id):
    # Retrieve the list of videos uploaded to the authenticated user's channel.
    playlistitems_list_request = youtube.playlistItems().list(
    playlistId=playlist_id,
    part='snippet',
    maxResults=50
    )
    video_ids = []

    while playlistitems_list_request and (len(video_ids) < CHANNEL_LIMIT):
        playlistitems_list_response = playlistitems_list_request.execute()

        # Print information about each video.
        for playlist_item in playlistitems_list_response['items']:
            video_ids.append(playlist_item['snippet']['resourceId']['videoId'])
            # title = playlist_item['snippet']['title']
            # video_id = playlist_item['snippet']['resourceId']['videoId']
            # print('{} ({})'.format(title, video_id))

            playlistitems_list_request = youtube.playlistItems().list_next(
            playlistitems_list_request, playlistitems_list_response)

    return video_ids

# listof playlist ids -> (listof (listof video ids))
# takes a list fo playlist ids and returns a list of list of video ids
def get_all_playlists(playlist_ids):
    print('Getting Channel Videos: {} Channels. '.format(len(playlist_ids)), end='', flush=True)
    all_video_ids = []

    for playlist in playlist_ids:
        all_video_ids.append(get_playlist_items(playlist))
        print('{} '.format(len(all_video_ids)), end='', flush=True)

    print('DONE')
    return all_video_ids

# playlist name -> playlist id
# creates a playlist with playlist_name and returns the playlist id
def make_playlist(playlist_name):
    print('Making Playlist.', end='')
    playlist_insert_response = youtube.playlists().insert(
        part = 'snippet',
        body = {'snippet':{'title':playlist_name}}
    ).execute()
    print('Playlist ID {}. DONE'.format(playlist_insert_response['id']))
    return playlist_insert_response['id']

# video id, playlist id -> adds video to playlist
def add_video_to_playlist(video_id, playlist_id):
    add_video_response = youtube.playlistItems().insert(
    part = 'snippet',
    body = dict(
            snippet=dict(
                playlistId=playlist_id,
                resourceId=dict(
                    videoId=video_id,
                    kind='youtube#video'
                )))
    ).execute()

# list of videos, playlist id -> adds videos to playlist
# takes a list of video ids and a playlist id and adds all videos to playlist
def add_all_to_playlist(video_list, playlist_id):
    print('Adding {} Videos to New Playlist. '.format(len(video_list)), end='', flush=True)
    counter = 0
    for video in video_list:
        try:
            add_video_to_playlist(video, playlist_id)
        except:
            print('couldnt add video')
        counter = counter + 1
        if(counter % (len(video_list) // 10)) == 0:
            print('{} '.format(counter), end='', flush=True)
    print('DONE')

# all_lists -> blendedlist
# take all lists and returns a blended list
def merge_lists(all_lists):
    print('Merging Playlists. ', end='')
    result = []
    counter = 0
    empty_counter = True
    while empty_counter and (len(result) < PLAYLIST_LENGTH):
        empty_counter = False
        for single_list in all_lists:
            try:
                result.append(single_list[counter])
                empty_counter = True or empty_counter
            except:
                empty_counter = False or empty_counter
        counter = counter + 1
    print('DONE')
    return result

# dict channel_name,csv -> ...
def make_channels(path_folder):
    pathlist = Path(path_folder).glob('*.csv')
    for path in pathlist:
        # because path is object not string
        print(str(path))
    return []


# main program flow
def app(playlist_name, channel_csv):
    channel_list = csv_to_channels_list(channel_csv)
    playlist_ids = channels_to_playlists(channel_list)
    new_playlist = make_playlist(playlist_name)
    add_all_to_playlist(merge_lists(get_all_playlists(playlist_ids)), new_playlist)
    return 1

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  # youtube = get_authenticated_service()
  # app('Cartoons Channel', 'channels/animations.csv')
  make_channels('channels/')

'''
FILE:           playlist_handlers.py
DATE:           24-03-2024
AUTHOR:         Gavin Sereg
DESCRIPTION:    This holds the handlers for the playlist_program.py
'''

from user_input import get_number, get_string
from playlist_helpers import show_message, draw_table, show_section_title
import playlist_data

def add(title):
    '''
    Handles all of the logic for adding a new playlist
    '''
    show_section_title(title)
    playlist = get_playlist_data()
    playlist_data.store_playlist(playlist)

def show_all(title):
    '''
    Handles all of the logic for showing all playlist records
    '''
    show_section_title(title)
    playlists = playlist_data.get_playlist_list()
    if len(playlists) == 0:
        show_message("There are no playlist records", "warning")
    else:
        show_playlist_table(playlists)

def delete(title):
    '''
    Handles all of the logic for deleting a playlist
    '''
    show_section_title(title)
    playlist_prompt = "ID of playlist to delete"
    show_all()
    playlists = playlist_data.get_playlist_list
    playlist = get_number(playlist_prompt)
    for i in range(len(playlists)):
        if playlist in playlists:
            playlists.pop(playlist)
        elif playlist not in playlists:
            show_message("Playlist not found")

def get_playlist_data():
    '''
    Asks the user for playlist data and returns the data as a list

    Record Format:
        playlist ID, author, playlist name, genre

    RETURNS
        list A list representing a playlist record
    '''
    playlist_ID_prompt = "Playlist ID"
    author_prompt = "First and last name"
    playlist_name_prompt = "Playlist name"
    genre_prompt = "What genre"

    playlist_ID = get_number(playlist_ID_prompt, True)
    author = get_string(author_prompt)
    playlist_name = get_string(playlist_name_prompt)
    genre = get_string(genre_prompt)

    playlist = [playlist_ID, playlist_name, author, genre]
    return playlist
    
def show_playlist_table(playlists: list):
    '''
    Displays a list of playlist records as a table. If there are no records, i.e: The list is empty, then the function
    displays a message stating a warning
    '''
    
    column_defs = [(5, "center"), (30, "left"), (20, "left"), (20, "left")]
    headers = ["ID", "Playlist Name", "Author", "Genre"]
    draw_table(column_defs, headers, playlists)
'''
FILE:           playlist_data.py
DATE:           24-03-2024
AUTHOR:         Gavin Sereg
DESCRIPTION:    This file holds all of the data functions and global variables for all files
'''

playlist_list = []

def store_playlist(playlist: list):
    '''
    Appends the playlist record to the playlist_list

    INPUTS:
        playlist a list representing the playlist record
    '''
    playlist_list.append(playlist)

def get_playlist_list() -> list:
    '''
    Returns the main list of playlist records

    RETURNS:
        list A list of playlist records
    '''
    return playlist_list

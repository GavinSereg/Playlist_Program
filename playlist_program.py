'''
FILE:           playlist_program.py
DATE:           24-03-2024
AUTHOR:         Gavin Sereg
DESCRIPTION:    This is the main file for the playlists. This is the menu for adding, showing all, and deleting playlists
'''

import playlist_handlers
from playlist_helpers import (show_program_title, get_choice, 
                              show_message, confirm_quit, show_menu_error, 
                              press_enter_key_to_continue)

VERSION = "1.0.0"

"""-----------------------------------------------------------------------------------"""
"""-----------------------------------MAIN FUNCTION-----------------------------------"""
"""-----------------------------------------------------------------------------------"""

def main():
    do_program_logic()

"""------------------------------------------------------------------------------------"""
"""-----------------------------------LOGIC FUNCTION-----------------------------------"""
"""------------------------------------------------------------------------------------"""

def do_program_logic():
    '''
    Displays a menu in a loop, responding to the
    users inputs until the user chooses to quit
    '''
    main_menu_title = "Main Menu"
    main_menu_options = ["Add a playlist", "Show all playlists", "Delete a Playlist", "Quit"]
    menu_prompt = "Your choice"
    error_response = "Your choice was not recognized. Please try again."
    program_complete = "Program complete"

    show_program_title()

    done = False
    while not done:

        choice = get_choice(main_menu_title, main_menu_options, menu_prompt)
        show_message()
        
        if choice == 1:
            playlist_handlers.add(main_menu_options[0])
        elif choice == 2:
            playlist_handlers.show_all(main_menu_options[1])
        elif choice == 3:
            playlist_handlers.delete(main_menu_options[2])
        elif choice == 4:
            done = confirm_quit()
            if done:
                break
            else:
                continue
        else:
            show_menu_error(error_response)
        
        press_enter_key_to_continue()
    
    show_message(f'\n{program_complete}\n')

if __name__ == "__main__":
    main()
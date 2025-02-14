'''
FILE:           playlist_helpers.py
DATE:           24-03-2024
AUTHOR:         Gavin Sereg
DESCRIPTION:    This file helps display tables and certain things
'''

from user_input import get_string, get_number

CONSOLE_WIDTH = 80

def show_program_title():
    """
    Displays the formatted program title

    INPUTS:
        title A string containing the title of the program
        width An int with the screen width for display in characters
    """
    program_title = "*** Employee Program ***"
    show_message(f"\n{program_title:^{CONSOLE_WIDTH}s}")

def show_section_title(title):
    """
    Displays a section title

    INPUTS:
        title A string with title of the section 
    """
    show_message(f"{'-- ' + title + ' --':^{CONSOLE_WIDTH}s}")

def show_message(message = "", type = ""):
    """
    Displays a message

    INPUTS:
        message A string with the text to display
    """
    if type != "":
        print(f"\n{type.upper()}:", end=" ")
    print(message)

def press_enter_key_to_continue():
    """
    Displays a message instructing the user to press 
    the Enter key and then waits until they do
    """
    press_enter = "Press the Enter key to continue..."
    input(f"\n{press_enter}")

def show_menu_error(message):
    """
    Displays the error message and then requests that 
    the user press Enter to continue
    
    INPUTS:
        message A string with the error message
    """
    show_message(message, "error")

def confirm_quit():
    """ 
    Displays a message stating that the user has chosen 
    to quit. Then asks the user to confirm the desire 
    to quite by entering Y&nbsp;

    RETURNS:
        boolean True if the user confirms the quit, and False otherwise
    """
    choice = get_string("Confirm quit (Y/N)")
    return choice.lower() == 'y'

def get_choice(title, options, prompt):
    """
    Displays a menu and prompts the user for an option

    RETURNS:
        string The user's option as a string
    """ 
    show_menu(title, options)
    choice = get_number(prompt)
    return choice

def show_menu(menu_title, options):
    """
    Displays the menu title and then displays the menu 
    options, one per line

    INPUTS:
        menu_title A string with the name of the menu
        options A list of strings with the options for the menu
    """
    show_section_title(menu_title)
    for i in range(1, len(options) + 1):
        show_message(f"{i}.\t{options[i - 1]}")
    show_message("")



"""------------------------------------------------------------------------------------"""
"""-----------------------------------TABLE FUNTIONS-----------------------------------"""
"""------------------------------------------------------------------------------------"""



def draw_table(column_defs: list, headers: list, data: list):
    """
    Draws a text-based table with the provided table.

    Note that the first two lists and the sublists of the third list must all 
    be the same size

    INPUTS:
        column_defs A list of tuples with column width and alignment
        headers A list of strings with the text of the column headers
        data A list of lists where each sublist is a record to be displayed
    """
    # determine the width of the table
    bar_size = 0
    for col in column_defs:
        bar_size += col[0]
    bar_size += len(headers) + 1  # for the vertical bars
    # print the top bar
    print('')
    draw_bar(bar_size, '-')
    # Draw the table header
    print('| ', end='')
    for i in range(len(column_defs)):
        draw_column(column_defs[i][0] - 2, headers[i], 'center')
        print(' | ', end='')
    print('')
    draw_bar(bar_size, '-')
    # Draw the table data
    for datum in data:
        print('| ', end='')
        for i in range(len(datum)):
            draw_column(column_defs[i][0] - 2, datum[i], column_defs[i][1])
            print(' | ', end='')
        print('')
        draw_bar(bar_size, '-')

def draw_column(width, value, direction):
    """
    Builds a string for a column and then prints without a newline.

    INPUTS:
        width   The field width of the column
        value   The value to display
        direction   The alignment
    """
    # determine the alignment
    align = '<'
    if direction == 'center':
        align = '^'
    elif direction == 'right':
        align = '>'
    # Build the string
    out = f'{value:{align}{width}}'
    # display the output
    print(out, end='')

def draw_bar(bar_size, bar_character):
    """
    Displays a horizontal line of the specified character.

    INPUTS:
        bar_size The width of the line in characters
        bar_character The character to use for the bar
    """
    bar = bar_character * bar_size
    print(bar)
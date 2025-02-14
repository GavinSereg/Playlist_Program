'''
FILE:           user_input.py
DATE:           24-03-2024
AUTHOR:         Gavin Sereg
DESCRIPTION:    This file holds functions for getting user input
'''

def get_string(prompt):
    """
    Displays the prompt requesting string input from the 
    user and then returns the string that is entered with 
    any leading or trailing white space characters removed

    INPUTS:
        prompt A string with the instructions for the user

    RETURNS:
        string The string entered by the user with whitespace stripped.
    """
    return input(prompt + ": ").strip()

def get_number(prompt: str, must_be_int: bool = False) -> float:
    """
    Accepts a required prompt (a string) and an optional must_be_int (a boolean)
    Returns the value entered (a number)
    """
    while(True):
        try:
            value = float(input(prompt + ": "))
            if (must_be_int and not value.is_integer()):
                print("Decimals are not allowed", end=", ")
                raise ValueError
            break
        except ValueError:
            print("invalid input")
    if (value.is_integer()):
        value = int(value)
    return value

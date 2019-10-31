import os


def clear():
    """
    console clear for the correct os
    """
    if os.name == "nt":
        os.system('cls') #on Windows System
    else:
        os.system('clear')
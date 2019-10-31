from utils.clear import clear

def menu(args):
    """
    docstring
        it ask the menu item to the cust and return it's choice if it's a right choice
    """
    clear()
    menu = args
    print("choose an option => ")
    print(menu)
    userInpt = input()

    while not userInpt in menu:
        print("Invalid argument")
        print("choose an option => ")
        print(menu)
        userInpt = input()
    
    return userInpt

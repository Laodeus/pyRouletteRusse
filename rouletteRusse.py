from menu.menu import menu
from utils.clear import clear
from quit.quit import quiting
from credit.credit import credit

while 1:
    action = menu(["play","credit","quit"])

    if action == "play":
        print("play")
    elif action == "credit":
        credit()
    elif action == "quit":
        quiting()
    else:
        print("Sometings goes wrong with the menu :/")
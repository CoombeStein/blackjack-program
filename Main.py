import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")
root = ctk.Ctk()


cards_values = {
    "A":11,
    "K":10,
    "Q":10,
    "j":10,
    "10":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2,
        }

player_cards=input("what cards does the player have \n(remember to leve a space between cards)\n:")
dealer_card=input("what card is the dealer showing :")


root.mainloop()
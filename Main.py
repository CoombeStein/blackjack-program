import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

#dictionary of all the cards values in a deck
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

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.total_player_score = 0
        self.total_dealer_score = 0 
        
        root = ctk.CTk()
        root.geometry('400x240')

        # asking user to input player cards
        player_card_label = ctk.CTkLabel(root, text="What cards do you have?\n remember"
            "to awnser with only the\n number or first letter of the card")
        player_card_label.pack()
        player_cards = ctk.CTkEntry(root, placeholder_text="eg: A 7")
        player_cards.bind('<Return>', self.add_score)
        player_cards.pack()

        #asking user to input dealer cards
        dealer_card_label= ctk.CTkLabel(root,text="What card does yhe dealer have?\n"
            " remember to awnser with only the\n number or first letter of the card")
        dealer_card_label.pack()
        dealer_cards = ctk.CTkEntry(root, placeholder_text="eg: A 7")
        dealer_cards.pack()

        root.mainloop()
    
    def add_score(self, event):
        player_score = event.widget.get().split()
        for word in player_score:
            if word.upper() in cards_values:
                self.total_player_score = self.total_player_score + cards_values[word.upper()]
                print(self.total_player_score)

if __name__ == "__main__":
    App()

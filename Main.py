import customtkinter as ctk

ctk.set_appearance_mode("dark")
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
    total_player_score = 0
    total_dealer_score = 0 
    def __init__(self):
        super().__init__()

        root = ctk.CTk()
        root.geometry('330x560')

        # asking user to input player cards
        player_card_label = ctk.CTkLabel(root, text="What cards do you have?\n remember "
            "to awnser with only the\n number or first letter of the card",font=("arial",20))
        player_card_label.pack()
        
        self.player_cards = ctk.CTkEntry(root, placeholder_text="eg: A 7")
        self.player_cards.pack()

        #asking user to input dealer cards
        dealer_card_label= ctk.CTkLabel(root,text="What card does the dealer have?\n"
            " remember to awnser with only the\n number or first letter of the card", font=("arial",20))
        dealer_card_label.pack()
       
        self.dealer_cards = ctk.CTkEntry(root, placeholder_text="eg: A 7")
        self.dealer_cards.pack()

        enter_button = ctk.CTkButton(root,text="Enter",command=self.hit_or_stand)
        enter_button.pack(pady=20)

        root.mainloop()

    def hit_or_stand(self):
        player_score = self.player_cards.get().split()
        for word in player_score:
            if word.upper() in cards_values:
                self.total_player_score = self.total_player_score + cards_values[word.upper()]
                
        dealer_score = self.dealer_cards.get().split()
        for word in dealer_score:
            if word.upper() in cards_values:
                self.total_dealer_score = cards_values[word.upper()]

        
        
        #if player has 17 or more always stand
        if self.total_player_score >= 17 :
            print("stand")
        #if player has 11 or less always hit
        elif self.total_player_score <= 11:
            print("hit")

        #if player has 12, hit if dealer has 3 or less or 7 or more,
        # otherwise stand
        elif self.total_player_score == 12:
            if self.dealer_score <= 3:
                print("hit")
            elif self.dealer_score >=7:
                print("hit")
            else:
                print("stand")

        #if player has 16 or less, hit if dealer has 7 or more, otherwise stand
        elif self.total_player_score <=16:
            if self.total_dealer_score >=7:
                print("hit")
            else:
                print("stand")
        else:
            print("stand")
                                                    
if __name__ == "__main__":
    App()



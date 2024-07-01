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
        self.root = ctk.CTk()
        self.root.geometry('330x560')
        # asking user to input player cards

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both",expand=1)

        player_card_label = ctk.CTkLabel(self.main_frame, text="What cards "
                                          "do you have? ",font=("arial",20))
        player_card_label.pack()
        player_card_label.pack(pady=20)

        player_help_label = ctk.CTkLabel(self.main_frame,text="remember to awnser with"
            " only the\n number or first letter of the card",font=("arial",10))
        player_help_label.pack()
        
        self.player_cards = ctk.CTkEntry(self.main_frame, placeholder_text="eg: A 7",
            width=190, height=45)
        self.player_cards.pack(pady=20)
        #asking user to input dealer cards
        dealer_card_label= ctk.CTkLabel(self.main_frame,text="What card does the dealer "
            "have?", font=("arial",20))
        dealer_card_label.pack(pady=20)
        
        dealer_help_label=ctk.CTkLabel(self.main_frame,text="remember to awnser with only"
            "the\n number or first letter of the card",font=("arial",10))
        dealer_help_label.pack()
       
        self.dealer_cards = ctk.CTkEntry(self.main_frame, placeholder_text="eg: A 7",
            width=190, height=45)
        self.dealer_cards.pack(pady=20)

        enter_button = ctk.CTkButton(self.main_frame,text="Enter", width=160, height=40
            ,command=self.hit_or_stand)
        enter_button.pack(pady=20)

        self.root.mainloop()
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
            self.stand()
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
                self.stand()
        #if player has 16 or less, hit if dealer has 7 or more, otherwise stand
        elif self.total_player_score <=16:
            if self.total_dealer_score >=7:
                print
            else:
                self.stand()
        else:
            self.stand()
    
    def stand(self):
        self.main_frame.destroy()
        self.stand_frame = ctk.CTkFrame(self.root)
        self.stand_frame.pack(fill="both", expand=1)

        self.player_stand = ctk.CTkLabel(self.stand_frame,text="Stand",font=(""
                                            "arial",40))
        self.player_stand.pack(pady=80)

        self.return_button = ctk.CTkButton(self.stand_frame,text="would"
                " you like to go again?", width=160, height=40)
        self.return_button.pack()
    
    def hit(self):
        self.main_frame.destroy()
        self.hit_frame = ctk.CTkFrame(self.root)
        self.hit_frame.pack(fill="both",expand=1)

        self.player_hit=ctk.CTKlabel(self.hit_frame, text="Hit", font=("arial",40))
        self.player_hit.pack(pady=80)


if __name__ == "__main__":
    App()

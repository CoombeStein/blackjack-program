import customtkinter as ctk, copy
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
#dictionary of all the cards values in a deck
cards_values = {
    "A":11,
    "K":10,
    "Q":10,
    "J":10,
    "10":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2,
    "1":1,
    
}


cards_list = list(cards_values.keys())
print(cards_list)

class App(ctk.CTk):
    total_player_score = 0
    total_dealer_score = 0 


    player_cards = []
    dealer_cards = []
    player_cards_list = []
    dealer_cards_list = []

    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        self.root.geometry('330x560')
        self.start()
        self.root.mainloop()
        self.value_inside = ctk.StringVar(self.root)
        self.value_inside.set("Select an Option")

    def start(self):
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
        
        self.player_card_1 = ctk.CTkOptionMenu(self.main_frame,values=list(cards_values))
        self.player_card_1.pack(pady=20)
        self.player_card_2 = ctk.CTkOptionMenu(self.main_frame,values=list(cards_values))
        self.player_card_2.pack(pady=20)
        self.player_cards = [self.player_card_1.get(), self.player_card_2.get()]

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

        enter_button = ctk.CTkButton(self.main_frame,text="Enter", width=190, height=45,
            command=lambda: self.hit_or_stand(self.player_cards))
        enter_button.pack(pady=20)

    def hit_or_stand(self, player_cards):
        print("called hit or stand")
        # old way
        # player_score = p_cards.get().split()

        for card in player_cards:
            self.player_cards_list.append(card.lower())

        for card in self.player_cards_list:
            if card.upper() in cards_values:
                self.total_player_score = self.total_player_score + cards_values[card.upper()]

        if not self.dealer_cards_list:
            self.previous_dealer_cards = copy.deepcopy(self.dealer_cards_list)          

        dealer_score = self.dealer_cards_list or self.previous_dealer_cards
        for card in dealer_score:
            if card.upper() in cards_values:
                self.total_dealer_score = cards_values[card.upper()]
        if self.total_player_score >= 21:
            print("bust")
        
        # if player has over 21 it will update players total score
        if self.total_player_score > 21:
            self.ace_21()
            
        #if player has 17 or more always stand
        if self.total_player_score >= 17 :
            self.stand()
            print("called 1")
        #if player has 11 or less always hit
        elif self.total_player_score <= 11:
             self.hit()
             print("called 2")
        #if player has 12, hit if dealer has 3 or less or 7 or more,
        # otherwise stand
        elif self.total_player_score == 12:
            if self.total_dealer_score <= 3:
                 self.hit()
                 print("called 3")
            elif self.total_dealer_score >=7:
                self.hit()
                print("called 4")
            else:
                self.stand()
                print("called 5")
        #if player has 16 or less, hit if dealer has 7 or more, otherwise stand
        elif self.total_player_score <=16:
            if self.total_dealer_score >=7:
                 self.hit()
                 print("called 6")
            else:
                self.stand()
                print("called 7")
        else:
            self.stand()
            print("called 8")
    
    def restart(self):
        self.frame_2.destroy()
        self.start()
    
    def return_button_function(self, parent, callback):
        self.return_button = ctk.CTkButton(parent,text="would"
                " you like to go again?",width=190, height=45,
                command=callback)
        self.return_button.pack()

    def delete_result_frame(self):
        if hasattr(self, 'frame_2'):
            self.frame_2.destroy()
    
    def stand(self):
        self.delete_result_frame()
        self.main_frame.destroy()
        self.frame_2 = ctk.CTkFrame(self.root)
        self.frame_2.pack(fill="both", expand=1)
        self.player_stand = ctk.CTkLabel(self.frame_2,text="Stand",font=(""
                                            "arial",40))
        self.player_stand.pack(pady=80)
        self.return_button_function(self.frame_2, self.restart)
         
        self.total_dealer_score = 0
        self.total_player_score = 0

        self.player_cards_list = []
        self.dealer_cards_list = []

    def hit(self):
        self.delete_result_frame()
        self.main_frame.destroy()
        self.frame_2 = ctk.CTkFrame(self.root)
        self.frame_2.pack(fill="both",expand=1)
        self.player_hit=ctk.CTkLabel(self.frame_2, text="Hit", font=("arial",40))
        self.player_hit.pack(pady=80)
        self.player_hit_entry=ctk.CTkOptionMenu(self.frame_2,values=list(cards_values))
        self.player_hit_entry.pack(pady=20)

        enter_button_2 = ctk.CTkButton(self.frame_2,text="Enter", width=190, height=45
            ,command=lambda: self.hit_or_stand(list(self.player_hit_entry.get())))
        enter_button_2.pack(pady=20)

        self.return_button_function(self.frame_2, self.restart)


# we was doinhg someweird shit with aces idk
    def ace_21(self):
        print(f'before {self.player_cards_list}')
        for card_data in enumerate(self.player_cards_list):
            index, card = list(card_data)
            if card.upper() == "A":
                self.player_cards_list[index] = str(cards_values['1'])
                print(f'after {self.player_cards_list}')
                break
        new_player_score = 0
        for card in self.player_cards_list:
            if type(card) is str:
                card = cards_values[card.upper()]
            new_player_score += int(card)
        self.total_player_score = new_player_score

if __name__ == "__main__":
    App()
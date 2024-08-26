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

 
#making a list of all the card keys for later use in the ace function
cards_list = list(cards_values.keys())

#the main program put into a class so that the program can function properly
class App(ctk.CTk):
    
    #making the total player and dealer score variables and player card list
    # varialbe for later 
    total_player_score = 0
    total_dealer_score = 0 
    player_cards_list = []

    #start of GUI makes the geometry,title,and mainloop for gui
    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        self.root.title("Blackjack Aid")
        self.root.geometry('330x560')
        self.start()
        self.root.mainloop()
        self.value_inside = ctk.StringVar(self.root)
        self.value_inside.set("Select an Option")

    #start of program
    #makes the first frame asking user to input their two cards and
    #the dealer card
    def start(self):
        # asking user to input player cards
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both",expand=1)

        player_card_label = ctk.CTkLabel(self.main_frame, text="What cards "
                                          "do you have? ",font=("arial",20))
        player_card_label.pack(pady=20)
        
        player_help_label = ctk.CTkLabel(self.main_frame,text="Select the two "
            "cards that have been\n delt to you at the start of the game",
            font=("arial",15))        
        player_help_label.pack()
        
        self.player_card_1 = ctk.CTkOptionMenu(self.main_frame, width = 190,
             height = 45, font=("arial",20),values=list(cards_values))
        self.player_card_1.pack(pady=20)

        self.player_card_2 = ctk.CTkOptionMenu(self.main_frame, width = 190,
             height = 45, font=("arial",20),values=list(cards_values))
        self.player_card_2.pack(pady=20)

        #asking user to input dealer cards
        dealer_card_label= ctk.CTkLabel(self.main_frame,text="What card does"
            " the dealer have?", font=("arial",20))
        dealer_card_label.pack(pady=20)
        
        dealer_help_label=ctk.CTkLabel(self.main_frame,text="Select the card"
            " that the\n dealer has been delt at the start",font=("arial",15))
        dealer_help_label.pack()
       
        self.dealer_cards =  ctk.CTkOptionMenu(self.main_frame,width=190,
            height=45,font=("arial",20),values=list(cards_values))
        self.dealer_cards.pack(pady=20)

        enter_button = ctk.CTkButton(self.main_frame,text="Enter", width=190, 
            height=45,font=("arial",20),
            command=lambda: self.hit_or_stand())
        enter_button.pack(pady=20)

    #calculates playes and dealer score and chencks if they should hit or stand
    #also chenckes if they have more that 21 and an ace to see if the ace should
    # 1 or if they dont they bust
    #calls the function corrisponding to what they should do
    def hit_or_stand(self, p_cards: list=None):
        if not hasattr(self, 'player_cards'):
            self.player_cards = [self.player_card_1.get(),
                self.player_card_2.get()]
    
        # can assume that the dealers score hasnt been stored
        if self.total_dealer_score == 0:
            self.total_dealer_score = cards_values[self.dealer_cards.get()
                .upper()]

        #makes a list of player cards for ace function
        player_cards = p_cards or self.player_cards    
        for card in player_cards:
            self.player_cards_list.append(card.lower())

        #resetting total player score to 0 before calculating the score
        self.total_player_score = 0

        #calculates total player score
        for card in self.player_cards_list:
            if card.upper() in cards_values:
                self.total_player_score = (self.total_player_score + 
                    cards_values[card.upper()])
              
        # if player has over 21 and an ace it will update players total score
        if self.total_player_score > 21:
            self.ace_21()

        #if the total player score is more than 21 and they dont have an ace
        # user will bust
        if self.total_player_score > 21:
            self.bust()
        
        #if player has 17 or more always stand
        elif self.total_player_score >= 17 :
            self.stand()

        #if player has 11 or less always hit
        elif self.total_player_score <= 11:
             self.hit()

        #if player has 12, hit if dealer has 3 or less or 7 or more,
        # otherwise stand
        elif self.total_player_score == 12:
            if self.total_dealer_score <= 3:
                 self.hit()
            elif self.total_dealer_score >=7:
                self.hit()
            else:
                self.stand()

        #if player has 16 or less, hit if dealer has 7 or more, otherwise stand
        elif self.total_player_score <=16:
            if self.total_dealer_score >=7:
                 self.hit()
            else:
                self.stand()
        else:
            self.stand()

    
    #function that restarts the program by ressetting data and calling the first
    # function in the loop
    def restart(self):
        del self.player_cards
        self.total_dealer_score = 0
        self.total_player_score = 0
        self.player_cards_list.clear()
        self.frame_2.destroy()
        self.start()

        
    #function that makes a button that calls the restart function
    def return_button_function(self, parent, callback):
        self.return_button = ctk.CTkButton(parent,text="Go again?",width=190,
             height=45,font=("arial",20), command=callback)
        self.return_button.pack()


    #Function that deletes the second frame(hit, stand, or bust frame)
    def delete_result_frame(self):
        if hasattr(self, 'frame_2'):
            self.frame_2.destroy()

    
    # function that makes a frame that tells the user to stand 
    #contains the return button
    def stand(self):
        self.delete_result_frame()
        self.main_frame.destroy()
        self.frame_2 = ctk.CTkFrame(self.root)
        self.frame_2.pack(fill="both", expand=1)
        self.player_stand = ctk.CTkLabel(self.frame_2,text="Stand",font=(""
                                            "arial",40))
        
        self.player_stand.pack(pady=80,)
        self.player_label_stand=ctk.CTkLabel(self.frame_2,text=f"Your total " 
            f"score right now is: {self.total_player_score}",font=("arial",15))
        self.player_label_stand.pack(pady=(0,30))
        self.return_button_function(self.frame_2, self.restart)
         
        self.total_dealer_score = 0
        self.total_player_score = 0

        self.player_cards_list.clear()


    #function that makes a new frame that tells the user to hit
    #contains option menu for new card, enter button, and return button
    def hit(self):
        self.delete_result_frame()
        self.main_frame.destroy()
        self.frame_2 = ctk.CTkFrame(self.root)
        self.frame_2.pack(fill="both",expand=1)
        self.player_hit=ctk.CTkLabel(self.frame_2, text="Hit", 
            font=("arial",40))
        self.player_hit.pack(pady=80)
        self.player_label_hit=ctk.CTkLabel(self.frame_2,text=f"Your total score"
            f" right now is: {self.total_player_score}",font=("arial",15))
        self.player_label_hit.pack(pady=0)
        self.player_hit_label=ctk.CTkLabel(self.frame_2,text=" Please enter the"
            " new card you've been delt",font=("arial",15))
        self.player_hit_label.pack(pady=20)
        self.player_hit_entry=ctk.CTkOptionMenu(self.frame_2,width = 190,
            height = 45,font = ("arial",20),values=list(cards_values))
        self.player_hit_entry.pack(pady=20)

        enter_button_2 = ctk.CTkButton(self.frame_2,text="Enter", width=190,
            height=45, font=("arial",20),command=lambda: 
                self.hit_or_stand([self.player_hit_entry.get()]))
        enter_button_2.pack(pady=20)

        self.return_button_function(self.frame_2, self.restart)


    #Function that changes aces to 1 when the total score over 21 and 
    #recalculates the total player score
    def ace_21(self):
        #making card list
        for card_data in enumerate(self.player_cards_list):
            index, card = list(card_data)
            
            #checking if they have an ace
            if card.upper() == "A":

                #changes ace to 1
                self.player_cards_list[index] = str(cards_values['1'])
                
                #breaks loop after ace has been changed to 1
                break
        
        #restets total player score
        new_player_score = 0
        for card in self.player_cards_list:
            if type(card) is str:                
                card = cards_values[card.upper()]
            new_player_score += int(card)
        self.total_player_score = new_player_score

    
    #function that tells the user that the busted
    #contains return button
    def bust(self):
        #destroying previus frames
        self.delete_result_frame()
        self.main_frame.destroy()
        self.frame_2.destroy()
        
        self.frame_2= ctk.CTkFrame(self.root)
        self.frame_2.pack(fill="both", expand=1)
        
        self.player_bust = ctk.CTkLabel(self.frame_2,text=f"You busted with a\n" 
            "score of more than 21",font=("arial",20))
        self.player_bust.pack(pady=(80,10))
        
        self.player_bust_2 = ctk.CTkLabel(self.frame_2,text = f'You had a'
            f' total score of: {self.total_player_score}', font=("arial",20))
        self.player_bust_2.pack(pady = (0,80))
        
        self.return_button_function(self.frame_2, self.restart)


if __name__ == "__main__":
    App()
'''
    Team Name: Robo-Squad
    Team Members: Himanshu Londhe
                  Pratik Jogdand
                  Swapnil Bhosale
    This is the class structure to hold the previous trick result
    holds the details of lead of the trick, winner and all the cards played in that trick
'''
class History():

    def __init__(self, lead, winner, trick):
        super().__init__()
        self.lead = lead
        self.winner = winner
        self.trick = trick
        self.score = 0



'''
    This class is a blueprint for the card playing agent
    This class implements the API for the agent
'''
class Player():

    team_name = "Robo_Squad"
    
    '''
        This is the constructor of the Player class.
        Constructor initializes the class instance variable to default values
        also initializes some constants
    '''
    def __init__(self):
        super().__init__()
        self.name = Player.team_name
        self.history = []
        self.hand = {}
        self.opponents = []
        self.counter = 0
        self.point = 0
        self.trick = 0
        self.type_of_cards = ["S", "H", "D", "C"]
        self.face_val = {
                        "T": "10",
                        "J": "11",
                        "Q": "12",
                        "K": "13",
                        "A": "14"
                    }
        self.rev_face_val = {
                            "10": "T",
                            "11": "J",
                            "12": "Q",
                            "13": "K",
                            "14": "A"
                        }
        
    
    '''
        This method returns the name of the agent.
        In our implementation in returns our team name
    '''
    def get_name(self):
        return self.name

    '''
        return the cards in the hand
    '''
    def get_hand(self):
        current_hand = []
        for val in self.hand:
            for val1 in self.hand[val]:
                current_hand.append(self.reverse_transform_card(val1))
        return current_hand
    
    '''
        This method accepts the list of cards as a hand cards.
        Also reinitialzies the variable because this method is called means it is a new game
    '''
    def new_hand(self, names: list):
        temp = names.copy()
        self.history.clear()
        self.hand.clear()
        self.opponents.clear()
        temp.remove(self.name)
        self.opponents = temp
        self.counter = 0
        #print(names)

    '''
        This method transforms the card face value to the type 
        which is used by our agent for selecting the random card
    '''
    def transform_card(self, card):
        face_value = card[0]
        if face_value == "T" or face_value == "J" or face_value == "Q"  or face_value == "K"  or face_value == "A":
            return (int(self.face_val[face_value]), card[1])
        else:
            return (int(face_value), card[1])


    def reverse_transform_card(self, card):
        #print("^^^^^^^^^^^^ ",card)
        face_value = card[0]
        res = ""
        if str(face_value) in self.rev_face_val:
            res += self.rev_face_val[str(face_value)] 
        else:
            res += str(face_value) 
        res += card[1]
        return res

    '''
        This method accepts the cards as a parameter.
        This cards would be allocated to our agent. Agent plays the game using these cards
    '''    
    def create_hand(self, cards):
        for val in cards:
            face_card_transformed = self.transform_card(val)
            if val[1] in self.hand:
                self.hand[val[1]].append(face_card_transformed)
            else:
                self.hand[val[1]] = [face_card_transformed]
        
        #print("created hand: player:{} , {}".format(self.name, self.hand))

    '''
        Add cards to the agent hand
    '''
    def add_cards_to_hand(self, cards):
        self.create_hand(cards)
    '''
    Helper function to check if we have an Ace of any kind in hand
    '''
    def do_we_have_ace(self):
        #print("finding  ace",self.hand)
        for val in self.hand:
            for val1 in self.hand[val]:
                if val1[0] == 14:
                    return True
    '''
    Helper funtion to find an Ace from the current hand
    '''
    def find_ace_card(self):
        
        for val in self.hand:
            for val1 in self.hand[val]:
                if val1[0] == 14:
                    return val1

    def find_ace_card_suit(self,  suit):
        res = None
        for val in self.hand[suit]:
            if val[0] == 14 :
                res = val
                break
        return  res



    def get_history(self):
        history_dict = {}
        for val in self.history:
            for card in val.trick:
                if card[1] in history_dict:
                    history_dict[card[1]].append(self.transform_card(card))
                else:
                    history_dict[card[1]] = [self.transform_card(card)]
        return history_dict

    '''
        This function is the part of agent where all business logic resides
    '''
    def play_card(self, lead, trick):
        
        card_to_be_return = None

        curr_trick_len = len(trick)

        if curr_trick_len == 0:  #if our agent is the lead

            #we have clubof two and first trick hence return that
            #if self.trick == 0:
                #card_to_be_return = (2, "C")
            if self.do_we_have_ace():     #if we have ace palce it
                #print("We have ace ")
                card_to_be_return = self.find_ace_card()
                #print("returnug ")
            else:
                #if we hold card of the suit greater than all the card with the same suit played in the history
                #then play that unplayed card
                #print("in else")
                history_dict = self.get_history()
                max_cards = {}
                for val in self.hand:
                    if len(self.hand[val]) > 0:
                        max_cards[val] = max(self.hand[val],key=lambda item:item[0])
                #print("max_cards: ", max_cards)
                for val in max_cards:
                    temp_set = {(i, val) for i in range(2,15)}
                    temp_set -= set(history_dict[val]) if val in history_dict and len(history_dict[val]) > 0 else set()
                    #print("temp_set: ",temp_set)
                    if max_cards[val][0] >= max(temp_set,key=lambda x:x[0])[0]:
                        card_to_be_return = max_cards[val]
                        break
                if card_to_be_return is None:
                    #print("inside card return is none")
                    temp = []
                    for val in self.type_of_cards:
                        if val in self.hand and len(self.hand[val]) > 0:
                            temp.append(min(self.hand[val],key=lambda item:item[0])) 
                    card_to_be_return = min(temp)

        elif curr_trick_len == 1 or curr_trick_len == 2:    #if our agent is 2nd or 3rd in the round

            if trick[0][1] in self.hand and len(self.hand[trick[0][1]]) > 0: #if we have a card of that particular suit
                max_card_hand = max(self.hand[trick[0][1]],key=lambda item:item[0])
                history_dict = self.get_history() #fetching latest history
                temp_set = set()
                for i in range(2,15):
                    temp_set.add((i, trick[0][1]))
                #print(temp_set - set())
                temp_set -= set(history_dict[trick[0][1]]) if trick[0][1] in history_dict else set() #calcuting the set difference to further compare with history
                trick_transformed = [self.transform_card(val) for val in trick]
                curr_max_trick = -99
                for val in trick_transformed:
                    if val[1] == trick_transformed[0][1] and val[0] > curr_max_trick:
                        curr_max_trick = val[0]
                #current_max = max([val for val in trick_transformed ])
                if max_card_hand[0] >= max(temp_set,key=lambda x:x[0])[0] and curr_max_trick < max_card_hand[0] : #checking condition to see if we have the best card after comparing with history
                        card_to_be_return = max_card_hand     
                else:
                    card_to_be_return = min(self.hand[trick[0][1]],key=lambda item:item[0])
            else: #if we dont have a card of that particular suit
                temp = []
                for val in self.type_of_cards:
                    if val in self.hand and len(self.hand[val]) > 0:
                        temp.append(min(self.hand[val],key=lambda item:item[0])) 
                card_to_be_return = min(temp)
        else: #the agent is 4th player in this particular trick

            if trick[0][1] in self.hand and len(self.hand[trick[0][1]]) > 0: #if we have a card of that particular suit
                max_cards = max(self.hand[trick[0][1]],key=lambda item:item[0])
                history_dict = self.get_history() #fetching latest history
                temp_set = set()
                for i in range(2,15):
                    temp_set.add((i, trick[0][1]))
                temp_set -= set(history_dict[trick[0][1]]) if trick[0][1] in history_dict else set()
                trick_transformed = [self.transform_card(val) for val in trick]
                curr_max = -99
                for val in trick_transformed:
                    if val[1] == trick_transformed[0][1] and val[0] > curr_max:
                        curr_max = val[0]
                if max_cards[0] > curr_max:
                        card_to_be_return = max_cards     #determing the card to play after succcesfully comparing with history 
                else:
                    card_to_be_return = min(self.hand[trick[0][1]],key=lambda item:item[0]) #we don't have a max card which is lower than history. To play safe, the agent plays the min card.
            else:#if we dont have a card of that particular suit
                temp = []
                for val in self.type_of_cards:
                    if val in self.hand and len(self.hand[val]) > 0:
                        temp.append(min(self.hand[val],key=lambda item:item[0])) 
                card_to_be_return = min(temp)

        #transform back the card so that we stick to the API spec
        rev_formatted =  self.reverse_transform_card(card_to_be_return)
        #print("Player: {} played: {}".format(self.name, rev_formatted))
        #remove played card from the hand
        #print("************** ",self.hand[card_to_be_return[1]].index(card_to_be_return))
        self.hand[card_to_be_return[1]].pop(self.hand[card_to_be_return[1]].index(card_to_be_return))
        return rev_formatted
       
    '''
        check if the winner of the trick is self. then increases the own score
    '''
    def collect_trick(self, lead, winner, trick):
        self.history.append(History(lead, winner, trick))
        self.counter += 1
        self.trick += 1
        if winner == self.get_name():
            self.point += 1

    #returns the own score
    def score(self):
        return self.point
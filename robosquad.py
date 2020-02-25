class History():

    def __init__(self, lead, winner, trick):
        super().__init__()
        self.lead = lead
        self.winner = winner
        self.trick = trick
        self.score = 0



class Player():
    team_name = "Robo Squad"
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.team_name = name
        self.history = {}
        self.hand = {}
        self.opponents = []
        self.counter = 0
        self.score = 0
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
        
    
    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand
    
    def new_hand(self, names: list):
        temp = names.copy()
        self.history.clear()
        self.hand.clear()
        self.opponents.clear()
        temp.remove(self.name)
        self.opponents = temp
        self.counter = 0
        print(names)

    
    def transform_card(self, card):
        face_value = card[0]
        if face_value == "T" or face_value == "J" or face_value == "Q"  or face_value == "K"  or face_value == "A":
            return (int(self.face_val[face_value]), card[1])
        else:
            return (int(face_value), card[1])

    def reverse_transform_card(self, card):
        face_value = card[0]
        res = ""
        if str(face_value) in self.rev_face_val:
            res += self.rev_face_val[str(face_value)] 
        else:
            res += str(face_value) 
        res += card[1]
        return res

    
    def create_hand(self, cards):
        for val in cards:
            face_card_transformed = self.transform_card(val)
            if val[1] in self.hand:
                self.hand[val[1]].append(face_card_transformed)
            else:
                self.hand[val[1]] = [face_card_transformed]
        
        print("created hand: player:{} , {}".format(self.name, self.hand))

        
    def add_card_to_hand(self, cards):
        self.create_hand(cards)

    def play_card(self, lead, trick):
        #we have that type of card
        card_to_be_return = None


        hist = []
        for val in self.history:
            hist.append(self.history[val].trick)
            #print(hist)
        
        if lead == self.team_name:
            print("hi")
            for i in self.hand:
                if i[0] == self.hand[i]:
                    print("aalo")
                    return self.reverse_transform_card(i)

        

        if lead != self.team_name and trick[0][1] in self.hand and len(self.hand[trick[0][1]]) > 0:
            max_val = max(self.hand[trick[0][1]],key=lambda item:item[0])
            if max_val[0] < max(trick)[0]:
                card_to_be_return = min(self.hand[trick[0][1]],key=lambda item:item[0])
            else:
                card_to_be_return = max_val
        else:
            temp = []
            for val in self.type_of_cards:
                if val in self.hand and len(self.hand[val]) > 0:
                    temp.append(min(self.hand[val],key=lambda item:item[0])) 
            card_to_be_return = min(temp)

        
        rev_formatted =  self.reverse_transform_card(card_to_be_return)
        print("Player: {} played: {}".format(self.name, rev_formatted))
        self.hand[card_to_be_return[1]].pop(self.hand[card_to_be_return[1]].index(card_to_be_return))





        return rev_formatted

         
       

    def collect_trick(self, lead, winner, trick):
        self.history[self.counter] = History(lead, winner, trick)
        self. counter += 1
        if winner == self.get_name():
            self.score += 1

    
    def score(self):
        return self.score

import random

def chunk(xs, n):
    ys = list(xs)
    random.shuffle(ys)
    ylen = len(ys)
    size = int(ylen / n)
    chunks = [ys[0+size*i : size*(i+1)] for i in range(n)]
    leftover = ylen - size*n
    edge = size*n
    for i in range(leftover):
            chunks[i%n].append(ys[edge+i])
    return chunks


def main():
    cards = ['2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AS',
            '2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD','AD',
            '2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AH',
            '2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AC']
    
    
    shuffeled = chunk(cards, 4)
    players = ["Himya", "Pratik", "Swapnil", "Robo Squad"]
    prev_player = players[0]
    player1 = Player(players[0])
    player2 = Player(players[1])
    player3 = Player(players[2])
    player4 = Player(players[3])
    player1.new_hand(players)
    player2.new_hand(players)
    player3.new_hand(players)
    player4.new_hand(players)
    player1.create_hand(shuffeled[0])
    player2.create_hand(shuffeled[1])
    player3.create_hand(shuffeled[2])
    player4.create_hand(shuffeled[3])
    def play_trick_sequentially(lead, trick, prev_player):
        if prev_player == "Himya":
            return player1.play_card(lead, trick)
        elif prev_player == "Pratik":
            return player2.play_card(lead, trick)
        elif prev_player == "Swapnil":
            return player3.play_card(lead, trick)
        elif prev_player == "Robo Squad":
            return player4.play_card(lead, trick)
        
    lead = players[0]
    prev_player = players[0]
    count = 0
    def transform_card(card):
        face_value = card[0]
        if face_value == "T" or face_value == "J" or face_value == "Q"  or face_value == "K"  or face_value == "A":
            return (int(face_val[face_value]), card[1])
        else:
            return (int(face_value), card[1])
    face_val = {
                        "T": "10",
                        "J": "11",
                        "Q": "12",
                        "K": "13",
                        "A": "14"
                    }
    rev_face_val = {
                            "10": "T",
                            "11": "J",
                            "12": "Q",
                            "13": "K",
                            "14": "A"
                        }
    def reverse_transform_card(self, card):
        face_value = card[0]
        res = ""
        res += rev_face_val[str(face_value)] 
        res += card[1]
        return res
    


    def send_res(res, trick_players):
        winner = None,
        game_lead = res[0][0]
        
        max_val = max(res,key=lambda item:item[0])
        winner = trick_players[res.index(max_val)]
        player1.collect_trick(game_lead, winner, res)
        player2.collect_trick(game_lead, winner, res)
        player3.collect_trick(game_lead, winner, res)
        player4.collect_trick(game_lead, winner, res)
        return winner


    
    for i in range(13):
        prev = []
        trick_players = []
        print("***** playing round:{} lead:{}".format(i, lead))
        for j in range(4):
            res = play_trick_sequentially(lead, prev, prev_player)
            prev.append(transform_card(res))
            trick_players.append(prev_player)
            prev_player = players[(players.index(prev_player) + 1) % 4]
        lead  = send_res(prev, trick_players)
        prev_player = lead

        print("************ winner is ",lead)





if __name__ == "__main__":
    main()
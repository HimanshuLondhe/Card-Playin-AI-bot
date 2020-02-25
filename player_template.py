class Player(object):
    def __init__(self):
        pass

    def get_name(self):
        return "Himya"
        pass

    def get_hand(self):
        """
        Returns a list of two character strings reprsenting cards in the agent's hand
        """
        pass

    def new_hand(self, names):
        """
        Takes a list of names of all agents in the game in clockwise playing order
        and returns nothing. This method is also responsible for clearing any data
        necessary for your agent to start a new round.
        """
        pass

    def add_cards_to_hand(self, cards):
        """
        Takes a list of two character strings representing cards as an argument
        and returns nothing.
        This list can be any length.
        """
        pass

    def play_card(self, lead, trick):
        """
        Takes a a string of the name of the player who lead the trick and
        a list of cards in the trick so far as arguments.

        Returns a two character string from the agents hand of the card to be played
        into the trick.
        """
        pass

    def collect_trick(self, lead, winner, trick):
        """
        Takes three arguements. Lead is the name of the player who led the trick.
        Winner is the name of the player who won the trick. And trick is a four card
        list of the trick that was played. Should return nothing.
        """
        pass

    def score(self):
        """
        Calculates and returns the score for the game being played.
        """
        pass

play_card("himya" , ["3C,'6C","QS"])
play_card("swapnil", ["8H"])

play card("robo squad", ["AD",])


play_card("pratik", "AS")
play_card("swapnil", "4S")

    play_card("Pratik", "3S")


cardlist = ('2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AS',q
            '2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD','AD',
            '2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AH',
            '2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AC')
print (cardlist)



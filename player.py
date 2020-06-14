VALUE_DICT = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10, "King": 10,"Queen": 10,"Jack": 10,"Joker":0}

class Player:
    def __init__(self, index, cards, next_player = None):
        """
        index   : unique player number
        cards   : cards dealt
        """
        self.index          = index
        self.cards          = cards
        self.next_player    = next_player 
        self.value          = self.get_current_value()

    def get_current_value(self):
        value = 0
        for card in self.cards:
            value = value + self.__get_card_value(card)
        return value

            
    def __get_card_value(self, card):
        return VALUE_DICT[card.value]
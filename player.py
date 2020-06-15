VALUE_DICT = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10, "King": 10,"Queen": 10,"Jack": 10,"Joker":0}

def print_cards(cards, return_str):
    return_str = ""
    for item in cards:
            return_str = return_str + str(item.suit) + "of" + str(item.value) + "\n\n"
    return return_str + "\n\n"
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

    def __str__(self):
        return_str = ""
        return_str = return_str + "Player {} \n\n".format(self.index)
        return_str = return_str + "Cards: \n\n"
        return_str = print_cards(self.cards, return_str)
        return_str = return_str + "Total : {}".format(self.get_current_value()) + "\n\n"
        return return_str
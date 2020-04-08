import pydealer as pd
from socket import *

MAX_PLAYERS     = 8
CARDS_TO_DEAL   = 5


class Player:
    def __init__(self, index, cards, next_player = None):
        """
        index   : unique player number
        cards   : cards dealt
        """
        self.index          = index
        self.cards          = cards
        self.next_player    = next_player 


class Game:
    def __init__(self):
        # deck of cards we are playing with!
        self.deck           = pd.Deck(jokers=True, num_jokers=3)
        self.deck.shuffle()

        # player info
        self.num_players    = 0     # initialised in new_game
        self.players         = []    # initialised in new_game

        # other piles
        self.unopened       = None
        self.top_cards       = []
        self.discarded      = []

        # who's playing
        self.curr_player    = 0

    
    def error(self, message):
        printf(""+message)
    
    def new_game(self, num_players):
        if num_players>MAX_PLAYERS:
            self.error("player limit exceeded")

        # create players
        self.num_players = num_players
        old_player = None
        first_player = None
        player = None
        for idx in range(num_players):
            # I dont want to deal with the stack, its irritating TODO
            dealt_cards_stack = self.deck.deal(CARDS_TO_DEAL, rebuild=False, shuffle=True)
            player = Player(idx, list(dealt_cards_stack.cards), old_player)
            if idx == 0:
                first_player = player
            self.players.append(player)
            old_player = player
        first_player.next_player = player

        # deal the top card
        # dont want to deal with the stack TODO
        self.top_cards = list(self.deck.deal(1, rebuild=False, shuffle=True).cards)
        self.discarded.extend(self.top_cards)
        self.top_card_index = 0
        
        # keep the rest of the deck down
        self.unopened = self.deck

        # player 0 starts
        self.curr_player = player
    
    def play_discard(self, cards_text):
        cards_arr = cards_text.split(",")
        cards_arr_int  = []
        for card in cards_arr:
            cards_arr_int.append(int(card))
        cards_arr_int.sort(reverse=True)

        return_string = []
        
        for card_idx in cards_arr_int:
            discarded_card = self.curr_player.cards.pop(card_idx)
            self.discarded.append(discarded_card)
            return_string.append("Removing player {}'s {} card".format(self.curr_player.index, discarded_card ))

        return return_string

    def play_pick_card(self, card_str):
        return_str = []
        if card_str.startswith("OLD"):
            self.curr_player.cards.append(self.top_cards[card_str[3]])
            self.discarded.pop(self.top_card_index)
            self.top_cards = self.discarded[self.top_card_index:len(self.discarded)-1]
        elif card_str == "NEW":
            card = list(self.unopened.deal(1, False, False).cards)[0]
            self.curr_player.cards.append(card)
            self.top_cards = self.discarded[self.top_card_index+1:len(self.discarded)]
            self.top_card_index = self.top_card_index+1
        return return_str

    def next_player(self):
        self.curr_player = self.curr_player.next_player

        
if __name__=="__main__":
    # Load the sockets - connection - whatevs

    # how many players?

    # create the new game
    game = Game()
    game.new_game(5)

    while True:
        # whose turn is it?
        turn = game.curr_player.index
        print("PLayer {} plays".format(turn))
        print("TOP CARD: {}".format(game.top_cards))

        first_text = input("SHOW? PLAY?")
        if first_text == "SHOW":
            game.show()
        elif first_text == "PLAY":
            second_text = input("Discard this") # 1,2
            print(game.play_discard(second_text))
            third_text  = input("OLD? NEW?") # OLD0, OLD1, NEW
            print(game.play_pick_card(third_text))
            game.next_turn()
        else:
            print("wut?")


        game.play(first_text)


        print(game.curr_player.cards)

        print(0)
        
        

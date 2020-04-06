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
        self.top_card       = None
        self.discarded      = None

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
            dealt_cards = self.deck.deal(CARDS_TO_DEAL, rebuild=False, shuffle=True)
            player = Player(idx, dealt_cards, old_player)
            if idx == 0:
                first_player = player
            self.players.append(player)
            old_player = player
        first_player.next_player = player

        # deal the top card
        self.top_card = self.deck.deal(CARDS_TO_DEAL, rebuild=False, shuffle=True)
        
        # keep the rest of the deck down
        self.unopened = self.deck

        # player 0 starts
        self.curr_player = player
    
    def play_turn(self):
        print(1)


        
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

        print(game.curr_player.cards)

        print(0)
        
        

import pydealer as pd

# local imports
from player import Player, print_cards

MAX_PLAYERS     = 8
CARDS_TO_DEAL   = 5

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
        self.curr_player_idx = 0 # starts the game!

    def print_dict(self, data):
        return_str = ""
        for item in data.keys():
            return_str = return_str + "{} : {}".format(item, data[item])
        return return_str
    
    def public_info(self):
        return_str = {}
        return_str["curr_turn"] = self.curr_player
        return_str["top_cards"] = self.top_cards
        return_str["discarded"] = self.discarded
        return return_str
    
    
    def private_info(self):
        return_str = self.public_info
        for player in self.players:
            return_str[""+player.index] = player
        
        return return_str


    def __str__(self):
        return_str = "current player is {}".format(self.curr_player)
        return_str = return_str + "top cards: \n"
        return_str = print_cards(self.top_cards, return_str)
        return_str = return_str + "discarded cards: \n"
        return_str = print_cards(self.discarded, return_str)
        for item in self.players:
            return_str = return_str + "Player {} \n".format(item.index) + str(item)
        return return_str


    def error(self, message):
        print(""+message)

    def __deal_as_list(self, num_cards, shuffle):
        return list(self.deck.deal(num_cards, shuffle=shuffle, rebuild=False).cards)
    
    def new_game(self, num_players):
        if num_players>MAX_PLAYERS:
            self.error("player limit exceeded")

        # create players
        self.num_players = num_players
        old_player = None #
        first_player = None#
        player = None
        for idx in range(num_players):
            # I dont want to deal with the stack, its irritating TODO
            dealt_cards_list = self.__deal_as_list(CARDS_TO_DEAL, shuffle=True)
            player = Player(idx, dealt_cards_list, old_player)
            if idx == 0:#
                first_player = player#
            self.players.append(player)
            old_player = player#
        first_player.next_player = player#

        self.curr_player_idx = 0 # starts the game!

        # deal the top card
        # dont want to deal with the stack TODO
        self.top_cards = self.__deal_as_list(1, shuffle=False)
        
        # keep the rest of the deck down
        self.unopened = self.deck

        # player 0 starts
        self.curr_player = self.players[self.curr_player_idx]
    
    def play_turn(self, discard_list_idx=None, pick_card_idx=None):
        # if show()
        # do something
        
        # if pick a new card
        if pick_card_idx == -1:
            # move current top card to discarded:
            for item in self.top_cards:
                card = self.top_cards.pop(-1)
                self.discarded.append(card)
            
            # makes popping possible
            discard_list_idx.sort(reverse=True)
            # move your discarded cards to the top cards pile:
            for idx in discard_list_idx:
                card = self.players[self.curr_player_idx].cards.pop(i)
                self.top_cards.append(card)
            
            # get your damn card!
            card = self.__deal_as_list(1, shuffle=True)
            self.players[self.curr_player_idx].cards.append(card)
        
        else:
            # move card from top to hand
            card = self.top_cards.pop(pick_card_idx)
            self.players[self.curr_player_idx].cards.append(card)

            # move top to discard
            for item in self.top_cards:
                card = self.top_cards.pop(-1)
                self.discarded.append(card)
            
            # makes popping possible
            discard_list_idx.sort(reverse=True)
            # move your discarded cards to the top cards pile:
            for idx in discard_list_idx:
                card = self.players[self.curr_player_idx].cards.pop(-1)
                self.top_cards.append(card)

        # next player be YOU!!
        self.curr_player_idx = self.curr_player_idx+1
        if self.curr_player_idx>self.num_players:
            self.curr_player_idx = 0

            
    
    '''
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
        self.curr_player.update()
        self.curr_player = self.curr_player.next_player
    '''
    
    def show(self):
        return_str = []
        return_str.append("Player {} Shows!".format(self.curr_player.index))
    
    def player_info(self):
        return_str = {}
        return_str["player num"] = self.curr_player_idx
        
        card_str = ""
        for card in self.players[self.curr_player_idx].cards:
            card_str = card_str + str(card.value) + " of " + str(card.suit) + "\n"
        return_str["player cards"] = card_str

        card_str = ""
        for card in self.top_cards:
            card_str = card_str + str(card.value) + " of " + str(card.suit) + "\n"
        return_str["top cards"] = card_str

        return return_str
        

        
if __name__=="__main__":
    game = Game()
    game.new_game(5)
    print(game.print_dict(game.public_info()))

    while(1):
        print(game.print_dict(game.public_info()))
        print(game.print_dict(game.player_info()))
        discard = []
        pick = 0
        print("BreakPoint MOFFOOO")
        game.play_turn(discard_list_idx=discard, pick_card_idx=pick)




    '''
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

    '''
        
        

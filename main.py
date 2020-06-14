

# local imports
from game import Game

        
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
        
        

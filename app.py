#!flask/bin/python
from flask import Flask, render_template
import pydealer as pd

# local imports
from player import Player
from game import Game

MAX_PLAYERS     = 8
CARDS_TO_DEAL   = 5

app = Flask(__name__)
game = Game()


@app.route('/')
def home():
    game.new_game(5)
    return render_template("start_page.html")

@app.route('/update', methods = ["POST", "GET"])
def update():
    state_data = str(game)
    player_num = game.curr_player
    player_data = game.print_dict(game.player_info())

    return render_template("main_page.html", state_data = state_data, player_num = player_num, player_data = player_num)

if __name__ == '__main__':
    app.run(debug=True)
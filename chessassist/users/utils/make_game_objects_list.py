import requests
import json


def make_game_object_list(username):
    resp = requests.get(f'https://lichess.org/api/games/user/{username}', params={'max': 50, 'analysed': True, 'pgnInJson': True, 'moves': True, 'evals': True, 'opening': True}, headers={"Accept": "application/x-ndjson"})

    games_list = resp.text.splitlines()
    games_list_dictified = []
    for game in games_list:
        game_dictified = json.loads(game)
        games_list_dictified.append(game_dictified)


    class Game:
        def __init__(self, username=username, color=None, win=None, moves=None, opening=None, analysis=None, pgn=None):
            self.username = username
            self.color = color
            self.win = win
            self.moves = moves
            self.opening = opening
            self.analysis = analysis
            self.pgn = pgn

        def make_game(self, input):

            if input['players']['white']['user']['name'] == self.username:
                self.color = 'white'
            else:
                self.color = 'black'

            if input['status'] == 'draw':
                self.win = 'draw'
            elif input['winner'] == self.color:
                self.win = 'win'
            else:
                self.win = 'loss'

            self.moves = input['moves']
            self.opening = input['opening']['name']
            self.analysis = input['analysis']
            self.pgn = input['pgn']

    game_objects_list = []
    for game in games_list_dictified:
        game_object = Game()
        game_object.make_game(game)
        game_objects_list.append(game_object)

    return game_objects_list
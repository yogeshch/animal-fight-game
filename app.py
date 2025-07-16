from flask import Flask, session, redirect, url_for, render_template, request, send_from_directory, make_response
from game_logic import AnimalFightGame
import os
import pickle

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Set cache timeout for static files (images, css, js)
@app.after_request
def add_cache_headers(response):
    if request.path.startswith('/static/'):
        response.cache_control.max_age = 60 * 60 * 24 * 365  # 1 year
        response.cache_control.public = True
    return response

def get_game():
    """Retrieve the current game from session, or create a new one."""
    if 'game' not in session:
        session['game'] = pickle.dumps(AnimalFightGame())
    return pickle.loads(session['game'])

def save_game(game):
    """Save the current game state to session."""
    session['game'] = pickle.dumps(game)

@app.route('/')
def home():
    return redirect(url_for('select_animals'))

@app.route('/select', methods=['GET', 'POST'])
def select_animals():
    if request.method == 'POST':
        selected = request.form.getlist('selected_animals')
        if len(selected) == 3:
            game = AnimalFightGame()
            game.select_player_animals(selected)
            save_game(game)
            return redirect(url_for('battle'))
    animals = AnimalFightGame().get_animals()
    return render_template('select.html', animals=animals)

@app.route('/battle', methods=['GET', 'POST'])
def battle():
    game = get_game()
    if request.method == 'POST':
        if game.battle_index >= 3:
            return redirect(url_for('results'))
        round_result = game.next_round()
        save_game(game)
        is_last_round = game.battle_index >= 3
        return render_template(
            'battle.html',
            round_num=round_result['round'],
            player_animal=round_result['player_animal'],
            player_value=round_result['player_value'],
            computer_animal=round_result['computer_animal'],
            computer_value=round_result['computer_value'],
            result=round_result['result'],
            player_score=game.player_score,
            computer_score=game.computer_score,
            is_last_round=is_last_round,
            pre_round=False
        )
    if game.battle_index == 0:
        return render_template(
            'battle.html',
            round_num=1,
            player_animal=None,
            player_value=None,
            computer_animal=None,
            computer_value=None,
            result=None,
            player_score=game.player_score,
            computer_score=game.computer_score,
            is_last_round=False,
            pre_round=True
        )
    else:
        if game.battle_index >= 3:
            round_result = game.rounds[-1]
            return render_template(
                'battle.html',
                round_num=round_result['round'],
                player_animal=round_result['player_animal'],
                player_value=round_result['player_value'],
                computer_animal=round_result['computer_animal'],
                computer_value=round_result['computer_value'],
                result=round_result['result'],
                player_score=game.player_score,
                computer_score=game.computer_score,
                is_last_round=True,
                pre_round=False
            )
        else:
            round_result = game.rounds[-1]
            is_last_round = game.battle_index >= 3
            return render_template(
                'battle.html',
                round_num=round_result['round'],
                player_animal=round_result['player_animal'],
                player_value=round_result['player_value'],
                computer_animal=round_result['computer_animal'],
                computer_value=round_result['computer_value'],
                result=round_result['result'],
                player_score=game.player_score,
                computer_score=game.computer_score,
                is_last_round=is_last_round,
                pre_round=False
            )

@app.route('/results')
def results():
    game = get_game()
    return render_template(
        'results.html',
        player_score=game.player_score,
        computer_score=game.computer_score,
        rounds=game.rounds
    )

@app.route('/rematch')
def rematch():
    game = AnimalFightGame()
    save_game(game)
    return redirect(url_for('select_animals'))

if __name__ == '__main__':
    app.run(debug=True) 
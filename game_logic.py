import random

ANIMAL_NAMES = [
    'lion', 'tiger', 'bear', 'wolf', 'fox',
    'elephant', 'giraffe', 'zebra', 'dolphin', 'penguin'
]

class AnimalFightGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.animal_values = self._randomize_animal_values()
        self.player_animals = []
        self.computer_animals = []
        self.battle_index = 0
        self.player_score = 0
        self.computer_score = 0
        self.rounds = []

    def _randomize_animal_values(self):
        values = list(range(1, 11))
        random.shuffle(values)
        return {animal: values[i] for i, animal in enumerate(ANIMAL_NAMES)}

    def select_player_animals(self, animals):
        self.player_animals = animals
        available = list(set(ANIMAL_NAMES) - set(animals))
        self.computer_animals = random.sample(available, 3)
        self.battle_index = 0
        self.player_score = 0
        self.computer_score = 0
        self.rounds = []

    def next_round(self):
        if self.battle_index >= 3:
            return None
        player_animal = self.player_animals[self.battle_index]
        computer_animal = self.computer_animals[self.battle_index]
        player_value = self.animal_values[player_animal]
        computer_value = self.animal_values[computer_animal]
        if player_value > computer_value:
            result = 'player'
            self.player_score += 1
        elif computer_value > player_value:
            result = 'computer'
            self.computer_score += 1
        else:
            result = 'tie'
        round_result = {
            'round': self.battle_index + 1,
            'player_animal': player_animal,
            'player_value': player_value,
            'computer_animal': computer_animal,
            'computer_value': computer_value,
            'result': result
        }
        self.rounds.append(round_result)
        self.battle_index += 1
        return round_result

    def is_game_over(self):
        return self.battle_index >= 3

    def get_scores(self):
        return {'player': self.player_score, 'computer': self.computer_score}

    def get_animals(self):
        return ANIMAL_NAMES

    def get_animal_values(self):
        return self.animal_values

    def get_computer_animals(self):
        return self.computer_animals 
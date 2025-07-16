# Animal Fighter Web App - Function Documentation

This document describes the key functions and routes in the Animal Fighter Web App (Flask version).

## Game Logic (game_logic.py)
- `AnimalFightGame` class: Encapsulates all game state and logic.
  - `reset_game(self)`: Resets the game state and randomizes animal values.
  - `select_player_animals(self, animals)`: Sets the player's animals and randomly selects computer animals.
  - `next_round(self)`: Plays the next round, returns round result dict.
  - `is_game_over(self)`: Returns True if all rounds are played.
  - `get_scores(self)`: Returns current scores.
  - `get_animals(self)`: Returns the list of animal names.
  - `get_animal_values(self)`: Returns the current animal values.
  - `get_computer_animals(self)`: Returns the computer's selected animals.

## Flask App (app.py)
- `/` (GET): Redirects to `/select`.
- `/select` (GET, POST):
  - GET: Shows animal selection page.
  - POST: Stores selected animals, starts new game, redirects to `/battle`.
- `/battle` (GET, POST):
  - GET: Shows pre-round state or last round's results.
  - POST: Plays next round, shows results. After last round, requires extra POST to go to `/results`.
- `/results` (GET): Shows final scores and round-by-round summary.
- `/rematch` (GET): Resets the game and redirects to `/select`.

## Frontend (templates/)
- `layout.html`: Base template, includes Bootstrap and custom CSS.
- `select.html`: Animal selection grid, enables 'Start Battle' when 3 animals are chosen.
- `battle.html`: Shows round number, animal images, powers, results, and navigation buttons.
- `results.html`: Shows final scores, winner, and a summary of all rounds.

## Notes
- Game state is stored in the session using pickle for persistence between requests.
- All animal images must be present in `static/images/` before starting the game.
- The UI is responsive and mobile-friendly. 
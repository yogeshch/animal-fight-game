# Animal Fighter GUI - Function Documentation

This document describes the key functions in `emoji_fighter_gui_images.py` (modern image edition).

## Image Handling
- `load_animal_images(self)`: Loads 10 animal images (150x150, .jpg/.png) from the local `Images` folder. Stores them in `self.animal_images` for use in the UI.
- `create_fallback_image(self, animal)`: Creates a colored fallback image if the animal image is missing.

## UI Setup
- `setup_ui(self)`: Builds the main window and all UI frames.
- `setup_selection_ui(self)`: Builds the animal selection grid, using loaded images.
- `setup_battle_ui(self)`: Builds the battle display.
- `setup_results_ui(self)`: Builds the results and replay UI.

## Game Logic
- `randomize_animal_values(self)`: Randomizes hidden values for each animal at the start of each game.
- `select_animal(self, animal_name)`: Handles player selection of animals.
- `update_selection_display(self)`: Updates the UI to show selected animals.
- `start_battle(self)`: Begins the battle phase, randomly selects computer animals.
- `next_battle_round(self)`: Runs each round of the battle, updates scores.
- `show_results(self)`: Displays the final result and score.
- `rematch(self)`: Resets the game for a new match.
- `exit_game(self)`: Exits the application.

## Notes
- All images must be present in the `Images` folder before starting the game.
- No debug or print statements are present in the production version. 
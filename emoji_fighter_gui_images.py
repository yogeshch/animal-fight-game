import os
import random
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class AnimalFighterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Fighter - Image Edition")
        self.root.geometry("900x650")
        self.root.configure(bg='#F7F9FA')  # Light background
        
        self.animal_names = [
            'lion', 'tiger', 'bear', 'wolf', 'fox',
            'elephant', 'giraffe', 'zebra', 'dolphin', 'penguin'
        ]
        self.animal_images = {}
        self.animal_values = {}
        self.player_animals = []
        self.computer_animals = []
        self.battle_index = 0
        self.player_score = 0
        self.computer_score = 0
        self.game_phase = "selection"  # selection, battle, results
        
        self.load_animal_images()
        self.setup_ui()
        self.randomize_animal_values()
        self.show_selection_phase()

    def load_animal_images(self):
        """Loads animal images from the Images folder."""
        for animal in self.animal_names:
            img_path_jpg = os.path.join('Images', f'{animal}.jpg')
            img_path_png = os.path.join('Images', f'{animal}.png')
            img = None
            if os.path.exists(img_path_jpg):
                img = Image.open(img_path_jpg)
            elif os.path.exists(img_path_png):
                img = Image.open(img_path_png)
            if img:
                img = img.resize((150, 150), Image.Resampling.LANCZOS)
                self.animal_images[animal] = ImageTk.PhotoImage(img)
            else:
                self.animal_images[animal] = self.create_fallback_image(animal)

    def create_fallback_image(self, animal):
        """Creates a fallback image if the animal image is missing."""
        img = Image.new('RGB', (150, 150), color=(200, 200, 200))
        return ImageTk.PhotoImage(img)

    def randomize_animal_values(self):
        """Randomizes hidden values for each animal."""
        values = list(range(1, 11))
        random.shuffle(values)
        self.animal_values = {animal: values[i] for i, animal in enumerate(self.animal_names)}

    def setup_ui(self):
        """Builds the main window and all UI frames."""
        # Title
        title_label = tk.Label(
            self.root,
            text="Animal Fighter - Image Edition",
            font=("Segoe UI", 26, "bold"),
            bg='#F7F9FA',
            fg='#222222'
        )
        title_label.pack(pady=20)

        self.main_frame = tk.Frame(self.root, bg='#F7F9FA')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.setup_selection_ui()
        self.setup_battle_ui()
        self.setup_results_ui()

    def setup_selection_ui(self):
        self.selection_frame = tk.Frame(self.main_frame, bg='#F7F9FA')
        instructions = tk.Label(
            self.selection_frame,
            text="Select 3 animals for battle!",
            font=("Segoe UI", 16, "bold"),
            bg='#F7F9FA',
            fg='#3498DB'
        )
        instructions.pack(pady=10)
        self.progress_label = tk.Label(
            self.selection_frame,
            text="Selection: 0/3",
            font=("Segoe UI", 14),
            bg='#F7F9FA',
            fg='#2980B9'
        )
        self.progress_label.pack(pady=5)
        self.animal_grid = tk.Frame(self.selection_frame, bg='#F7F9FA')
        self.animal_grid.pack(pady=20)
        self.animal_buttons = {}
        for i, animal in enumerate(self.animal_names):
            row = i // 5
            col = i % 5
            btn = tk.Button(
                self.animal_grid,
                image=self.animal_images[animal],
                width=150, height=150,
                relief='raised',
                bg='#EAF2FB',
                activebackground='#D6EAF8',
                borderwidth=2,
                command=lambda a=animal: self.select_animal(a)
            )
            btn.grid(row=row, column=col, padx=10, pady=10)
            self.animal_buttons[animal] = btn
        self.selected_frame = tk.Frame(self.selection_frame, bg='#F7F9FA')
        self.selected_frame.pack(pady=20)
        self.selected_label = tk.Label(
            self.selected_frame,
            text="Your selected animals: ",
            font=("Segoe UI", 14),
            bg='#F7F9FA',
            fg='#222222'
        )
        self.selected_label.pack()
        self.start_battle_btn = tk.Button(
            self.selection_frame,
            text="Start Battle!",
            font=("Segoe UI", 16, "bold"),
            bg='#F1C40F',
            fg='#222222',
            activebackground='#F9E79F',
            activeforeground='#222222',
            command=self.start_battle,
            state='disabled',
            borderwidth=2
        )
        self.start_battle_btn.pack(pady=20)

    def setup_battle_ui(self):
        self.battle_frame = tk.Frame(self.main_frame, bg='#F7F9FA')
        battle_title = tk.Label(
            self.battle_frame,
            text="BATTLE TIME!",
            font=("Segoe UI", 20, "bold"),
            bg='#F7F9FA',
            fg='#3498DB'
        )
        battle_title.pack(pady=10)

        # Score counter label
        self.score_label = tk.Label(
            self.battle_frame,
            text="You: 0 🏆   |   Computer: 0 🤖",
            font=("Segoe UI", 16, "bold"),
            bg='#F7F9FA',
            fg='#2980B9',
            anchor='center',
            justify='center'
        )
        self.score_label.pack(pady=(0, 10))

        # Animal matchup frame
        self.matchup_frame = tk.Frame(self.battle_frame, bg='#F7F9FA')
        self.matchup_frame.pack(pady=40)

        # Player animal tile
        self.player_tile = tk.Frame(self.matchup_frame, bg='#EAF2FB', bd=8, relief='ridge', width=180, height=220)
        self.player_tile.grid_propagate(False)
        self.player_img_label = tk.Label(self.player_tile, bg='#EAF2FB')
        self.player_img_label.pack()
        self.player_name_label = tk.Label(self.player_tile, font=("Segoe UI", 14, "bold"), bg='#EAF2FB', fg='#222222')
        self.player_name_label.pack()
        self.player_power_label = tk.Label(self.player_tile, font=("Segoe UI", 12), bg='#EAF2FB', fg='#3498DB')
        self.player_power_label.pack()
        self.player_tile.grid(row=0, column=0, padx=40, pady=10)

        # VS label
        self.vs_label = tk.Label(self.matchup_frame, text="VS", font=("Segoe UI", 24, "bold"), bg='#F7F9FA', fg='#F1C40F')
        self.vs_label.grid(row=0, column=1, padx=10)

        # Computer animal tile
        self.computer_tile = tk.Frame(self.matchup_frame, bg='#EAF2FB', bd=8, relief='ridge', width=180, height=220)
        self.computer_tile.grid_propagate(False)
        self.computer_img_label = tk.Label(self.computer_tile, bg='#EAF2FB')
        self.computer_img_label.pack()
        self.computer_name_label = tk.Label(self.computer_tile, font=("Segoe UI", 14, "bold"), bg='#EAF2FB', fg='#222222')
        self.computer_name_label.pack()
        self.computer_power_label = tk.Label(self.computer_tile, font=("Segoe UI", 12), bg='#EAF2FB', fg='#3498DB')
        self.computer_power_label.pack()
        self.computer_tile.grid(row=0, column=2, padx=40, pady=10)

        self.battle_display = tk.Text(
            self.battle_frame,
            height=6,
            width=60,
            font=("Segoe UI", 18, "bold"),
            bg='#FEF9E7',
            fg='#222222',
            wrap='word',
            state='disabled',
            relief='flat',
            borderwidth=0
        )
        self.battle_display.pack(pady=10, padx=20)
        self.next_round_btn = tk.Button(
            self.battle_frame,
            text="Next Round",
            font=("Arial", 14),
            bg='#3498DB',
            fg='white',
            command=self.next_battle_round
        )
        self.next_round_btn.pack(pady=10)

    def setup_results_ui(self):
        self.results_frame = tk.Frame(self.main_frame, bg='#F7F9FA')
        self.results_title = tk.Label(
            self.results_frame,
            text="",
            font=("Segoe UI", 24, "bold"),
            bg='#F7F9FA',
            fg='#3498DB'
        )
        self.results_title.pack(pady=20)
        self.final_scores = tk.Label(
            self.results_frame,
            text="",
            font=("Segoe UI", 16),
            bg='#F7F9FA',
            fg='#222222'
        )
        self.final_scores.pack(pady=10)
        button_frame = tk.Frame(self.results_frame, bg='#F7F9FA')
        button_frame.pack(pady=30)
        self.rematch_btn = tk.Button(
            button_frame,
            text="Play Again",
            font=("Segoe UI", 16, "bold"),
            bg='#F1C40F',
            fg='#222222',
            activebackground='#F9E79F',
            activeforeground='#222222',
            command=self.rematch,
            borderwidth=2
        )
        self.rematch_btn.pack(side='left', padx=10)
        self.exit_btn = tk.Button(
            button_frame,
            text="Exit Game",
            font=("Segoe UI", 16, "bold"),
            bg='#E74C3C',
            fg='#F7F9FA',
            activebackground='#FADBD8',
            activeforeground='#E74C3C',
            command=self.exit_game,
            borderwidth=2
        )
        self.exit_btn.pack(side='left', padx=10)

    def show_selection_phase(self):
        self.battle_frame.pack_forget()
        self.results_frame.pack_forget()
        self.selection_frame.pack(expand=True, fill='both')
        self.update_selection_display()

    def show_battle_phase(self):
        self.selection_frame.pack_forget()
        self.results_frame.pack_forget()
        self.battle_frame.pack(expand=True, fill='both')
        self.battle_index = 0
        self.player_score = 0
        self.computer_score = 0
        self.battle_display.config(state='normal')
        self.battle_display.delete('1.0', tk.END)
        self.battle_display.config(state='disabled')
        self.next_round_btn.config(state='normal')
        # Show placeholder tiles before first round
        self.set_placeholder_tiles()
        # Reset score label for new game
        self.score_label.config(text="You: 0 🏆   |   Computer: 0 🤖")

    def set_placeholder_tiles(self):
        # Player placeholder
        self.player_img_label.config(image='', bg='#EAF2FB')
        self.player_img_label.image = None
        self.player_name_label.config(text='Player')
        self.player_power_label.config(text='')
        self.player_tile.config(bg='#EAF2FB', bd=8)
        # Computer placeholder
        self.computer_img_label.config(image='', bg='#EAF2FB')
        self.computer_img_label.image = None
        self.computer_name_label.config(text='Computer')
        self.computer_power_label.config(text='')
        self.computer_tile.config(bg='#EAF2FB', bd=8)

    def show_results_phase(self):
        self.selection_frame.pack_forget()
        self.battle_frame.pack_forget()
        self.results_frame.pack(expand=True, fill='both')

    def select_animal(self, animal):
        if animal not in self.player_animals and len(self.player_animals) < 3:
            self.player_animals.append(animal)
            self.animal_buttons[animal].config(relief='sunken', bg='#27AE60')
            self.update_selection_display()
            if len(self.player_animals) == 3:
                self.start_battle_btn.config(state='normal')
            else:
                self.start_battle_btn.config(state='disabled')

    def update_selection_display(self):
        self.progress_label.config(text=f"Selection: {len(self.player_animals)}/3")
        selected = ', '.join(self.player_animals)
        self.selected_label.config(text=f"Your selected animals: {selected}")
        for animal, btn in self.animal_buttons.items():
            if animal in self.player_animals:
                btn.config(relief='sunken', bg='#27AE60')
            else:
                btn.config(relief='raised', bg='#34495E')

    def start_battle(self):
        all_animals = set(self.animal_names)
        available = list(all_animals - set(self.player_animals))
        self.computer_animals = random.sample(available, 3)
        self.show_battle_phase()

    def next_battle_round(self):
        if self.battle_index >= 3:
            self.next_round_btn.config(state='disabled')
            self.show_results()
            return

        player_animal = self.player_animals[self.battle_index]
        computer_animal = self.computer_animals[self.battle_index]
        player_value = self.animal_values[player_animal]
        computer_value = self.animal_values[computer_animal]
        result = ""
        if player_value > computer_value:
            result = f"You win this round! ({player_value} vs {computer_value})"
            self.player_score += 1
            winner = 'player'
        elif computer_value > player_value:
            result = f"Computer wins this round! ({computer_value} vs {player_value})"
            self.computer_score += 1
            winner = 'computer'
        else:
            result = f"It's a tie! ({player_value} vs {computer_value})"
            winner = 'tie'

        # Update animal tiles visually for the current round
        self.player_img_label.config(image=self.animal_images[player_animal])
        self.player_img_label.image = self.animal_images[player_animal]
        self.player_name_label.config(text=player_animal.capitalize())
        self.player_power_label.config(text=f"Power: {player_value}")
        self.computer_img_label.config(image=self.animal_images[computer_animal])
        self.computer_img_label.image = self.animal_images[computer_animal]
        self.computer_name_label.config(text=computer_animal.capitalize())
        self.computer_power_label.config(text=f"Power: {computer_value}")

        # Enhanced Animation: pulse winner, dim loser, animate VS
        self.reset_tile_highlights()
        self.animate_vs_label()
        self.animate_winner_loser(winner)

        # Update score label
        self.score_label.config(text=f"You: {self.player_score} 🏆   |   Computer: {self.computer_score} 🤖")

        # Show only the current round result, centered and styled
        self.battle_display.config(state='normal')
        self.battle_display.delete('1.0', tk.END)
        if winner == 'player':
            emoji = '🏆'
            color = '#27AE60'
        elif winner == 'computer':
            emoji = '🤖'
            color = '#E74C3C'
        else:
            emoji = '🤝'
            color = '#F1C40F'
        round_text = (
            f"Round {self.battle_index+1} {emoji}\n\n"
            f"🟦 You: {player_animal.capitalize()}  (Power: {player_value})\n"
            f"🟥 Computer: {computer_animal.capitalize()}  (Power: {computer_value})\n\n"
        )
        result_line = f"➡️  {result}"
        self.battle_display.tag_configure('center', justify='center')
        self.battle_display.tag_configure('normaltext', foreground='#222222')
        self.battle_display.insert(tk.END, round_text, ('center', 'normaltext'))
        self.battle_display.insert(tk.END, result_line + '\n', ('center', 'normaltext'))
        self.battle_display.config(state='disabled')

        # Animate the result text (scale up/fade in effect)
        self.animate_result_text()

        self.battle_index += 1

    def animate_winner_loser(self, winner):
        # Animation steps for pulse (background only, border width fixed)
        pulse_colors = ['#F7DC6F', '#F1C40F', '#F39C12', '#F1C40F', '#F7DC6F']
        steps = len(pulse_colors)
        duration = 1000  # ms
        interval = duration // steps

        def step(i):
            if winner == 'player':
                self.player_tile.config(bg=pulse_colors[i])
                self.computer_tile.config(bg='#EAF2FB')
            elif winner == 'computer':
                self.computer_tile.config(bg=pulse_colors[i])
                self.player_tile.config(bg='#EAF2FB')
            else:  # tie
                self.player_tile.config(bg=pulse_colors[i])
                self.computer_tile.config(bg=pulse_colors[i])
            if i < steps - 1:
                self.root.after(interval, lambda: step(i+1))
            else:
                self.root.after(200, self.reset_tile_highlights)
        step(0)

    def animate_vs_label(self):
        # Animate VS label: scale up and flash color
        vs_colors = ['#E74C3C', '#F1C40F', '#E74C3C', '#F1C40F', '#E74C3C']
        vs_fonts = [("Arial", 24, "bold"), ("Arial", 32, "bold"), ("Arial", 40, "bold"), ("Arial", 32, "bold"), ("Arial", 24, "bold")]
        steps = len(vs_colors)
        interval = 1000 // steps
        def step(i):
            self.vs_label.config(fg=vs_colors[i], font=vs_fonts[i])
            if i < steps - 1:
                self.root.after(interval, lambda: step(i+1))
            else:
                self.vs_label.config(fg='#E74C3C', font=("Arial", 24, "bold"))
        step(0)

    def show_results(self):
        self.show_results_phase()
        if self.player_score > self.computer_score:
            result_text = "Congratulations! You won the Animal Fighter game! 🏆"
        elif self.computer_score > self.player_score:
            result_text = "Sorry, the computer won. Better luck next time! 🤖"
        else:
            result_text = "It's a draw! Well fought! 🤝"
        self.results_title.config(text=result_text)
        self.final_scores.config(
            text=f"Final Score - You: {self.player_score} | Computer: {self.computer_score}")
        # Ensure results screen is visible and buttons are enabled
        self.rematch_btn.config(state='normal')
        self.exit_btn.config(state='normal')

    def rematch(self):
        self.player_animals = []
        self.computer_animals = []
        self.battle_index = 0
        self.player_score = 0
        self.computer_score = 0
        self.randomize_animal_values()
        self.show_selection_phase()
        self.start_battle_btn.config(state='disabled')
        # Reset score label for new game
        if hasattr(self, 'score_label'):
            self.score_label.config(text="You: 0 🏆   |   Computer: 0 🤖")

    def exit_game(self):
        self.root.destroy()

    def reset_tile_highlights(self):
        self.player_tile.config(bg='#EAF2FB', bd=8)
        self.computer_tile.config(bg='#EAF2FB', bd=8)

    def animate_result_text(self):
        # Simple scale/fade animation by changing font size and color intensity
        font_sizes = [14, 16, 18, 20, 18, 16, 18]
        colors = ['#F1C40F', '#F7DC6F', '#F1C40F', '#F39C12', '#F1C40F', '#F7DC6F', '#F1C40F']
        steps = len(font_sizes)
        def step(i):
            self.battle_display.config(state='normal')
            self.battle_display.tag_configure('result', font=("Segoe UI", font_sizes[i], "bold"), foreground=colors[i])
            self.battle_display.config(state='disabled')
            if i < steps - 1:
                self.root.after(60, lambda: step(i+1))
        step(0)

def main():
    root = tk.Tk()
    app = AnimalFighterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
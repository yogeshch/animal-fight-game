import tkinter as tk
from tkinter import ttk, messagebox
import random

class EmojiFighterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Emoji Fighter - Animal Edition")
        self.root.geometry("800x600")
        self.root.configure(bg='#2C3E50')
        
        # Animal emojis with randomized values
        self.animal_emojis = [
            '🦁', '🐯', '🐻', '🐺', '🦊', '🐸', '🐵', '🐨', '🐼', '🐷',
            '🐮', '🐷', '🐸', '🐙', '🦈', '🐊', '🦖', '🦕', '🦅', '🦉'
        ]
        
        # Game state
        self.player_emojis = []
        self.computer_emojis = []
        self.emoji_values = {}
        self.game_phase = "selection"  # "selection", "battle", "results"
        self.current_selection = 0
        
        self.setup_ui()
        self.randomize_emoji_values()
        
    def randomize_emoji_values(self):
        """Randomize emoji values for each new game."""
        values = list(range(1, 21))
        random.shuffle(values)
        self.emoji_values = {emoji: value for emoji, value in zip(self.animal_emojis, values)}
        
    def setup_ui(self):
        """Setup the main UI components."""
        # Title
        title_label = tk.Label(
            self.root, 
            text="🐾 Emoji Fighter - Animal Edition 🐾", 
            font=("Arial", 24, "bold"),
            bg='#2C3E50',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Main frame
        self.main_frame = tk.Frame(self.root, bg='#2C3E50')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Selection phase UI
        self.setup_selection_ui()
        
        # Battle phase UI (initially hidden)
        self.setup_battle_ui()
        
        # Results phase UI (initially hidden)
        self.setup_results_ui()
        
        # Show selection phase initially
        self.show_selection_phase()
        
    def setup_selection_ui(self):
        """Setup the emoji selection UI."""
        self.selection_frame = tk.Frame(self.main_frame, bg='#2C3E50')
        
        # Instructions
        instructions = tk.Label(
            self.selection_frame,
            text="Select 5 animal emojis for battle!",
            font=("Arial", 16),
            bg='#2C3E50',
            fg='white'
        )
        instructions.pack(pady=10)
        
        # Progress
        self.progress_label = tk.Label(
            self.selection_frame,
            text="Selection: 0/5",
            font=("Arial", 14),
            bg='#2C3E50',
            fg='#3498DB'
        )
        self.progress_label.pack(pady=5)
        
        # Emoji grid
        self.emoji_frame = tk.Frame(self.selection_frame, bg='#2C3E50')
        self.emoji_frame.pack(pady=20)
        
        # Create emoji buttons in a 5x4 grid
        for i, emoji in enumerate(self.animal_emojis):
            row = i // 5
            col = i % 5
            
            btn = tk.Button(
                self.emoji_frame,
                text=emoji,
                font=("Arial", 24),
                width=3,
                height=2,
                bg='#34495E',
                fg='white',
                relief='raised',
                command=lambda e=emoji: self.select_emoji(e)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
            
        # Selected emojis display
        self.selected_frame = tk.Frame(self.selection_frame, bg='#2C3E50')
        self.selected_frame.pack(pady=20)
        
        self.selected_label = tk.Label(
            self.selected_frame,
            text="Your selected emojis: ",
            font=("Arial", 14),
            bg='#2C3E50',
            fg='white'
        )
        self.selected_label.pack()
        
        # Start battle button (initially disabled)
        self.start_battle_btn = tk.Button(
            self.selection_frame,
            text="Start Battle!",
            font=("Arial", 16, "bold"),
            bg='#E74C3C',
            fg='white',
            command=self.start_battle,
            state='disabled'
        )
        self.start_battle_btn.pack(pady=20)
        
    def setup_battle_ui(self):
        """Setup the battle UI."""
        self.battle_frame = tk.Frame(self.main_frame, bg='#2C3E50')
        
        # Battle title
        battle_title = tk.Label(
            self.battle_frame,
            text="🐾 BATTLE TIME! 🐾",
            font=("Arial", 20, "bold"),
            bg='#2C3E50',
            fg='#E74C3C'
        )
        battle_title.pack(pady=10)
        
        # Battle display
        self.battle_display = tk.Text(
            self.battle_frame,
            height=15,
            width=60,
            font=("Courier", 12),
            bg='#34495E',
            fg='white',
            wrap='word'
        )
        self.battle_display.pack(pady=10, padx=20)
        
        # Battle button
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
        """Setup the results UI."""
        self.results_frame = tk.Frame(self.main_frame, bg='#2C3E50')
        
        # Results title
        self.results_title = tk.Label(
            self.results_frame,
            text="",
            font=("Arial", 24, "bold"),
            bg='#2C3E50',
            fg='white'
        )
        self.results_title.pack(pady=20)
        
        # Final scores
        self.final_scores = tk.Label(
            self.results_frame,
            text="",
            font=("Arial", 16),
            bg='#2C3E50',
            fg='white'
        )
        self.final_scores.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(self.results_frame, bg='#2C3E50')
        button_frame.pack(pady=30)
        
        # Rematch button
        self.rematch_btn = tk.Button(
            button_frame,
            text="Play Again",
            font=("Arial", 16, "bold"),
            bg='#27AE60',
            fg='white',
            command=self.rematch
        )
        self.rematch_btn.pack(side='left', padx=10)
        
        # Exit button
        self.exit_btn = tk.Button(
            button_frame,
            text="Exit Game",
            font=("Arial", 16, "bold"),
            bg='#E74C3C',
            fg='white',
            command=self.exit_game
        )
        self.exit_btn.pack(side='left', padx=10)
        
    def show_selection_phase(self):
        """Show the selection phase."""
        self.battle_frame.pack_forget()
        self.results_frame.pack_forget()
        self.selection_frame.pack(expand=True, fill='both')
        
    def show_battle_phase(self):
        """Show the battle phase."""
        self.selection_frame.pack_forget()
        self.results_frame.pack_forget()
        self.battle_frame.pack(expand=True, fill='both')
        
    def show_results_phase(self):
        """Show the results phase."""
        self.selection_frame.pack_forget()
        self.battle_frame.pack_forget()
        self.results_frame.pack(expand=True, fill='both')
        
    def select_emoji(self, emoji):
        """Handle emoji selection."""
        if emoji not in self.player_emojis and len(self.player_emojis) < 5:
            self.player_emojis.append(emoji)
            self.current_selection = len(self.player_emojis)
            self.update_selection_display()
            
            if len(self.player_emojis) == 5:
                self.start_battle_btn.config(state='normal')
                
    def update_selection_display(self):
        """Update the selection display."""
        self.progress_label.config(text=f"Selection: {len(self.player_emojis)}/5")
        self.selected_label.config(text=f"Your selected emojis: {' '.join(self.player_emojis)}")
        
    def start_battle(self):
        """Start the battle phase."""
        # Computer selects 5 random emojis
        self.computer_emojis = random.sample(self.animal_emojis, 5)
        
        # Initialize battle variables
        self.current_round = 0
        self.player_score = 0
        self.computer_score = 0
        
        self.show_battle_phase()
        self.battle_display.delete(1.0, tk.END)
        self.battle_display.insert(tk.END, "🐾 BATTLE BEGINS! 🐾\n\n")
        self.battle_display.insert(tk.END, f"Your team: {' '.join(self.player_emojis)}\n")
        self.battle_display.insert(tk.END, f"Computer's team: {' '.join(self.computer_emojis)}\n\n")
        self.battle_display.insert(tk.END, "Press 'Next Round' to start the battle!\n")
        
    def next_battle_round(self):
        """Process the next battle round."""
        if self.current_round < 5:
            player_emoji = self.player_emojis[self.current_round]
            computer_emoji = self.computer_emojis[self.current_round]
            player_value = self.emoji_values[player_emoji]
            computer_value = self.emoji_values[computer_emoji]
            
            # Display round
            self.battle_display.insert(tk.END, f"\n--- Round {self.current_round + 1} ---\n")
            self.battle_display.insert(tk.END, f"{player_emoji} ({player_value}) vs {computer_emoji} ({computer_value})\n")
            
            # Determine winner
            if player_value > computer_value:
                self.battle_display.insert(tk.END, f"🎉 {player_emoji} wins this round!\n")
                self.player_score += 1
            elif computer_value > player_value:
                self.battle_display.insert(tk.END, f"💥 {computer_emoji} wins this round!\n")
                self.computer_score += 1
            else:
                self.battle_display.insert(tk.END, "🤝 It's a tie!\n")
                
            self.current_round += 1
            
            # Update button text
            if self.current_round < 5:
                self.next_round_btn.config(text=f"Next Round ({self.current_round + 1}/5)")
            else:
                self.next_round_btn.config(text="See Results", command=self.show_results)
                
        # Auto-scroll to bottom
        self.battle_display.see(tk.END)
        
    def show_results(self):
        """Show the final results."""
        self.show_results_phase()
        
        # Determine winner
        if self.player_score > self.computer_score:
            result_text = "🎉 CONGRATULATIONS! YOU WON! 🎉"
            color = '#27AE60'
        elif self.computer_score > self.player_score:
            result_text = "😔 Computer wins! Better luck next time!"
            color = '#E74C3C'
        else:
            result_text = "🤝 It's a draw! Well fought!"
            color = '#F39C12'
            
        self.results_title.config(text=result_text, fg=color)
        self.final_scores.config(text=f"Final Score:\nYou: {self.player_score} | Computer: {self.computer_score}")
        
    def rematch(self):
        """Start a new game."""
        # Reset game state
        self.player_emojis = []
        self.computer_emojis = []
        self.current_selection = 0
        self.game_phase = "selection"
        
        # Randomize emoji values for new game
        self.randomize_emoji_values()
        
        # Reset UI
        self.progress_label.config(text="Selection: 0/5")
        self.selected_label.config(text="Your selected emojis: ")
        self.start_battle_btn.config(state='disabled')
        self.next_round_btn.config(text="Next Round", command=self.next_battle_round)
        
        # Show selection phase
        self.show_selection_phase()
        
    def exit_game(self):
        """Exit the game."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

def main():
    root = tk.Tk()
    app = EmojiFighterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
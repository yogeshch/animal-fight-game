
import random

# A dictionary of emojis and their assigned values
EMOJIS = {
    '😀': 10, '😂': 12, '😍': 15, '🤔': 8, '😎': 18,
    '😭': 5, '😡': 13, '🤯': 20, '😴': 2, '🥳': 17,
    '😇': 16, '😈': 14, '👻': 9, '👽': 11, '🤖': 19,
    '👾': 7, '🤡': 6, '🤠': 4, '🧐': 3, '💀': 1
}

def get_emoji_list():
    """Returns the list of available emojis."""
    return list(EMOJIS.keys())

def get_player_selection(emoji_list):
    """Gets the player's emoji selection."""
    print("Select 5 emojis from the following list:")
    for i, emoji in enumerate(emoji_list, 1):
        print(f"{i}. {emoji}", end='  ')
        if i % 5 == 0:
            print()
    print()

    player_choices = []
    while len(player_choices) < 5:
        try:
            prompt = f"Enter the number for your emoji choice ({len(player_choices) + 1}/5): "
            choice_input = input(prompt)
            if not choice_input:
                print("Invalid input. Please enter a number.")
                continue
            choice = int(choice_input)
            if 1 <= choice <= len(emoji_list):
                selected_emoji = emoji_list[choice - 1]
                if selected_emoji not in player_choices:
                    player_choices.append(selected_emoji)
                else:
                    print("You have already selected that emoji. Please choose another one.")
            else:
                print(f"Invalid choice. Please select a number between 1 and {len(emoji_list)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return player_choices

def get_computer_selection(emoji_list):
    """Gets the computer's random emoji selection."""
    return random.sample(emoji_list, 5)

def reveal_and_compare(player_emojis, computer_emojis):
    """Reveals the values and compares the emojis to determine the winner."""
    player_score = 0
    computer_score = 0

    print("\n--- Emoji Battle ---")
    print("Player's Emojis vs. Computer's Emojis")
    print("-" * 30)

    for i in range(5):
        player_emoji = player_emojis[i]
        computer_emoji = computer_emojis[i]
        player_value = EMOJIS[player_emoji]
        computer_value = EMOJIS[computer_emoji]

        print(f"Round {i+1}: {player_emoji} ({player_value}) vs. {computer_emoji} ({computer_value})")

        if player_value > computer_value:
            print(f"  {player_emoji} wins this round!")
            player_score += 1
        elif computer_value > player_value:
            print(f"  {computer_emoji} wins this round!")
            computer_score += 1
        else:
            print("  It's a tie!")

    print("\n--- Final Results ---")
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

    if player_score > computer_score:
        print("\nCongratulations! You won the Emoji Fighter game! 🥳")
    elif computer_score > player_score:
        print("\nSorry, the computer won. Better luck next time! 🤖")
    else:
        print("\nIt's a draw! Well fought! 🤝")

def main():
    """Main function to run the game."""
    print("Welcome to Emoji Fighter!")
    emoji_list = get_emoji_list()
    player_emojis = get_player_selection(emoji_list)
    computer_emojis = get_computer_selection(emoji_list)

    print("\nYour selected emojis:", ' '.join(player_emojis))
    print("Computer's selected emojis:", ' '.join(computer_emojis))

    reveal_and_compare(player_emojis, computer_emojis)

if __name__ == "__main__":
    main()

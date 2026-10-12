import random

def get_player_move():
    while True:
        move = input("Enter your move (Rock, Paper, Scissors): ").strip().capitalize()
        if move in ["Rock", "Paper", "Scissors"]:
            return move
        print("Invalid choice. Please try again.")

def ai_move(player_history):
    if not player_history:
        return random.choice(["Rock", "Paper", "Scissors"])
    
    frequencies = {"Rock": 0, "Paper": 0, "Scissors": 0}
    for move in player_history:
        if move in frequencies:
            frequencies[move] += 1
            
    most_frequent_move = max(frequencies, key=frequencies.get)
    
    counters = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }
    return counters[most_frequent_move]

def determine_winner(player_move, ai_move_choice):
    if player_move == ai_move_choice:
        return "Tie"
    
    winning_combinations = {
        ("Rock", "Scissors"),
        ("Scissors", "Paper"),
        ("Paper", "Rock")
    }
    
    if (player_move, ai_move_choice) in winning_combinations:
        return "Player"
    else:
        return "AI"

def play_game():
    player_score = 0
    ai_score = 0
    player_history = []
    
    print("Welcome to Rock, Paper, Scissors against an Adaptive AI!")
    
    while True:
        player_move = get_player_move()
        ai_move_choice = ai_move(player_history)
        
        player_history.append(player_move)
        
        print(f"\nYou played: {player_move}")
        print(f"AI played: {ai_move_choice}")
        
        result = determine_winner(player_move, ai_move_choice)
        
        if result == "Player":
            print("You win this round!")
            player_score += 1
        elif result == "AI":
            print("AI wins this round!")
            ai_score += 1
        else:
            print("This round is a tie!")
            
        print(f"Current Score -> Player: {player_score} | AI: {ai_score}\n")
        
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\nFinal Results:")
            print(f"Player Score: {player_score}")
            print(f"AI Score: {ai_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()

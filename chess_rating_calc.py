def calculate_elo_change(player_rating, opponent_rating, result, k_factor=32):
    """
    Calculate the Elo rating change for a chess game.
    
    Args:
        player_rating: Current Elo rating of the player
        opponent_rating: Current Elo rating of the opponent
        result: Game result (1 for win, 0.5 for draw, 0 for loss)
        k_factor: K-factor (determines rating volatility, default 32)
    
    Returns:
        New rating after the game
    """
    expected_score = 1 / (1 + 10 ** ((opponent_rating - player_rating) / 400))
    rating_change = k_factor * (result - expected_score)
    new_rating = player_rating + rating_change
    
    return round(new_rating, 1)


def main():
    print("Chess Rating Calculator (Elo System)\n")
    
    player_rating = float(input("Enter your current rating: "))
    num_games = int(input("How many games did you play in the tournament? "))
    
    k_factor = int(input("Enter K-factor (default 32): ") or "32")
    
    total_rating_change = 0
    
    for i in range(1, num_games + 1):
        print(f"\n--- Game {i} ---")
        opponent_rating = float(input("Enter opponent's rating: "))
        
        print("Game result: 1=Win, 0.5=Draw, 0=Loss")
        result = float(input("Enter result: "))
        
        new_rating = calculate_elo_change(player_rating, opponent_rating, result, k_factor)
        rating_change = new_rating - player_rating
        total_rating_change += rating_change
        player_rating = new_rating
        
        print(f"New rating after game {i}: {new_rating}")
    
    final_rating = player_rating
    print(f"\nTournament Summary:")
    print(f"Final rating: {final_rating}")
    print(f"Total change: {total_rating_change:+.1f}")


if __name__ == "__main__":
    main()
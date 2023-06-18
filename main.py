from team import team1, team2
from outcome import simulate_shot_attempt
from stats import export_statistics, final_stats
from match import simulate_quidditch_match

# Simulate the Quidditch match
simulate_quidditch_match(team1, team2)

#Print the player's final stats
final_stats(team1, team2)

# Export statistics to a CSV file
export_statistics(team1, team2)
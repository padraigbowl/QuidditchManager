# Quidditch Manager

Quidditch Manager is a Python project that simulates a Quidditch match between two teams and generates statistics for the game results. The simulator implements the rules and gameplay mechanics of the fictional sport Quidditch from the Harry Potter series.

## How to Run the Simulator

1. Ensure that you have Python installed on your system.
2. Download the following repository: https://github.com/padraigbowl/QuidditchManager
3. Run Python and navigate to the directory where you saved the downloaded files 
3. Run the 'main.py' script to start the simulation.

## How the Simulator Works

1. The simulator begins by initializing the game settings and player statistics for each team.
2. The match starts, and the possession is assigned to one of the teams.
3. The simulator simulates shot attempts by randomly selecting an initial chaser from the team in possession and determining the outcome (goal, save, catch, or miss) based on weights assigned to each outcome.
4. The outcome of the shot attempt is displayed, and relevant statistics are updated accordingly.
5. Possession may change depending on the outcome of the shot attempt. Possession will turnover when a goal is scored or the quaffle is caught. If the shot is saved or missed, the next team in possession will be selected randomly
6. The simulator checks if the snitch is caught based on a catch probability. If caught, the game ends.
7. The probability of the snitch being caught increases with each unsuccessful attempt.
8. Steps 3-7 are repeated until the snitch is caught.
9. The simulator displays the final scores and generates statistics for each player of each team.
10. The simulation ends.

## Game Statistics

The simulator generates various statistics for each team and player, including goals, assists, shots, shots missed, shots saved, shots caught, and goals conceded by the keepers. These statistics provide insights into the performance of individual players and the overall performance of the teams.

A CSV file will be generated of the game statistics for further analysis.

## Customization

To customize the simulation further, you can modify the weights assigned to different outcomes in the `simulate_shot_attempt` function. Adjusting these weights will affect the likelihood of goals, saves, catches, and misses, which can impact the game dynamics and final results.

Feel free to experiment with different team compositions, player attributes, and weights to create unique scenarios and explore the possibilities of the Quidditch Manager Simulator.

Enjoy simulating and managing your Quidditch matches!

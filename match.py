import random
import time

from outcome import simulate_shot_attempt

# Function to simulate the Quidditch match
def simulate_quidditch_match(team1, team2):
    print(f"Quidditch Match: {team1['name']} vs. {team2['name']}")
    print("----- GAME START -----")

    snitch_caught = False
    catch_probability = 0.0005
    possession = team1
    current_team = possession


    while not snitch_caught:
        possession_change = False

        # Simulate shot attempts for the current team in possession
        outcome = simulate_shot_attempt(current_team, team1 if current_team == team2 else team2)
        if outcome == 'goal' or outcome == 'catch':
            possession_change = True
        elif outcome == 'save' or outcome == 'miss':
            possession_change = random.choice([True, False])
        #time.sleep(0.5)

        # Check if the snitch is caught
        if random.random() <= catch_probability:
            snitch_caught = True
            snitch_catcher = current_team['seeker']
            current_team['score'] += 150
            print(f"The Snitch is caught by {snitch_catcher['name']} from {current_team['name']}!")
            break

        # Change possession to the other team
        if possession_change:
            possession = team1 if current_team == team2 else team2
        current_team = possession

        # Increase catch probability with each unsuccessful attempt
        catch_probability += 0.0005

    print("----- GAME OVER -----")
    print(f"{team1['name']} score: {team1['score']} points")
    print(f"{team2['name']} score: {team2['score']} points")

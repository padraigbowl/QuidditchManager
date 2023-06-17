import random
import time
from team import team1, team2

# Function to simulate a shot attempt
def simulate_shot_attempt(current_team, opposing_team):
    chaser = random.choice(current_team['chasers'])
    outcome = random.choices(['goal', 'save', 'catch', 'miss'], weights=[chaser['goal_weight'], current_team['keeper']['save_weight'], current_team['keeper']['catch_weight'], 0.2])[0]
    assisting_chaser = None  # Initialize the assisting chaser to None

    if outcome == 'goal':
        current_team['score'] += 10
        chaser['goals'] += 1
        # Choose a random assisting chaser from the same team
        assisting_chaser = random.choice(current_team['chasers'])
        assisting_chaser['assists'] += 1

    chaser['shots'] += 1
    chaser['attempts'][outcome] += 1

    print(f"{current_team['name']} have possession")
    print(f"Shot attempt by {chaser['name']} from {current_team['name']}")

    if outcome == 'goal':
        print(f"Goal scored by {chaser['name']} from {current_team['name']}!")
        if assisting_chaser:
            print(f"Assist by {assisting_chaser['name']} from {current_team['name']}!")
    elif outcome == 'save':
        print(f"Shot saved by {opposing_team['keeper']['name']} from {opposing_team['name']}!")
        opposing_team['keeper']['saves'] += 1
    elif outcome == 'catch':
        print(f"Quaffle caught by {opposing_team['keeper']['name']} from {opposing_team['name']}!")
        opposing_team['keeper']['catches'] += 1
    else:
        print(f"Shot missed by {chaser['name']} from {current_team['name']}")

    print(f"-----")
    print(f"{current_team['name']} score: {current_team['score']} points")
    print(f"{opposing_team['name']} score: {opposing_team['score']} points")
    print("-----")

    return outcome


# Function to simulate the Quidditch match
def simulate_quidditch_match(team1, team2):
    print(f"Quidditch Match: {team1['name']} vs. {team2['name']}")
    print("----- GAME START -----")

    snitch_caught = False
    catch_probability = 0.0005
    possession = team1
    current_team = possession

    # Initialize goal tally, shot attempts, and assists for each chaser
    for chaser in team1['chasers'] + team2['chasers']:
        chaser['goals'] = 0
        chaser['shots'] = 0
        chaser['assists'] = 0  # Initialize assists
        chaser['attempts'] = {'goal': 0, 'save': 0, 'catch': 0, 'miss': 0}

    # Initialize save and catch statistics for each keeper
    for team in [team1, team2]:
        team['keeper']['saves'] = 0
        team['keeper']['catches'] = 0

    while not snitch_caught:
        possession_change = False

        # Simulate shot attempts for the current team in possession
        outcome = simulate_shot_attempt(current_team, team1 if current_team == team2 else team2)
        if outcome == 'goal' or outcome == 'catch':
            possession_change = True
        elif outcome == 'save' or outcome == 'miss':
            possession_change = random.choice([True, False])
        #time.sleep(1)

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

    # Print chaser shot attempt statistics
    print("\nChaser Statistics:")
    for team in [team1, team2]:
        print(f"{team['name']}:")
        for chaser in team['chasers']:
            print(f"{chaser['name']}:")
            print(f"  Goals: {chaser['goals']}")
            print(f"  Assists: {chaser['assists']}")
            print(f"  Shots: {chaser['shots']}")
            print(f"  Shots Missed: {chaser['attempts']['miss']}")
            print(f"  Shots Saved: {chaser['attempts']['save']}")
            print(f"  Shots Caught: {chaser['attempts']['catch']}")

    # Calculate goals conceded by each keeper
    for team in [team1, team2]:
        opposing_team = team2 if team == team1 else team1
        goals_conceded = sum(chaser['goals'] for chaser in opposing_team['chasers'])
        team['keeper']['goals_conceded'] = goals_conceded

    # Print keeper shot attempt statistics
    print("\nKeeper Statistics:")
    for team in [team1, team2]:
        print(f"{team['name']}:")
        print(f"{team['keeper']['name']}:")
        print(f"  Saves: {team['keeper']['saves']}")
        print(f"  Catches: {team['keeper']['catches']}")
        print(f"  Goals Conceded: {team['keeper']['goals_conceded']}")

# Simulate the Quidditch match
simulate_quidditch_match(team1, team2)


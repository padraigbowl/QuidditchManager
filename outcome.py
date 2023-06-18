import random

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


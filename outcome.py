import random

def simulate_shot_attempt(current_team, opposing_team):
    chaser = random.choice(current_team['chasers'])
    outcome = random.choices(['goal', 'save', 'catch', 'miss'], weights=[chaser['goal_weight'], current_team['keeper']['save_weight'], current_team['keeper']['catch_weight'], 0.2])[0]
    if outcome == 'goal':
        current_team['score'] += 10
        print(f"{current_team['name']} have possession")
        print(f"Goal scored by {chaser['name']} from {current_team['name']}!")
        print(f"-----")
        print(f"{current_team['name']} score: {current_team['score']} points")
        print(f"{opposing_team['name']} score: {opposing_team['score']} points")
        print("-----")
        return 'goal'
    elif outcome == 'save':
        print(f"{current_team['name']} have possession")
        print(f"Shot attempt by {chaser['name']} from {current_team['name']}")
        print(f"Shot saved by {opposing_team['keeper']['name']} from {opposing_team['name']}!")
        return 'save'
    elif outcome == 'catch':
        print(f"{current_team['name']} have possession")
        print(f"Shot attempt by {chaser['name']} from {current_team['name']}")
        print(f"Quaffle caught by {opposing_team['keeper']['name']} from {opposing_team['name']}!")
        return 'catch'
    else:
        print(f"{current_team['name']} have possession")
        print(f"Shot missed by {chaser['name']} from {current_team['name']}")
        return 'miss'


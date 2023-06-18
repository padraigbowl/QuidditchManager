import random
import time

#Simulate the outcome of each possession
def simulate_shot_attempt(current_team, opposing_team):
    chasers = current_team['chasers']
    passing_chaser = random.choice(chasers)
    assisting_chaser = None
    print(f"Quaffle is with {current_team['chasers'][0]['name']} from {current_team['name']}")
    # Determine the number of passes before the shot attempt
    num_passes = random.randint(0, 7)

    # Simulate passing the Quaffle between chasers
    for _ in range(num_passes):
        for chaser in chasers:
            if chaser != passing_chaser:
                passing_success = random.choices([True, False], weights=[0.8, 0.2])[0]  # Adjust passing success probability as desired
                if passing_success:
                    assisting_chaser = chaser
                    print(f"Pass from {passing_chaser['name']} to {assisting_chaser['name']}")
                    time.sleep(0.5)
                    passing_chaser = assisting_chaser
                    break
        else:
            # If no successful pass, possession changes to the opposing team
            current_team, opposing_team = opposing_team, current_team
            print("Pass failed. Possession changes.")
            print(f"{current_team['name']} have possession now.")
            print(f"Quaffle is with {current_team['chasers'][0]['name']} from {current_team['name']}")

    chaser = passing_chaser

    outcome = random.choices(['goal', 'save', 'catch', 'miss'], weights=[chaser['goal_weight'], current_team['keeper']['save_weight'], current_team['keeper']['catch_weight'], 0.2])[0]

    if outcome == 'goal':
        current_team['score'] += 10
        chaser['goals'] += 1
        if assisting_chaser:
            assisting_chaser['assists'] += 1

    chaser['shots'] += 1
    chaser['attempts'][outcome] += 1


    print(f"Quaffle is with {chaser['name']} from {current_team['name']}")

    if assisting_chaser:
        chaser = assisting_chaser

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
        possession = opposing_team
        current_team = possession
        print(f"{opposing_team['name']} have possession now.")
        print(f"Quaffle is with {opposing_team['keeper']['name']} from {opposing_team['name']}")

    print(f"-----")
    print(f"{current_team['name']} score: {current_team['score']} points")
    print(f"{opposing_team['name']} score: {opposing_team['score']} points")
    print("-----")

    return outcome


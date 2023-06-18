import csv

def export_statistics(team1, team2):
    filename = 'quidditch_stats.csv'

    # Prepare the data for CSV export
    chaser_data = [['Team', 'Chaser', 'Goals', 'Assists', 'Shots', 'Shots Missed', 'Shots Saved', 'Shots Caught']]
    keeper_data = [['Team', 'Keeper', 'Saves', 'Catches', 'Goals Conceded']]

    # Add chaser statistics
    for team in [team1, team2]:
        for chaser in team['chasers']:
            chaser_row = [
                team['name'],
                chaser['name'],
                chaser['goals'],
                chaser['assists'],
                chaser['shots'],
                chaser['attempts']['miss'],
                chaser['attempts']['save'],
                chaser['attempts']['catch']
            ]
            chaser_data.append(chaser_row)

    # Add keeper statistics
    for team in [team1, team2]:
        keeper_row = [
            team['name'],
            team['keeper']['name'],
            team['keeper']['saves'],
            team['keeper']['catches'],
            team['keeper']['goals_conceded']

        ]
        keeper_data.append(keeper_row)

    # Export the data to CSV
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(chaser_data)
        writer.writerow([])  # Add an empty row as separator
        writer.writerows(keeper_data)

    print(f"Statistics exported to {filename} successfully.")

def final_stats(team1,team2):
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
  
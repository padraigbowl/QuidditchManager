import random

# Player Class
class Player:
    def __init__(self, name, position, skill_level, stamina):
        self.name = name
        self.position = position
        self.skill_level = skill_level
        self.stamina = stamina

    def move(self):
        # Logic for player movement
        pass


# Subclasses for Each Position
class Keeper(Player):
    def save_shot(self):
        # Logic for saving shots from opposing chasers
        pass

class Beater(Player):
    def hit_bludger(self):
        # Logic for hitting bludgers towards opposing players
        pass

class Chaser(Player):
    def pass_quaffle(self):
        # Logic for passing the quaffle to other chasers
        pass

    def attempt_pass(self, receiver):
        # Logic for attempting a pass to another chaser
        pass_success = random.randint(0, 9) < self.skill_level
        return pass_success
    
    def attempt_shot(self):
        shot_success = random.random() < self.skill_level
        return shot_success


    def score_goal(self):
        # Logic for attempting to score goals against the opposing team's keeper
        pass

class Seeker(Player):
    def seek_snitch(self):
        # Logic for trying to catch the snitch, which ends the game
        pass

# Quidditch Game Simulator
class QuidditchGameSimulator:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.current_possession = random.choice([team1, team2])  # Randomly assign possession to start

    def start_game(self):
        print("Starting the Quidditch game!")
        # Initialize game state and other setup logic

    def change_possession(self):
        if self.current_possession == self.team1:
            self.current_possession = self.team2
        else:
            self.current_possession = self.team1

    def play_by_play(self):
        while True:
            # Play-by-play logic, including player actions based on possession
            print("New possession")
            if self.current_possession == self.team1:
                passer = random.choice(self.team1.chasers)
                opposing_chaser = random.choice(self.team2.chasers)
            else:
                passer = random.choice(self.team2.chasers)
                opposing_chaser = random.choice(self.team1.chasers)

            print(f"{self.current_possession.name} has the quaffle.")
            print(f"{passer.name} has possession.")

            # Attempt pass between chasers
            receiver = random.choice([chaser for chaser in self.current_possession.chasers if chaser != passer])
            pass_success = passer.attempt_pass(receiver)

            if pass_success:
                print(f"{passer.name} passes to {receiver.name}. Pass is successful.")
                num_passes = random.randint(0, 9)
                for _ in range(num_passes):
                    passer = receiver
                    receiver = random.choice([chaser for chaser in self.current_possession.chasers if chaser != passer])
                    pass_success = passer.attempt_pass(receiver)

                    if not pass_success:
                        # Pass failed, break the passing loop
                        break
                    else:
                        print(f"{passer.name} passes to {receiver.name}. Pass is successful.")

            if pass_success:
                # Successful pass, attempt a shot
                print(f"{receiver.name} attempts a shot.")
                passer.attempt_shot()
                print(f"{self.current_possession.name} scores a goal!")
                self.current_possession = self.team2 if self.current_possession == self.team1 else self.team1

            else:
                # Pass failed, change possession and select a chaser from the opposing team
                print(f"{passer.name} passes to {receiver.name}. Pass fails. Possession changes.")
                self.current_possession = self.team2 if self.current_possession == self.team1 else self.team1

            # Check for snitch catch condition and end the game if necessary
            if self.check_snitch_caught():
                break



    def check_snitch_caught(self):
        # Get the seekers from both teams
        seeker1 = self.team1.seeker
        seeker2 = self.team2.seeker

        # Calculate catch chances based on skill levels
        catch_chance_seeker1 = seeker1.skill_level / (seeker1.skill_level + seeker1.stamina)
        catch_chance_seeker2 = seeker2.skill_level / (seeker2.skill_level + seeker2.stamina)

        # Determine the seeker attempting to catch the snitch
        if random.random() < catch_chance_seeker1:
            catching_seeker = seeker1
        else:
            catching_seeker = seeker2

        # Attempt to catch the snitch
        print(f"{catching_seeker.name} is attempting to catch the snitch!")
        if catching_seeker == seeker1:
            non_catching_seeker = seeker2
        else:
            non_catching_seeker = seeker1

        if random.random() < catch_chance_seeker1 / 10:
            print(f"{catching_seeker.name} caught the snitch! Game over.")
            return True
        else:
            print(f"{catching_seeker.name} failed to catch the snitch. The game continues.")
            return False

# Team Class
class Team:
    def __init__(self, name, keeper, beaters, chasers, seeker):
        self.name = name
        self.keeper = keeper
        self.beaters = beaters
        self.chasers = chasers
        self.seeker = seeker


# Create players for Team 1
keeper1 = Keeper("Keeper 1", "Keeper", skill_level=8, stamina=9)
beater1 = Beater("Beater 1", "Beater", skill_level=7, stamina=8)
beater2 = Beater("Beater 2", "Beater", skill_level=6, stamina=7)
chaser1 = Chaser("Chaser 1", "Chaser", skill_level=9, stamina=9)
chaser2 = Chaser("Chaser 2", "Chaser", skill_level=8, stamina=8)
chaser3 = Chaser("Chaser 3", "Chaser", skill_level=7, stamina=7)
seeker1 = Seeker("Seeker 1", "Seeker", skill_level=10, stamina=10)

team1 = Team("Team 1", keeper1, [beater1, beater2], [chaser1, chaser2, chaser3], seeker1)

# Create players for Team 2
keeper2 = Keeper("Keeper 2", "Keeper", skill_level=7, stamina=8)
beater3 = Beater("Beater 3", "Beater", skill_level=8, stamina=9)
beater4 = Beater("Beater 4", "Beater", skill_level=7, stamina=8)
chaser4 = Chaser("Chaser 4", "Chaser", skill_level=8, stamina=9)
chaser5 = Chaser("Chaser 5", "Chaser", skill_level=7, stamina=8)
chaser6 = Chaser("Chaser 6", "Chaser", skill_level=6, stamina=7)
seeker2 = Seeker("Seeker 2", "Seeker", skill_level=9, stamina=9)

team2 = Team("Team 2", keeper2, [beater3, beater4], [chaser4, chaser5, chaser6], seeker2)

# Create a game simulator and start the game
game_simulator = QuidditchGameSimulator(team1, team2)
game_simulator.start_game()
game_simulator.play_by_play()

import random
class Player:
    def __init__(self, name, batting, bowling, fielding, running, experience):
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.running = running
        self.experience = experience
class Teams:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = players
    def select_captain(self, captain):
        self.captain = captain
    def send_next_player(self):
        if len(self.batting_order) > 0:
            return self.batting_order.pop(0)
        else:
            return None
    def choose_bowler(self):
        return random.choice(self.players)
    def decide_batting_order(self):
        self.batting_order = self.players.copy()  # Assign all players to the batting order
class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage
class Umpire:
    def __init__(self):
        self.scores = {'team1': 0, 'team2': 0}
        self.wickets = {'team1': 0, 'team2': 0}
        self.overs = 0

    def predict_outcome(self, bowler, batsman):
        # Perform calculations based on player stats, field conditions, etc.
        # Return the outcome of the ball, e.g., "boundary", "out", "no run", etc.
        boundary_chance = batsman.batting * (1 - bowler.fielding)
        out_chance = 1 - (batsman.batting * bowler.bowling)
        no_run_chance = (1 - batsman.batting) * (1 - bowler.bowling)
        outcomes = ['boundary', 'out', 'no run']
        weights = [boundary_chance, out_chance, no_run_chance]
        outcome = random.choices(outcomes, weights=weights)[0]
        if outcome == 'boundary':
            return 4  # Example: Assign 4 runs for a boundary
        elif outcome == 'out':
            return 0  # Example: Assign 0 runs for getting out
        elif outcome == 'no run':
            return 0  # Example: Assign 0 runs for no run
    def update_score(self, runs):
        # Update the score based on the runs scored
        self.scores['team1'] += runs
    def update_wickets(self):
        # Update the wickets count
        self.wickets['team1'] += 1
    def update_overs(self):
        # Update the overs count
        self.overs += 1
class Commentator:
    def __init__(self):
        pass
    def provide_commentary(self, ball_outcome):
        # Generate commentary based on the ball outcome and match stats
        pass
class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire()
        self.commentator = Commentator()
        self.team1.decide_batting_order()
        self.team2.decide_batting_order() 
    def start_match(self):
        self.team1.select_captain(random.choice(self.team1.players))
        self.team2.select_captain(random.choice(self.team2.players))
        # Start the match innings and simulate the game
        while self.umpire.overs < 20:
            bowler = self.team2.choose_bowler()
            batsman = self.team1.send_next_player()
            if batsman is None:
                print("No more batsmen available.")
                break
            ball_outcome = self.umpire.predict_outcome(bowler, batsman)
            self.umpire.update_score(ball_outcome)
            self.umpire.update_wickets()
            self.umpire.update_overs()
            self.commentator.provide_commentary(ball_outcome)
        # End the match and display the final scorecard
        self.display_scorecard()
    def display_scorecard(self):
        print("Dhoni's Team: {} - {}".format(self.team1.name, self.umpire.scores['team1']))
        print("Kane's Team: {} - {}".format(self.team2.name, self.umpire.scores['team2']))
        print("Overs: {}".format(self.umpire.overs))
        print("Wickets: Team 1 - {}, Team 2 - {}".format(self.umpire.wickets['team1'], self.umpire.wickets['team2']))
# Sample usage
player1 = Player("MS Dhoni", 0.8, 2.2, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.9, 2.1, 0.95, 0.7, 0.8)
player3 = Player("Virat Kohli", 0.9, 2.1, 0.95, 0.7, 0.8)
player4 = Player("Virat Kohli", 0.9, 2.1, 0.95, 0.7, 0.8)
player5 = Player("Virat Kohli", 0.9, 2.1, 0.95, 0.7, 0.8)
player6 = Player("Virat Kohli", 0.9, 2.1, 0.95, 0.7, 0.8)
player7 = Player("Virat Kohli", 0.9, 2.1, 0.95, 0.7, 0.8)
team1 = Teams("Dhoni's Team", [player1, player2, player3, player4, player5, player6, player7])
player3 = Player("Kane Williamson", 0.85, 0.15, 0.97, 0.75, 0.9)
player4 = Player("Joe Root", 0.82, 0.18, 0.96, 0.72, 0.85)
team2 = Teams("Kane's Team", [player3, player4])
field = Field("Large", 0.8, "Dry", 0.1)
match = Match(team1, team2, field)
match.start_match()
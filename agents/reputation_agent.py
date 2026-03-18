import json

class ReputationAgent:

    def __init__(self):
        self.scores = {}

    def update_score(self, user, action):
        points = {
            "upload": 10,
            "viral": 50,
            "proposal": 25,
            "teaching": 40
        }

        self.scores[user] = self.scores.get(user, 0) + points.get(action, 0)

    def leaderboard(self):
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    agent = ReputationAgent()
    agent.update_score("user1", "viral")
    print(agent.leaderboard())
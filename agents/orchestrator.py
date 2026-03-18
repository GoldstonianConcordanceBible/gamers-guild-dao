from scout_agent import ScoutAgent
from analyst_agent import AnalystAgent
from reputation_agent import ReputationAgent
from treasury_agent import TreasuryAgent

class Orchestrator:

    def __init__(self):
        self.scout = ScoutAgent()
        self.analyst = AnalystAgent()
        self.reputation = ReputationAgent()
        self.treasury = TreasuryAgent()

    def run_cycle(self):
        trends = self.scout.find_trends()
        insights = self.analyst.analyze(trends)
        self.treasury.optimize(insights)
        print("Cycle complete")

if __name__ == "__main__":
    Orchestrator().run_cycle()
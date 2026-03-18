import time
from agents.orchestrator import Orchestrator

orch = Orchestrator()

while True:
    orch.run_cycle()
    time.sleep(3600)  # hourly cycles
import json, sys
from src.byoc import Environment, plan
for line in sys.stdin:
    if line.strip():
        payload=json.loads(line); approved,reasons=plan(Environment(**payload))
        print(json.dumps({"input":payload,"approved":approved,"reasons":reasons}))

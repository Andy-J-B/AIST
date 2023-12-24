import json

with open("RIIS/data/set.json", "w") as d:
    json.dump({}, d)
with open("RIIS/data/regressionLine.json", "w") as d:
    json.dump(0, d)

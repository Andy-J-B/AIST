import json

with open("data/classification.json", "w") as d:
    json.dump({}, d)
with open("data/set.json", "w") as d:
    json.dump({}, d)
with open("data/cleanUp.json", "w") as d:
    json.dump(0, d)
with open("data/log.txt", "w") as d:
    d.write("")

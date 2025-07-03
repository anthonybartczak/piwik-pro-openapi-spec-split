import json, os

spec = json.load(open("openapi-spec.json"))
os.makedirs("paths", exist_ok=True)

for p, data in spec["paths"].items():
    chunk = {**spec, "paths": {p: data}}
    name  = p.strip("/").replace("/", "_") or "root"
    json.dump(chunk, open(f"paths/{name}.json","w"), indent=2)

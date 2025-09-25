import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
load_dotenv(repo_root / ".env")

API_KEY = os.getenv("SCALESERP_API_KEY")
if not API_KEY:
    raise SystemExit("Error: SCALESERP_API_KEY environment variable not set.")

URL = "https://api.scaleserp.com/search"

# set up the request parameters using documentation
params = {
    "api_key": API_KEY,
    "q": "domino's pizza",
    "location": "Paris,Paris,Ile-de-France,France",
    "device": "mobile",
    "page": 1,
    "num": 20,
}

# call http to the endpoint with 30 sec timeout, else raise error
try:
    resp = requests.get(URL, params=params, timeout=30)
    resp.raise_for_status()
except requests.RequestException as e:
    raise SystemExit(f"Error: {e}")

    # process the response with 2 spaces indentation and save
data = resp.json()
out_path = repo_root / "outputs" / "resultats_scaleserp.json"

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

#print the first 6 keys of the results
print(f"Save to {out_path}")
print("Results Keys:", list(data.keys())[:6])


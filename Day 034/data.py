import requests
from pathlib import Path

root = Path(__file__).parent

API = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get(API, params)
response.raise_for_status()
data = response.json()
question_data = data["results"]

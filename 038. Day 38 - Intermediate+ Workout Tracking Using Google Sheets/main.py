import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

root = Path(__file__).parent
EDAMAM_APPID = os.getenv("EDAMAM_APPID")
EDAMAM_APPKEY = os.getenv("EDAMAM_APPKEY")
SHEETY_API = os.getenv("SHEETY_API")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
edamam_endpoint = "https://api.edamam.com/api/nutrition-data"

# Sheety
sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/foodTracker/food/"


def main():
    prompt = input("What food did you eat today? ")
    food_params = {
        "app_id": EDAMAM_APPID,
        "app_key": EDAMAM_APPKEY,
        "ingr": prompt
    }

    response = requests.get(url=edamam_endpoint, params=food_params)
    response.raise_for_status()
    data = response.json()

    with open(root/"data.json", "w") as f:
        json.dump(obj=data, fp=f, indent=2)

    ingredients = data["ingredients"][0]
    if "parsed" not in ingredients:
        return print(f'Food "{prompt}" not found')

    parsed_data = ingredients["parsed"][0]
    nutrients_data = parsed_data["nutrients"]

    summary = {
        "food": {
            "date": datetime.now().strftime("%m/%d/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "food": parsed_data["food"],
            "quantity": parsed_data["quantity"],
            "measurement": parsed_data["measure"],
            "energy": get_nutrient(nutrients_data, "ENERC_KCAL"),
            "totalFat": get_nutrient(nutrients_data, "FAT"),
            "saturatedFat": get_nutrient(nutrients_data, "FASAT"),
            "transFat": get_nutrient(nutrients_data, "FATRN"),
            "cholesterol": get_nutrient(nutrients_data, "CHOLE"),
            "sodium": get_nutrient(nutrients_data, "NA"),
            "carbohydrates": get_nutrient(nutrients_data, "CHOCDF"),
            "fiber": get_nutrient(nutrients_data, "FIBTG"),
            "sugars": get_nutrient(nutrients_data, "SUGAR"),
            "protein": get_nutrient(nutrients_data, "PROCNT"),
        }
    }

    headers = {
        "Authorization": SHEETY_AUTH,
        "Content-Type": "application/json"
    }

    ### SHEETY ###
    response = requests.post(
        url=sheety_endpoint, json=summary, headers=headers)
    response.raise_for_status()
    if 300 > response.status_code >= 200:
        print("Successfully added to Google Sheets.")


def get_nutrient(nutrients, key):
    return nutrients.get(key, {}).get("quantity") or 0


while True:
    main()

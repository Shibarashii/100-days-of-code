import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
USERNAME = "shiba"
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

# Add user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Add graph
graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Add pixels
add_pixel_endpoint = f"{graph_endpoint}/{graph_params["id"]}"

add_pixel_params = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "2.0"
}


# Update pixels
update_pixel_endpoint = f"{add_pixel_endpoint}/{add_pixel_params["date"]}"
update_pixel_params = {
    "quantity": "4.9"
}

# Delete pixels
delete_pixel_endpoint = update_pixel_endpoint

response = requests.delete(
    url=update_pixel_endpoint, headers=headers)
print(response.text)

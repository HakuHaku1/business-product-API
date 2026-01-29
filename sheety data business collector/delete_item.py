import requests
import os
class Delete():

    def Deleting_data(deleted_item):
        
        hidden_token = os.environ.get("SECRET_AUTH_TOKEN")

        Headers = {
            "Authorization": hidden_token

        }

        URL = "https://api.sheety.co/6c41d3c9c114f6b32ee49fa82549eb71/businessProductApi/sheet1"

        get_response = requests.get(url= URL, headers= Headers )

        finding_data = get_response.json()
        get_response.raise_for_status()

        for index in finding_data["sheet1"]:
            if index["name"] == deleted_item:
                id = index["id"]
                delete_finalization = f"{URL}/{id}"
                delete_data = requests.delete(url= delete_finalization, headers= Headers)
                delete_data.raise_for_status()
                print("successfully deleted")                




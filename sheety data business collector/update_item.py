import requests
import os
class Update():
    def updating_data(update_item, data_selected, user_new_selection):
        
        hidden_token = os.environ.get("SECRET_AUTH_TOKEN")

        Headers = {
            "Authorization": hidden_token

        }

        URL = "https://api.sheety.co/6c41d3c9c114f6b32ee49fa82549eb71/businessProductApi/sheet1"

        get_response = requests.get(url= URL, headers= Headers )

        find_data = get_response.json()
        get_response.raise_for_status()

        for index in find_data["sheet1"]:
            if index["name"] == update_item:
                add_parameter = {
                    "sheet1":{
                            f"{data_selected}": f"{user_new_selection}"
                        }
                    }
                id = index["id"]
                update_finalization = f"{URL}/{id}"
                update_response = requests.put(url= update_finalization,json= add_parameter, headers= Headers)
                update_response.raise_for_status()
                print("successfully updated")                



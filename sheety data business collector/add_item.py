import requests
import os
class Add():

    def Adding_data(add_name, add_category, add_price, add_sold, add_amount, add_last_update):
        
        hidden_token = os.environ.get("SECRET_AUTH_TOKEN")

        headers = {
            "Authorization": hidden_token

        }
        add_parameter = {
            "sheet1":{
                "name":add_name,
                "category":add_category,
                "price":add_price,
                "sold":add_sold,
                "amount":add_amount,
                "lastupdated":add_last_update
            }
        }
        URL = "https://api.sheety.co/6c41d3c9c114f6b32ee49fa82549eb71/businessProductApi/sheet1"

        response_add = requests.post(url= URL,json= add_parameter, headers= headers )
        response_add.raise_for_status()
        if response_add.status_code == 200:
            print("sucessfully added")
        else:
            print("error")

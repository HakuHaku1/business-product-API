from add_item import Add
from delete_item import Delete
from update_item import Update
import datetime as dt
continue_app = True

User_choice = input("Please enter these three selection\n\nAdd\nUpdate\nDelete\n\nSelect: ").lower() 

date = dt.datetime.now().strftime("%m/%d/%Y")

if User_choice == "add":
    name = input("Please enter the name of the product: ").lower() 
    category = input("Please enter the category of the product: ").lower() 
    price = input("Please enter the price of the product: ").lower() 
    sold = input("Please enter the sold of the product: ").lower() 
    amount = input("Please enter the amount of the product: ").lower() 

    Add.Adding_data(name,category,price, sold, amount, date )
elif User_choice == "delete":
    delete_name = input("Please enter the name of the product you want to delete: ").lower() 

    Delete.Deleting_data(delete_name)
elif User_choice == "update":
    Product_name = input("Please enter the product name that you want to update: ").lower() 
    Product_detail = input("\nPlease enter the detail of the product you want to update \n\nname\ncategory\nprice\nsold\namount\n\nselect one: ").lower() 
    User_new_data = input("Please enter the new detail you want to add: ").lower() 
    Update.updating_data(Product_name, Product_detail, User_new_data)
#Grocery management system
grocery_list = []
def add_item(name, quantity, price):
    item = {
        "name": name,
        "quantity": quantity,
        "price" : price,
        "available": True
    }
    grocery_list.append(item)

def remove_item(name):
     for list in grocery_list:
          if list["name"] == name:
               grocery_list.remove(list)
               print(f"{name} has been remove from the list")
               return
          print(f"{name} is not in the list")

def display_items():
    for list in grocery_list:
        print(f"Name: {list['name']}, Quantity: {list['quantity']}, Price: {list['price']}, Available: {list['available']}")

def search_item(search_query):
    found_items = []
    for list in grocery_list:
        if search_query.lower() in list["name"].lower():
            found_items.append(list)
    if found_items:
     for list in found_items:
         print(f"Name: {list['name']}, Quantity: {list['quantity']}, Price: {list['price']}, Available: {list['available']}")
    else:
        print(f"No Item found with the name {search_query}")

def check_out_item(name):
    for list in grocery_list:
        if list["name"] == name:
            if list["available"]:
             list["available"] = False
             print(f"{name} has been checked out")
            else:
             print(f"{name} is not available")
            return
            print(f"{name} is not in the list")

def retun_item(name):
    for list in grocery_list:
        if list["name"] == name:
            if not list["available"]:
             list["available"] = True
             print(f"{name} has been returned")
            else:
             print(f"{name} is already available")
            return
            print(f"{name} is not in the list")

# Example usage
add_item("rice", 2, 70)
add_item("oil", 1, 150)
add_item("sugar", 1, 40)
display_items()


search_item("rice")
check_out_item("rice")
display_items()

retun_item("rice")
display_items()

remove_item("oil")
display_items()



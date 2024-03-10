Grocery Management System
A simple Python program for managing grocery items, including adding, removing, searching, checking out, and returning items.

# Features
- Add Item: Add a new grocery item to the list with its name, quantity, and price.
- Remove Item: Remove a grocery item from the list.
- Display Items: Display all grocery items along with their details (name, quantity, price, availability).
- Search Item: Search for a grocery item by its name.
- Check Out Item: Mark a grocery item as checked out, changing its availability status.
- Return Item: Mark a checked-out grocery item as returned, changing its availability status.
# Installation
This project requires Python 3.6 or later. Clone the repository to your local machine:

```
git clone https://github.com/your-username/grocery-management-system.git
```
# Usage
- Open a terminal or command prompt.
- Navigate to the project directory.
- Run the program using Python:

```
python grocery_management_system.py
```
- Follow the on-screen instructions to interact with the grocery management system.
# Example

```
add_item("rice", 2, 70)
add_item("oil", 1, 150)
add_item("sugar", 1, 40)

display_items()

search_item("rice")
check_out_item("rice")
display_items()

return_item("rice")
display_items()

remove_item("oil")
display_items()
```
# License
This project is licensed under the MIT License.

# Contributing
Contributions are welcome! Please feel free to fork the repository and submit pull requests.



import string
import secrets
from tinydb import TinyDB
from tinydb import Query
Fruit = Query()
db = TinyDB("password_manager.json")

# Generate password
def password_gen(password_length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    print(password)
    return

# Add new password to DB
def add_password():
    name = input("Password Name: ")
    url = input("URL: ")
    username = input("Username: ")
    password = input("Password: ")
    db.insert({'name': name, 'url': url, 'username': username, 'password': password,})
    return

# Retrieve Password
def get_password():
    user_search = input("What is the name of the password: ")
    print(db.search(Fruit.name == user_search))
    return

# Update Password
def update_password():
    user_update = input("Name of the password you want to update: ")
    new_update_password = input("New password: ")
    db.update({'password': new_update_password}, Fruit.name == user_update)
    print("Password updated")
    return

# Delete Password
def delete_password():
    user_delete = input("Name of the password you want to delete: ")
    db.remove(Fruit.name == user_delete)
    print("Password successfully deleted")
    return


# Welcome Message
print("------------------------------")
print("Welcome to PassKNOX")
print("------------------------------\n")


# User Options
def user_options():
    print("1. GENERATE new password")
    print("2. ADD new password")
    print("3. VIEW password")
    print("4. UPDATE password")
    print("5. DELETE password")
    return


# Display User Options
print(user_options())

# User selects option via input
user_action = input("Please select an action 1-5: ")

# Generate new password
if user_action == "1":
    password_gen(12),

# Add new password to DB
elif user_action == "2":
    add_password()
    print("Password successfully added"),

# View password record from DB
elif user_action == "3":
    get_password(),

# Update/Edit password in DB
elif user_action == "4":
    update_password()
    print("Password successfully updated"),

# Delete password from DB
elif user_action == "5":
    delete_password()
    print("Password successfully deleted"),

else:
    print("Please select action 1-5")


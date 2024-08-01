from User import user

users = {}

def add_user():
    name = input("Enter your first and last name: ")
    library_id = input("Enter your library ID: ")
    #borrowed_books - need to add these with the method

    new_user = user(name, library_id)
    users[library_id] = new_user

    print(f"User '{name}' added successfully.")

def view_user_details():
    user_id = input("Enter the library ID of the user you would like to view: ")
    if user_id in users:
        user = users[user_id]
        print(f"User details: User Name: {user.get_name()}, Library ID: {user.get_user_id()}")
    else:
        print("User not found")

def display_users():
    if users:
        for user in users.values():
            print(f"User Name: {user.get_name()}, User ID: {user.get_user_id()}")
    else:
        print("No users currently in the database.")




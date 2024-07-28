from User import user

users = {}

def add_user():
    name = input("Enter your first and last name: ")
    library_id = input("Enter your library ID: ")
    #borrowed_books - need to add these with the method

    new_user = user(name, library_id)
    users.append(new_user)

def view_user_details():
    name = input("Enter the name of the user you would like to view: ")
    if name in users:
        user = users[name]
        print(f"User details: User Name: {user.get_name()}, Library ID: {user.get_library_id()}")
    else:
        print("User not found")

def display_users():
    if users:
        for user in users.values():
            print(f"User Name: {user.get_name()}, Library ID: {user.get_library_id()}")
        else:
            print("No users currently in the database.")


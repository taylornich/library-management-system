from Genre import genre

genres = {}

def add_genre():
    name = input("Enter the new genre to be added: ")
    description = input("Enter a brief decription of the genre to be added: ")
    category = input("Please enter the category that this genre belongs to, fiction or nonfiction: ")

    new_genre = genre(name, description, category)
    genres.append(new_genre)

def view_genre_details():
    name = input("Enter the name of the genre you would like to view: ")
    if name in genres:
        genre = genres[name]
        print(f"Genre details: Name: {genre.get_name()}, Description: {genre.get_description()}, Category: {genre.get_category()}")
    else:
        print("Genre not found in the database")

def display_genres():
    if genres:
        for genre in genres.values():
            print(f"Name: {genre.get_name()}, Description: {genre.get_description}, Category: {genre.get_category()}")
    else: 
        print("No genres currently in the database")

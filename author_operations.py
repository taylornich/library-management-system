from Author import author

authors = {}

def add_author():
    author_name = input("Enter the name of the author: ")
    biography = input("Enter a short biography for the author or type N/A: ")

    new_author = author(author_name, biography)
    authors[author_name] = new_author
    print(f"Author {new_author} added successfully.")

def view_author_details():
    author_name = input("Enter the name of the author you would like to view: ")
    if author_name in authors:
        author = authors[author_name]
        print(f"Author details: name: {author.get_author_name()}, Biography: {author.get_biography()}")
    else:
        print("Author not in the database.")

def display_authors():
    if authors:
        for author in authors.values():
            print(f"Name: {author.get_author_name()}, Biography: {author.get_biography()}")
    else:
        print("No authors currently in database.")



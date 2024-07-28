from Author import author

authors = {}

def add_author():
    name = input("Enter the name of the author: ")
    biography = input("Enter a short biography for the author or type N/A: ")

    new_author = author(name, biography)
    authors.append(new_author)

def view_author_details():
    name = input("Enter the name of the author you would like to view: ")
    if name in authors:
        author = authors[name]
        print(f"Author details: name: {author.get_name()}, Biography: {author.get_biography()}")

def display_authors():
    if authors:
        for author in authors.values():
            print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")
        else:
            print("No authors currently in database.")


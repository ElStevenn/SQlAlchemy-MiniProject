from datetime import date
from database_conection import *

author_data = [
    {
        "Name": "Jane Austen",
        "Birth_date": date(1775, 12, 16),
    },
    {
        "Name": "Mark Twain",
        "Birth_date": date(1835, 11, 30),
    },
    {
        "Name": "Agatha Christie",
        "Birth_date": date(1890, 9, 15),
    },
    {
        "Name": "J.R.R. Tolkien",
        "Birth_date": date(1892, 1, 3),
    },
    {
        "Name": "Gabriel García Márquez",
        "Birth_date": date(1927, 3, 6),
    },
    {
        "Name": "Maya Angelou",
        "Birth_date": date(1928, 4, 4),
    },
    {
        "Name": "Haruki Murakami",
        "Birth_date": date(1949, 1, 12),
    },
    {
        "Name": "Chimamanda Ngozi Adichie",
        "Birth_date": date(1977, 9, 15),
    },
    {
        "Name": "Neil Gaiman",
        "Birth_date": date(1960, 11, 10),
    },
    {
        "Name": "Hermann Hesse",
        "Birth_date": date(1877, 7, 2),
    },
    {
        "Name": "Isabel Allende",
        "Birth_date": date(1942, 8, 2),
    },
    {
        "Name": "Toni Morrison",
        "Birth_date": date(1931, 2, 18),
    },
    {
        "Name": "Yuval Noah Harari",
        "Birth_date": date(1976, 2, 24),
    },
    {
        "Name": "J.K. Rowling",
        "Birth_date": date(1965, 7, 31),
    },
    {
        "Name": "Gabriela Mistral",
        "Birth_date": date(1889, 4, 7),
    },
    {
        "Name": "Kazuo Ishiguro",
        "Birth_date": date(1954, 11, 8),
    },
    {
        "Name": "Leo Tolstoy",
        "Birth_date": date(1828, 9, 9),
    },
    {
        "Name": "Virginia Woolf",
        "Birth_date": date(1882, 1, 25),
    },
    {
        "Name": "Octavio Paz",
        "Birth_date": date(1914, 3, 31),
    },
    {
        "Name": "Ayn Rand",
        "Birth_date": date(1905, 2, 2),
    },
    {
        "Name": "Roald Dahl",
        "Birth_date": date(1916, 9, 13),
    },
]

books_data = [
    {'Title': 'The Alchemist', 'Publication_Date': date(1988, 4, 25)},
    {'Title': 'To Kill a Mockingbird', 'Publication_Date': date(1960, 7, 11)},
    {'Title': '1984', 'Publication_Date': date(1949, 6, 8)},
    {'Title': 'The Great Gatsby', 'Publication_Date': date(1925, 4, 10)},
    {'Title': 'Pride and Prejudice', 'Publication_Date': date(1813, 1, 28)},
    {'Title': 'The Hobbit', 'Publication_Date': date(1937, 9, 21)},
    {'Title': 'Brave New World', 'Publication_Date': date(1932, 3, 2)},
    {'Title': 'Harry Potter and the Sorcerer\'s Stone', 'Publication_Date': date(1997, 6, 26)},
    {'Title': 'The Catcher in the Rye', 'Publication_Date': date(1951, 7, 16)},
    {'Title': 'Lord of the Flies', 'Publication_Date': date(1954, 9, 17)},
    {'Title': 'The Da Vinci Code', 'Publication_Date': date(2003, 3, 18)},
    {'Title': 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe', 'Publication_Date': date(1950, 10, 16)},
    {'Title': 'The Hunger Games', 'Publication_Date': date(2008, 9, 14)},
    {'Title': 'Fahrenheit 451', 'Publication_Date': date(1953, 10, 19)},
    {'Title': 'Moby-Dick', 'Publication_Date': date(1851, 10, 18)},
    {'Title': 'The Shining', 'Publication_Date': date(1977, 1, 28)},
    {'Title': 'Gone with the Wind', 'Publication_Date': date(1936, 6, 30)},
    {'Title': 'The Lord of the Rings: The Fellowship of the Ring', 'Publication_Date': date(1954, 7, 29)},
    {'Title': 'One Hundred Years of Solitude', 'Publication_Date': date(1967, 5, 30)},
    {'Title': 'The Color Purple', 'Publication_Date': date(1982, 9, 26)},
]

genres_data = [
    {'Genere_Name': 'Fiction'},
    {'Genere_Name': 'Mystery'},
    {'Genere_Name': 'Science Fiction'},
    {'Genere_Name': 'Fantasy'},
    {'Genere_Name': 'Romance'},
    {'Genere_Name': 'Historical Fiction'},
    {'Genere_Name': 'Thriller'},
    {'Genere_Name': 'Horror'},
    {'Genere_Name': 'Adventure'},
    {'Genere_Name': 'Humor'},
    {'Genere_Name': 'Non-Fiction'},
    {'Genere_Name': 'Poetry'},
    {'Genere_Name': 'Drama'},
    {'Genere_Name': 'Young Adult'},
    {'Genere_Name': 'Children\'s'},
    {'Genere_Name': 'Biography'},
    {'Genere_Name': 'Self-Help'},
    {'Genere_Name': 'Classic Fiction'},
    {'Genere_Name': 'Magical Realism'},
]


engine = create_engine('sqlite:///databases/databases.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session() # Session maker

books_instances = [Books(Title=book['Title'], Publication_Date=book['Publication_Date']) for book in books_data]
genre_instances = [Generes(Genere_Name=genre['Genere_Name']) for genre in genres_data]
author_instances = [Authors(Name=author['Name'], Birth_date=author['Birth_date']) for author in author_data]


session.add_all(books_instances)
session.add_all(genre_instances)
session.add_all(author_instances)


session.commit()
session.close()


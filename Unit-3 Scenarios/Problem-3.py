import csv
import re

# Read book records from CSV file
with open("books.csv", "r") as file:
    reader = csv.DictReader(file)
    books = list(reader)

# Display all book details
print("Book Details:")
for book in books:
    print(book)

# Get keyword from user
keyword = input("\nEnter title keyword: ")

# Create regular expression pattern
pattern = "^" + keyword

# Search books whose title starts with the keyword
print("\nMatching Books:")

for book in books:
    if re.match(pattern, book["Title"], re.IGNORECASE):
        print(book)


# books.csv:
# Book ID,Title,Author,Price
# 101,Python Programming,John Smith,500
# 102,Data Science Basics,Anita Sharma,600
# 103,Python for Beginners,Rahul Verma,450
# 104,Database Management,Neha Patel,550
# 105,Java Programming,Amit Kumar,400


# OUTPUT:
# Book Details:
# {'Book ID': '101', 'Title': 'Python Programming', 'Author': 'John Smith', 'Price': '500'}
# {'Book ID': '102', 'Title': 'Data Science Basics', 'Author': 'Anita Sharma', 'Price': '600'}
# {'Book ID': '103', 'Title': 'Python for Beginners', 'Author': 'Rahul Verma', 'Price': '450'}
# {'Book ID': '104', 'Title': 'Database Management', 'Author': 'Neha Patel', 'Price': '550'}
# {'Book ID': '105', 'Title': 'Java Programming', 'Author': 'Amit Kumar', 'Price': '400'}
#
# Enter title keyword: Python
#
# Matching Books:
# {'Book ID': '101', 'Title': 'Python Programming', 'Author': 'John Smith', 'Price': '500'}
# {'Book ID': '103', 'Title': 'Python for Beginners', 'Author': 'Rahul Verma', 'Price': '450'}

import csv
import requests

URL = "https://openlibrary.org/subjects/programming.json"
parameters = {"limit":50}
min_year = 2000
output_file = "past_2000_books.csv"

response = requests.get( URL , params=parameters)
data = response.json()
books = data.get("works" , [])
filtered_books = []


for book in books :

    publish_year = book["first_publish_year"]
    authors = book.get("authors" , [])

    if authors:
        author = authors[0].get("name")
    else:
        author = "Unknown"

    if publish_year and publish_year >= min_year :
        filtered_books.append({
            "Title":book.get("title","N/A") ,
            "Author":author ,
            "Publish Year":publish_year
            })

with open(output_file , "w" , newline="" , encoding="utf-8") as file:
    writer = csv.DictWriter(file , fieldnames=["Title" , "Author" , "Publish Year"])
    writer.writeheader()
    writer.writerows(filtered_books)

print(f"a total number of {len(filtered_books)} books were written in the CSV file.")
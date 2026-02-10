import csv
import requests

parameters = {"limit":50}
response = requests.get("https://openlibrary.org/subjects/programming.json" , params=parameters)
data = response.json()
books = data["works"]
filtered_books = []

for book in books :
    publish_year = book["first_publish_year"]
    if publish_year > 2000 :
        filtered_books.append({"Title":book["title"] , "Author":book["authors"][0]["name"] , "Publish Year":publish_year})

with open("past_2000_books.csv" , "w" , newline="" , encoding="utf-8") as file:
    writer = csv.DictWriter(file , fieldnames=["Title" , "Author" , "Publish Year"])
    writer.writeheader()
    writer.writerows(filtered_books)

print(f"a total number of {len(filtered_books)} books were written in the CSV file.")
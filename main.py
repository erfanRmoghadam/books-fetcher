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
years = []

#loop started
for book in books :

    publish_year = book["first_publish_year"]
    authors = book.get("authors" , [])

    if authors:
        author = authors[0].get("name")
    else:
        author = "Unknown"

    if publish_year and publish_year >= min_year :
        decade = f"{(publish_year//10)*10}s"
        filtered_books.append({
            "Title":book.get("title","N/A") ,
            "Author":author ,
            "Publish Year":publish_year,
            "Decade":decade, 
            "Edition Count":book.get("edition_count")
            })
#loop ended


filtered_books.sort(key= lambda x : x["Publish Year"] , reverse=True)


with open(output_file , "w" , newline="" , encoding="utf-8") as file:
    writer = csv.DictWriter(file , fieldnames=["Title" , "Author" , "Publish Year" , "Decade" , "Edition Count" ])
    writer.writeheader()
    writer.writerows(filtered_books)


for book in filtered_books:
    years.append(book["Publish Year"])

newest_book = filtered_books[0]["Title"]
oldest_book = filtered_books[-1]["Title"]


print("\nSummary Report")
print("-" * 90)
print(f"Total books fetched : {len(books)}")
print(f"Books published after {min_year} : {len(filtered_books)}")
print(f"Newest book was '{newest_book}' which was published in {max(years)}")
print(f"Oldest book was '{oldest_book}' which was published in {min(years)}")
print(f"Average of books published years : {sum(years) // len(years)}")
print(f"Full details of books published after {min_year} were saved in {output_file} file.")
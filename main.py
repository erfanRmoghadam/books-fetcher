import csv
import requests
from typing import Any, Dict, List, TypedDict

class Book(TypedDict):
    Title: str
    Author: str
    PublishYear: int
    Decade: str
    EditionCount: int | None


URL: str = "https://openlibrary.org/subjects/programming.json"
parameters: Dict[str, int] = {"limit": 50}
MIN_YEAR: int = 2000
OUTPUT_FILE: str = "past_2000_books.csv"

response: requests.Response = requests.get(URL, params=parameters)
data: Dict[str, Any] = response.json()

books: List[Dict[str, Any]] = data.get("works", [])
filtered_books: List[Book] = []
years: List[int] = []


for book in books:

    publish_year: int | None = book.get("first_publish_year")
    authors: List[Dict[str, Any]] = book.get("authors", [])

    if authors:
        author: str = authors[0].get("name", "Unknown")
    else:
        author = "Unknown"

    if publish_year and publish_year >= MIN_YEAR:
        decade: str = f"{(publish_year//10)*10}s"

        filtered_books.append(
            {
                "Title": book.get("title", "N/A"),
                "Author": author,
                "Publish Year": publish_year,
                "Decade": decade,
                "Edition Count": book.get("edition_count"),
            }
        )


filtered_books.sort(key=lambda x: x["Publish Year"], reverse=True)


with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer: csv.DictWriter = csv.DictWriter(
        file, fieldnames=["Title", "Author", "Publish Year", "Decade", "Edition Count"]
    )
    writer.writeheader()
    writer.writerows(filtered_books)


for book in filtered_books:
    years.append(book["Publish Year"])

newest_book: str = filtered_books[0]["Title"]
oldest_book: str = filtered_books[-1]["Title"]


print("\nSummary Report")
print("-" * 90)
print(f"Total books fetched : {len(books)}")
print(f"Books published after {MIN_YEAR} : {len(filtered_books)}")
print(f"Newest book was '{newest_book}' which was published in {max(years)}")
print(f"Oldest book was '{oldest_book}' which was published in {min(years)}")
print(f"Average of books published years : {sum(years) // len(years)}")
print(
    f"Full details of books published after {MIN_YEAR} were saved in {OUTPUT_FILE} file."
)

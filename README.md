# books-fetcher
This project is a simple Python script that fetches programming-related book data from the Open Library API, filters books published after the year 2000, and saves the results into a CSV file which contains the book title, author and publish year.

It’s a small but practical example of working with:
Public APIs
HTTP requests
JSON data
CSV file handling in Python.

Features:
Fetches 50 programming books from Open Library and filters books published after 2000
Extracts:
book title, author name and publish year
Writes the filtered data into a CSV file
And lastly prints a summary of how many books were saved.

Requirements:
Make sure you have Python 3.x installed.
Required Python libraries:
requests (external)
csv (built-in)

And it was mentioned earlier, the data source of this program is:
Open Library API (https://openlibrary.org/subjects/programming.json) 
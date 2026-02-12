# books-fetcher
This project is a simple Python script that fetches programming-related book data from the Open Library API, filters books published after the year 2000, and saves the results into a CSV file which contains the book title, author and publish year.

  

It’s a small but practical example of working with:  
Public APIs  
HTTP requests  
JSON data  
CSV file handling in Python.

  

Features:  
Fetches some programming books data from Open Library and filters books published after 2000  
Handles missing or incomplete data safely   
Extracts:  
Book title, author name, publish year and decade, and edition count  
Sorts all books based on their published year (from newest to oldest)
Writes the filtered data into a CSV file  
And lastly prints a detailed summary in terminal including:  
The total number of how many books were fetched  
The total number of how many books were published after 2000  
Newest published book (title and year)  
Oldest published book (title and year)  
And output CSV file name.  
This separation keeps the CSV file clean while still providing useful insights for the user.  


The project also follows clean code and professional practices:  
Code was formatted using Black for consistent style and PEP8 compliance  
Generated CSV file is ignored in the repository using a .gitignore file  
Dependencies are listed in requirements.txt for easy setup  



Requirements:
Make sure you have Python 3.x installed.  
Required Python libraries:  
requests (external)  
csv (built-in)


And as it was mentioned earlier, the data source of this program is:  
Open Library API (https://openlibrary.org/subjects/programming.json) 
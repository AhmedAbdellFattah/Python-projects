import requests
from bs4 import BeautifulSoup

def scrape_books_info(url):
    """
    Scrapes book information from the provided URL and prints the title and rating.
    
    Args:
        url (str): The URL of the website to scrape.

    Returns:
        None
    """
    # Make a request to the specified URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Select all book articles on the page
    books = soup.select("article")

    # Iterate through each book and extract title and rating information
    for book in books:
        title = book.select_one("h3 a")["title"]
        rating = book.select_one("p[class*=star-rating]")["class"][1]
        print(f"Book titled: {title} has a rating of: {rating} stars")

# URL of the website to scrape
url_to_scrape = "https://books.toscrape.com/"

# Call the function to scrape and print book information
scrape_books_info(url_to_scrape)

import requests as r
from bs4 import BeautifulSoup
import pandas as pd 

# Fonction pour extraire le titre d'un livre
def extract_title(book: BeautifulSoup) -> str:
    """Extract the title of a book from a BeautifulSoup object.
    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The title of the book.
    """
    return book.find("h3").text

# Fonction pour extraire le prix d'un livre
def extract_price(book: BeautifulSoup) -> str:
    """Extract the price of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The price of the book.
    """
    return book.find("p", class_="price_color").text

# Fonction pour extraire la note d'un livre
def extract_rating(book: BeautifulSoup) -> str:
    """Extract the rating of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The rating of the book.
    """
    return book.find("p", class_="star-rating").get('class')[1]

# Fonction pour extraire la disponibilité d'un livre
def extract_availability(book: BeautifulSoup) -> str:
    """Extract the availability of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The availability of the book.
    """
    return book.find("p", class_="instock availability").text.strip()

# Fonction qui combine les informations d'un livre dans un dictionnaire
def extract_book_info(book: BeautifulSoup) -> dict:
    """Extract all information of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        dict: A dictionary containing the title, price, rating, and availability of the book.
    """
    
    table_dict = {
        'title': extract_title(book),
        'price': extract_price(book),
        'rating': extract_rating(book),
        'availability': extract_availability(book)
    }
    return table_dict
#get books 
def get_books_html(url: str) -> BeautifulSoup:
    """Fetch the HTML content of a book page.

    Args:
        url (str): The URL of the book page.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the HTML content.
    """
    response = r.get(url)
    # print(f"Status code: ", response.status_code)
    html_content = response.content
    sp = BeautifulSoup(html_content, "html.parser")
    # return sp

    books = sp.find_all("article", class_="product_pod")
    return books

    # list_dict = [extract_book_info(book) for book in books]
    # print(list_dict[:5])
    
# Parcourir les pages et récupérer les livres
def scrape_books(pages: int) -> list[dict]:
    """Scrape books from the specified number of pages.

    Args:
        pages (int): The number of pages to scrape.

    Returns:
        list: A list of dictionaries containing books information.
    """
    pg_url = "https://books.toscrape.com/catalogue/page-{}.html"

    all_books = []

    for pg_num in range(1, pages + 1):
        url = pg_url.format(pg_num)
        books = get_books_html(url)
        data_books = [extract_book_info(book) for book in books]
        all_books.extend(data_books)
        # print(all_books)
    return all_books
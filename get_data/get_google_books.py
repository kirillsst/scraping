import requests as r 

def fetch_books_from_api(query="food", maxResults= 40, orderBy="relevance"):
    url = "https://www.googleapis.com/books/v1/volumes"

    params = {
        "q": "food",
        "filter": "paid-ebooks", 
        "maxResults": 40,
        "orderBy": "relevance"
    }

    response = r.get(url, params=params)
    response.raise_for_status()
    return response.json().get("items", [])
# books = fetch_books_from_api()
# print(len(books))
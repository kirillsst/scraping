from get_data.get_scraping_data import scrape_books
from get_data.get_google_books import fetch_books_from_api
from process_data.process_scrapping_data import convert_types
from process_data.clean_books_data import clean_books_data
from database.insert_data import insert_and_count_books
import pandas as pd 

def run_scraping_pipeline(pages:int, database:str):
    print("Scraping sur website...")
    books = scrape_books(5)
    df_scraped = pd.DataFrame(books)

    print("Scraping Google Books API...")
    books_api = fetch_books_from_api()
    df_api = clean_books_data(books_api)

    print("Concat.....")
    cnc = pd.concat([df_scraped, df_api], ignore_index=True)

    print("Traitment...")
    df_clean = convert_types(df_scraped)

    print(" Insertion dans la base de données...")
    insert_and_count_books(df_clean, database)

    print("Sauvgarde")
    df_clean.to_csv("~/scraping_repo/scraping/data/data_scraping.csv", index=False)
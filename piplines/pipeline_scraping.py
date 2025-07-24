from get_data.get_scraping_data import scrape_books
from process_data.process_scrapping_data import convert_types
from database.insert_data import insert_and_count_books
import pandas as pd 

def run_scraping_pipeline(pages:int, database:str):
    print("Scraping...")
    books = scrape_books(5)
    df = pd.DataFrame(books)

    print("Traitment")
    df_clean = convert_types(df)

    print("Sauvgarde")
    df_clean.to_csv("~/scraping_repo/scraping/data/data_scraping.csv", index=False)
    

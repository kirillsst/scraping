from piplines import pipeline_scraping as ps
import argparse

def main():
    try:
        parser = argparse.ArgumentParser(description="Extraction de données automatisée pour le site  books.toscrape.com")
        parser.add_argument(
            '--pages',
            type=int, 
            default=1,
            help='Nombre de pages à scraper'
        )
        parser.add_argument(
            '--database',
            type=str,
            default="book_store",
            help='Nom de DataBase'
        )

        args = parser.parse_args()
        ps.run_scraping_pipeline(args.pages, args.database)
        
        print("Scraping {args.pages} page(s) dans la base {args.database}.db ...")
    except Exception as i:
        print(f"Error {i}")

if __name__ == "__main__":
    main()
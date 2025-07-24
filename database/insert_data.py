import sqlite3
import pandas as pd
import os

def insert_and_count_books(df_books: pd.DataFrame, db_name: str = "book_store.db") -> int:
    """
    Insère les livres dans la base de données et retourne le nombre total de livres.

    Args:
        df_books (pd.DataFrame): Le DataFrame contenant les livres.
        db_name (str): Le nom de la base de données (par défaut "book_store.db").

    Returns:
        int: Le nombre total de livres insérés.
    """
    db_dir = "database" 
    os.makedirs(db_dir, exist_ok=True)#crée un dossier s'il n'existe pas

    db_path = f"{db_dir}/{db_name}"

    with sqlite3.connect(db_path) as connection:
        df_books.to_sql('books', connection, if_exists='replace', index=False)
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM books")
        res = cursor.fetchone()[0]
        print(f"Nombre de livres insérés dans la BDD : {res}")
        return res

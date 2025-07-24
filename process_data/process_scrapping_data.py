import pandas as pd 

# Fonction pour convertir la valeur de availability en booléen
def convert_availability(value : str) -> bool:
    """Convert the availability value to a boolean.

    Args:
        value (str): The availability status of the book.

    Returns:
        bool: True if the book is available, False otherwise.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return "In stock" in value.strip()
    return False
    return "In stock" in value

# # Créer une fonction convert_types qui combine les traitements faits dans les cellules précédentes
def convert_types(df_books: pd.DataFrame) -> pd.DataFrame:
    """Convert the types of the DataFrame columns to appropriate types.

    Args:
        df_books (pd.DataFrame): The DataFrame containing book data.

    Returns:
        pd.DataFrame: The DataFrame with converted types.
    """
    df_books["title"] = df_books["title"].astype("string")
    df_books["rating"] = df_books["rating"].map({"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}).astype("Int64")
    df_books["price"] = df_books["price"].astype(str).str.replace("£", "").astype(float)
    df_books["availability"] = df_books["availability"].apply(convert_availability)

    return df_books
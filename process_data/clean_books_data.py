import pandas as pd

def clean_books_data(items):
    books_list = []

    for book in items:
        volume_info = book.get('volumeInfo', {})
        sale_info = book.get('saleInfo', {})

        title = volume_info.get('title', None)
        price = sale_info.get('retailPrice', {}).get('amount', None)
        rating = volume_info.get('averageRating', None)

        books_list.append({
            'title': title,
            'price': price,
            'rating': rating
        })

        df = pd.DataFrame(books_list).dropna().reset_index(drop=True)
        df['availability'] = False

        return df
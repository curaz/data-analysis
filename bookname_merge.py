# Book과 Bookstats의 정보를 merge합니다.
import pandas as pd
books = pd.read_csv('final_merged_book.csv')
titles = pd.read_csv('files/book.csv')[['id', 'title']]

united_df = pd.merge(books, titles, on='id', how='left')
united_df.to_csv('example_f.csv')
# Book과 Bookstats의 정보를 merge합니다.
import pandas as pd
stats = pd.read_csv('final_BookStats.csv')
books = pd.read_csv('final_book_entity.csv', encoding='euc-kr')

united_df = pd.merge(stats, books, on='id', how='outer')
united_df.to_csv('example.csv', encoding='euc-kr')
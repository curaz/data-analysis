import pandas as pd
import ast

path = ''
# csv 파일 토대로, 유저가 관련 있는 모든 책 불러오기
reader_csv = pd.read_csv(path + 'csv/user-book.csv')
item_list = pd.read_csv(path + 'csv/item_list.csv')
user_list = pd.read_csv(path + 'csv/user_list.csv')
# 관련 있는 모든 책 => remap id로 변환

# train / test 파일로 저장하기
f= open("txt/train.txt","w+")

user_id = pd.merge(reader_csv, user_list, how='outer', on='id')

id_to_remap_id = dict(zip(item_list['id'], item_list['remap_id']))
def remap_books(book_list_str):
    # 문자열로 되어 있는 리스트를 실제 리스트로 변환
    if pd.isna(book_list_str):
        return []  # nan 값을 빈 리스트로 변환
    book_list = ast.literal_eval(book_list_str)
    # 리스트의 각 id를 remap_id로 변환
    remapped_list = [id_to_remap_id.get(book_id, book_id) for book_id in book_list if book_id in id_to_remap_id]
    return remapped_list

# user_book_df의 books 열에 함수 적용
user_id['books'] = user_id['books'].apply(remap_books)

user_id.sort_values(by='remap_id', inplace=True)
for index, row in user_id.iterrows():
    if pd.isna(row['remap_id']):
        continue
    data = f"\n{int(row['remap_id'])} "
    if len(row['books'])>0:
        data += ' '.join(map(str, row['books']))
    f.write(data)

# 결과를 새로운 CSV 파일로 저장
user_id.to_csv('user-book-remapped.csv', index=False)
f.close()
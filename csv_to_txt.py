#1. csv 불러오기
#2. txt 파일 생성
#2. 각 book 데이터 순회하며 bookid - entity 컬럼들 txt 파일에 저장

import pandas as pd

items = pd.read_csv('csv/item_list.csv', encoding='euc-kr', encoding_errors='ignore')
f= open("txt/item_list.txt","w+")
f.write('id, remap_id\n')
for index, row in items.iterrows():
    data = str(row['id']) + ' ' + str(row['remap_id']) + '\n'
    f.write(data)

f.close()
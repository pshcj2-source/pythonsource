#터미널 창에 uv pip install openpyxl /uv pip install pandas

import pandas as pd

user_list = pd.read_excel('sample.xlsx', sheet_name='Sheet1', engine='openpyxl')
print(user_list)
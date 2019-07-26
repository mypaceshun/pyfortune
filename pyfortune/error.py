from session import Session
import pandas as pd

s = Session()
s.login("yumemita@gmail.com", "yumemita99")

data_list = s.fetch_apply_list()
df = pd.io.json.json_normalize(data_list) #list to pandas.DataFrame
print(df)

detail = s.fetch_apply_detail(df["link"].iloc[2])
print(detail)
detail = s.fetch_apply_detail(df["link"].iloc[2])
print(detail)
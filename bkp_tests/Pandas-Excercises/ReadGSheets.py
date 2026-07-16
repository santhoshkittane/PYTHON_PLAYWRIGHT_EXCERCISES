import pandas as pd

sheet_id = "1QW7UbI2l5A1uKjPxrTNCC1uQnt19MJkbvk_YeR0tRt0"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
df = pd.read_csv(url)
# 'Unnamed':["?","n.a"]
print(df.head())